# author: Liberty
# date: 2019/4/28 19:02

import requests

for i in range(100):
    requests.get('http://127.0.0.1:8000/school/test/')

d1 = """{'help_text': '', 'default': <class 'django.db.models.fields.NOT_PROVIDED'>, 'blank': False, 'unique_for_month': None, 'column': 'name', 
'_unique': False, 'concrete': True, 'creation_counter': 311, 'attname': 'name', 'name': 'name', 'null': False, 'serialize': True, 
'remote_field': None, '_db_tablespace': None, 'verbose_name': '考试名称', 'editable': True, 'primary_key': False, 'db_column': None, 
'is_relation': False, 'cached_col': Col(school_examination, school.Examination.name), '_verbose_name': '考试名称', 
'validators': [<django.core.validators.MaxLengthValidator object at 0x0000000006778B00>], 'unique_for_year': None, 
'choices': [], 'auto_created': False, 'db_index': False, 'model': <class 'school.models.Examination'>,
 'unique_for_date': None, 'max_length': 255, '_validators': [], 'error_messages': {'invalid_choice': 'Value %(value)r is not a valid choice.',
  'blank': 'This field cannot be blank.', 'unique_for_date': '%(field_label)s must be unique for %(date_field_label)s %(lookup_type)s.',
   'unique': '%(model_name)s with this %(field_label)s already exists.', 'null': 'This field cannot be null.'}, '_error_messages': None}"""

"""
{'unique_for_month': None, 'null': False, '_error_messages': None, 'name': 'test_tags', '_validators': [], 'default': <class 'django.db.models.fields.NOT_PROVIDED'>, 
 '_verbose_name': '标签',
  'db_index': False,
 'editable': True, 'concrete': True, 'max_length': None, 'serialize': True, 'column': 'test_tags', 
   'remote_field': <ManyToManyRel: school.examination>, 'creation_counter': 315, 'verbose_name': '标签', 'has_null_arg': False, 'validators': [], 'db_column': None, 
   'unique_for_date': None, 'opts': <Options for Examination>, 'm2m_reverse_target_field_name': <function ManyToManyField.contribute_to_related_class.<locals>.<lambda> at 0x000000000673B6A8>,
    '_unique': False,  'attname': 'test_tags', 'related_model': <class 'school.models.TestTag'>,
      'error_messages': {'null': 'This field cannot be null.', 'unique_for_date': '%(field_label)s must be unique for %(date_field_label)s %(lookup_type)s.',
       'unique': '%(model_name)s with this %(field_label)s already exists.', 'invalid_choice': 'Value %(value)r is not a valid choice.', 'blank': 'This field cannot be blank.'},
        'help_text': '', '_db_tablespace': None, 'auto_created': False, 'primary_key': False, 
         'swappable': True, 'choices': [], 'is_relation': True, 'm2m_target_field_name': <function ManyToManyField.contribute_to_related_class.<locals>.<lambda> at 0x000000000673B378>, 
         'unique_for_year': None, 'db_table': None, 'blank': True, 'model': <class 'school.models.Examination'>}

"""


"""
{'_error_messages': None, 'editable': True, 'is_relation': True, 'creation_counter': 312, 'name': 'course_map', 'db_column': None, 'from_fields': ['self'], 'column': 'course_map_id', 
'attname': 'course_map_id', '_unique': False, 'primary_key': False, 'unique_for_year': None, 'related_model': <class 'school.models.ClassCourseMap'>, 
'error_messages': {'invalid_choice': 'Value %(value)r is not a valid choice.', 'invalid': '%(model)s instance with %(field)s %(value)r does not exist.', 
'unique': '%(model_name)s with this %(field_label)s already exists.', 'blank': 'This field cannot be blank.', 'null': 'This field cannot be null.', 
'unique_for_date': '%(field_label)s must be unique for %(date_field_label)s %(lookup_type)s.'}, 
'_db_tablespace': None, 'help_text': '', 'max_length': None, 'verbose_name': '课程', 'db_index': True, 'db_constraint': True, 'auto_created': False, 'blank': False, 'serialize': True,
 'to_fields': ['id'], 'swappable': True, '_verbose_name': '课程', '_validators': [], 'remote_field': <ManyToOneRel: school.examination>, 'concrete': True, 'unique_for_month': None, 
 'choices': [], 'validators': [], '_related_fields': [(<django.db.models.fields.related.ForeignKey: course_map>,
  <django.db.models.fields.AutoField: id>)], 'null': False, 'default': <class 'django.db.models.fields.NOT_PROVIDED'>, 
  'opts': <Options for Examination>, 'model': <class 'school.models.Examination'>, 'unique_for_date': None}


"""

"""
{'blank': True, '_verbose_name': '标签', '_unique': False,
 'm2m_reverse_field_name': functools.partial(<bound method ManyToManyField._get_m2m_reverse_attr of <django.db.models.fields.related.ManyToManyField: test_tags>>, 
 <ManyToManyRel: school.examination>, 'name'), 
 'm2m_target_field_name': <function ManyToManyField.contribute_to_related_class.<locals>.<lambda> at 0x0000000006772620>, 
 '_validators': [], 
 'm2m_reverse_target_field_name': <function ManyToManyField.contribute_to_related_class.<locals>.<lambda> at 0x0000000006772510>, 'creation_counter': 315, 
 'choices': [], 'related_model': <class 'school.models.TestTag'>, 
 'm2m_reverse_name': functools.partial(<bound method ManyToManyField._get_m2m_reverse_attr of <django.db.models.fields.related.ManyToManyField: test_tags>>, 
 <ManyToManyRel: school.examination>, 'column'), '_db_tablespace': None, 
 'm2m_db_table': functools.partial(<bound method ManyToManyField._get_m2m_db_table of <django.db.models.fields.related.ManyToManyField: test_tags>>,
  <Options for Examination>), '_m2m_name_cache': 'examination',
   'error_messages': {'unique_for_date': '%(field_label)s must be unique for %(date_field_label)s %(lookup_type)s.',
    'blank': 'This field cannot be blank.', 'invalid_choice': 'Value %(value)r is not a valid choice.', 
    'null': 'This field cannot be null.', 'unique': '%(model_name)s with this %(field_label)s already exists.'}, 
    'column': 'test_tags', 'null': False, 'help_text': '', 'concrete': True, '_error_messages': None, 
    'verbose_name': '标签', 'model': <class 'school.models.Examination'>, 'validators': [], 
    'serialize': True, 'unique_for_date': None, 'unique_for_year': None, 'db_index': False, 
    'm2m_field_name': functools.partial(<bound method ManyToManyField._get_m2m_attr of <django.db.models.fields.related.ManyToManyField: test_tags>>,
     <ManyToManyRel: school.examination>, 'name'), 'db_table': None, 'primary_key': False,
      'm2m_column_name': functools.partial(<bound method ManyToManyField._get_m2m_attr of <django.db.models.fields.related.ManyToManyField: test_tags>>, 
      <ManyToManyRel: school.examination>, 'column'),
       'default': <class 'django.db.models.fields.NOT_PROVIDED'>, 'auto_created': False, 'db_column': None, 
       'has_null_arg': False, '_m2m_reverse_name_cache': 'testtag', 'swappable': True, 'unique_for_month': None, 'name': 'test_tags',
        'opts': <Options for Examination>, 'attname': 'test_tags',
         'remote_field': <ManyToManyRel: school.examination>, 'editable': True, 'max_length': None, 'is_relation': True}

"""
