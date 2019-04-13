# author: Liberty
# date: 2019/4/13 14:11

from django.contrib.auth.base_user import BaseUserManager


class UserProfileManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('请输入正确的邮箱。。。')
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        # 创建一个用户信息
        user.create_user_info()
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user
