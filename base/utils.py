# author: Liberty
# date: 2019/4/22 20:31

import logging

from django.contrib.auth.models import BaseUserManager

__logger__ = logging.getLogger(__name__)


class MyUserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('Users must have an username')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(username=username, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user


def check_float(val: str) -> bool:
    try:
        float(val)
        return True
    except ValueError as e:
        __logger__.error(e)
        return False
