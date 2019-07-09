from celery import Celery
from . import config

import os
# 为celery设置环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'meiduo_mall.settings.dev')

# app = Celery('task',
#              broker='redis://192.168.203.151:6379/0',
#              backend='redis://192.168.203.151:6379/0')
# app.autodiscover_tasks(['meiduo_celery.express'], related_name='tasks', force=True)


app = Celery('task')
app.config_from_object(config)