# author: Liberty
# date: 2019/4/27 14:40

from celery import task


# noinspection PyCallingNonCallable
@task
def tasks_create_file(job_name, **kwargs):
    print('start celery tasks {}'.format(job_name))
    path = kwargs.get('path')
    content = kwargs.get('content')
    with open(path, 'wb') as f:
        f.write(content)
    return 'ok'
