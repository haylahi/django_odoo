# author: Liberty
# date: 2019/4/22 20:51

import base64
import os

from django.apps import apps
from django.conf import settings
from django.http import HttpResponse
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from base.utils import (
    make_error_resp, make_success_resp, json,
    generate_random_code, make_correct_path,
    create_file
)
from . import models
from . import serializer as s
from . import tasks


class UnitCreateListView(viewsets.ViewSet):
    # noinspection PyMethodMayBeStatic,PyUnusedLocal
    def show_unit_list(self, request, *args, **kwargs):
        # TODO 分页
        result = models.BaseUnit.objects.filter(is_active=True)
        serializer = s.BaseUnitSerializer(result, many=True)
        return Response(serializer.data)

    # noinspection PyMethodMayBeStatic,PyUnusedLocal
    def create_unit(self, request, *args, **kwargs):
        serializer = s.BaseUnitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UploadFileView(viewsets.ViewSet):
    """
    var attr = {
        'fApp': 'base', // not req
        'fModel': 'province', // not req
        'fField': '', // not req
        'fId': '1', // not req
        'fFileName': '',
        'fFileType': '',
        'fFIleData': '',
    };

    """

    # noinspection PyMethodMayBeStatic,PyUnusedLocal
    def upload_file(self, request, *args, **kwargs):
        # TODO 判断逻辑问题 传入值的问题  null '' Nan ...
        user_token, front_data = request.data.get('token', None), request.data.get('data', None)
        if user_token and front_data:
            try:
                json_data = json.loads(front_data)
            except Exception as e:
                _msg = 'UserError: request body\'s data error: {e}'.format(e=e)
                return Response(make_error_resp(_msg))

            if not (json_data.get('fFileName') and json_data.get('fFileType') and json_data.get('fFIleData')):
                _msg = 'UserError: request body data error'
                return Response(make_error_resp(_msg))
            # 尝试 base64 解码
            _b64 = json_data.get('fFIleData')
            if ',' in _b64:
                _b64 = _b64.split(',')[1]
            try:
                base64.b64decode(_b64)
            except Exception as e:
                _msg = 'UserError: {e}'.format(e=e)
                return Response(make_error_resp(_msg))

            _front_file_name = json_data.get('fFileName')
            _file_suffix = os.path.splitext(_front_file_name)[1]
            if _file_suffix == '':
                _msg = 'UserError: request body data error'
                return Response(make_error_resp(_msg))

            # 获取一个随机的文件名
            _f = generate_random_code()

            file_object_path = '{f}{s}'.format(f=_f, s=_file_suffix)
            file_object_attr = {
                'file_name': _front_file_name,
                'file_type': json_data.get('fFileType'),
                'file_suffix': _file_suffix,
                'file_path': file_object_path
            }

            fApp, fModel, fField, fId = json_data.get('fApp'), json_data.get('fModel'), \
                                        json_data.get('fField'), json_data.get('fId')
            if fApp and fModel:
                try:
                    model_object = apps.get_model(fApp, fModel)
                except Exception as e:
                    _msg = 'UserError: {e}'.format(e=e)
                    return Response(make_error_resp(_msg))

                if fId:
                    try:
                        int(fId)
                    except Exception as e:
                        _msg = 'UserError: {e}'.format(e=e)
                        return Response(make_error_resp(_msg))
                    exist_tag = model_object.objects.filter(is_active=True, id=fId).exists()
                    if exist_tag is False:
                        _msg = 'Error: 404 Not Found'
                        return Response(make_error_resp(_msg))
                else:
                    _msg = 'Error: if app and model exists, then id is required'
                    return Response(make_error_resp(_msg))

                # 保存图片 make-path
                file_object_path = '{app}/{model}/{file}'.format(app=fApp, model=fModel, file=file_object_path)
                file_object_attr.update({
                    'app_label': fApp,
                    'model_name': fModel,
                    'model_id': fId,
                    'file_path': file_object_path
                })

                if fField:
                    try:
                        # noinspection PyProtectedMember
                        model_object._meta.get_field(fField)
                    except Exception as e:
                        _msg = 'UserError: {e}'.format(e=e)
                        return Response(make_error_resp(_msg))
                    file_object_attr.update({'model_field': fField})

            # ------------------- 检查完成 ----------------------------------------------

            _path = str(make_correct_path(settings.MEDIA_ROOT, file_object_path))
            _dir = os.path.dirname(_path)
            if not os.path.exists(_dir):
                os.makedirs(_dir)
            _b64 = base64.b64decode(_b64)

            # FIXME 修改这里的逻辑 可能会出现重复创建的情况  创建成功弹出一个通知
            try:
                res = tasks.tasks_create_file.delay('create_file', path=_path, content=_b64)
                res.get(timeout=0.5)
                print('--> celery task success')
            except:
                create_file(_path, _b64)
                print('create file success')

            models.FileObject.objects.create(**file_object_attr)
            _ret = make_success_resp()
            return Response(_ret)
        # if user_token and front_data:
        else:
            _msg = 'UserError: request body error.'
            return Response(make_error_resp(_msg))
