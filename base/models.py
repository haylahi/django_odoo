import re
from datetime import datetime

from django.contrib.auth.models import AbstractBaseUser
from django.db import models

from .utils import UserProfileManager, CustomFileStorage, compute_float

"""
文件以文件形式保存
    图片返回 base64
    其他返回文件流

基础模块
    company
    partner
    department
    employee
    
    银行账号 支付宝 现金 银行卡 微信
    
    根据self relation fileds 去 操作自己应该关闭的外键
    

"""

CHOICES_SEX = [
    ('MALE', '男'),
    ('FEMALE', '女'),
    ('NULL', '未知'),
]

DEFAULT_SEX = 'NULL'

CHOICES_DEPARTMENT_TYPE = [
    ('NORMAL', '常规'),
    ('SPECIAL', '特殊'),
    ('STORE', '子公司门店'),
    ('OTHER', '其他'),
]

DEFAULT_DEPARTMENT_TYPE = 'NORMAL'

CHOICES_UNIT_TYPE = [
    ('UNIT', '数量单位'),
    ('WEIGHT', '质量'),
    ('TIME', '时间'),
    ('LENGTH', '长度'),
    ('OTHER', '其他')
]

DEFAULT_UNIT_TYPE = 'UNIT'

CHOICES_UNIT_COMPUTE_TYPE = [
    ('STD', '标准'),
    ('RIDE', '大于'),
    ('DIVIDE', '小于'),
]

DEFAULT_UNIT_COMPUTE_TYPE = 'STD'
UNIT_COMPUTE_TYPE_BIGGER = 'RIDE'
UNIT_COMPUTE_TYPE_SMALLER = 'DIVIDE'

CHOICES_TAX_TYPE = [
    ('PERSONAL_INCOME_TAX', '个人所得税'),
    ('INCREMENT_TAX', '增值税'),
    ('OTHER', '其他'),
]

DEFAULT_TAX_TYPE = 'INCREMENT_TAX'

CHOICES_TAX_COMPUTE_TYPE = [
    ('GROUP', '税组'),
    ('FIXED', '固定'),
    ('PERCENT', '百分比'),
]

DEFAULT_TAX_COMPUTE_TYPE = 'PERCENT'

RE_SEQUENCE_MATCHING = re.compile(r'{(.*?)}')

SPECIAL_SEQUENCE_VALUE = {
    'Year': '%Y', 'year': '%y',
    'month': '%m', 'day': '%d',
    'Week': '%a', 'weekday': '%w',
    'h24': '%H', 'min': '%M', 'sec': '%S'
}

CHOICES_PARTNER_TAG_COLOR = [
    ('red', '红色'),
    ('blue', '蓝色'),
    ('green', '绿色'),
    ('yellow', '黄色'),
]

CHOICES_PARTNER_LEVEL = [
    ('A', 'VIP'),
    ('B', '高级'),
    ('C', ''),
    ('D', ''),
    ('E', '普通'),
]


# ----------------------------------------------------------------------------------------------------------------------


class Company(models.Model):
    """公司
            检查 code是否唯一
            不能选择自己的公司
            创建partner
    """

    name = models.CharField('公司名称', max_length=255)
    code = models.CharField('唯一编码', max_length=255)
    create_time = models.DateTimeField('创建时间', default=datetime.now)
    is_active = models.BooleanField(default=True)

    parent_company = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, verbose_name='上级公司', related_name='child_companys')
    default_tax = models.ForeignKey('BaseTax', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='默认税')
    default_currency = models.ForeignKey('Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='默认货币')

    child_dummy_balance = models.CharField('返点资金余额', max_length=255, default='0')
    child_cash_balance = models.CharField('实际资金余额', max_length=255, default='0')
    dummy_discount = models.CharField('默认返点比例(%)', max_length=255, default='40')

    def __str__(self):
        return '{}({})'.format(self.name, self.code)

    def my_child_companies(self):
        return self.child_companys.all().filter(is_active=True)

    def self_partner(self):
        p = self.my_partner.all().filter(is_active=True)
        if p and len(p) == 1:
            return p
        else:
            raise ValueError("ERROR: company's partner error")

    class Meta:
        ordering = ['-name']
        db_table = 'base_company'


class PartnerTag(models.Model):
    """检查同一个用户下标签的名字是否相同"""
    name = models.CharField('名称', max_length=255)
    color = models.CharField('颜色', max_length=255, choices=CHOICES_PARTNER_TAG_COLOR, default='green')
    user = models.ForeignKey('UserProfile', on_delete=models.CASCADE, verbose_name='所属用户', related_name='partner_tags')
    create_time = models.DateTimeField('创建时间', default=datetime.now)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-name']
        db_table = 'base_partner_tag'


class Partner(models.Model):
    """合作伙伴
    如果有公司 则不显示有公司的合作伙伴

    """
    company = models.ForeignKey('Company', on_delete=models.CASCADE, null=True, blank=True, verbose_name='所在公司', related_name='my_partner')
    name = models.CharField('合作伙伴', max_length=255)
    code = models.CharField('唯一编码', max_length=255)
    desc = models.CharField('详细描述', max_length=255, default='')
    create_time = models.DateTimeField('创建时间', default=datetime.now)
    is_active = models.BooleanField(default=True)

    tags = models.ManyToManyField('PartnerTag', blank=True, verbose_name='标签')
    partner_level = models.CharField('客户等级', max_length=255, )

    # 根据创建的场景去判断
    is_customer = models.BooleanField('是否是客户', default=False)
    is_supplier = models.BooleanField('是否是供应商', default=False)

    # 详细信息 检查唯一性
    uniform_social_credit_code = models.CharField('企业统一社会信用代码(税号)', max_length=255, default='')
    legal_person = models.CharField('公司法人', max_length=255, default='')
    register_date = models.DateField('成立时间', default=datetime.now)

    logo = models.ImageField('公司Logo', upload_to='company_logo/', storage=CustomFileStorage(), default='default_logo.png')
    web_site = models.URLField('合作伙伴网址', max_length=255, default='')
    contact_info = models.CharField('联系方式', max_length=255, default='')
    email = models.EmailField('合作伙伴邮箱', max_length=255, default='')

    # 地址信息
    country = models.ForeignKey('BaseCountry', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='所在国家')
    province = models.ForeignKey('BaseProvince', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='省份')
    city = models.ForeignKey('BaseCity', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='城市')
    address = models.CharField('详细地址', max_length=255, default='')

    # TODO 仓库位置 指定一个虚拟虚拟位置 银行账户 客户类型

    def __str__(self):
        return '{}({})'.format(self.name, self.code)

    class Meta:
        ordering = ['-name']
        db_table = 'base_partner'


class Department(models.Model):
    """部门"""
    company = models.ForeignKey('Company', on_delete=models.CASCADE, verbose_name='所在公司')
    name = models.CharField('部门名称', max_length=255)
    code = models.CharField('唯一编码', max_length=255)
    desc = models.CharField('详细描述', max_length=255, default='')
    logo = models.ImageField('部门Logo', upload_to='department_logo/', storage=CustomFileStorage(), default='default_logo.png')
    is_active = models.BooleanField(default=True)

    department_type = models.CharField('部门类型', max_length=255, choices=CHOICES_DEPARTMENT_TYPE, default=DEFAULT_DEPARTMENT_TYPE)
    parent_department = models.ForeignKey('Department', on_delete=models.CASCADE, null=True, blank=True, verbose_name='上级部门', related_name='child_departments')

    def __str__(self):
        return '{}({})'.format(self.name, self.code)

    def my_child_departments(self):
        return self.child_departments.all().filter(is_active=True)

    def department_manager(self):
        employees = self.employees.all().filter(is_active=True, is_department_manager=True)
        if employees and len(employees) == 1:
            return employees[0]
        else:
            return None

    class Meta:
        ordering = ['-name']
        db_table = 'base_department'


class JobClassification(models.Model):
    """职位"""
    name = models.CharField('职位名称', max_length=255)
    code = models.CharField('唯一编码', max_length=255)
    desc = models.CharField('详细描述', max_length=255, default='')
    requirement = models.CharField('技能要求', max_length=255, default='')
    pub_date = models.DateField('发布日期', default=datetime.now)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-name']
        db_table = 'base_job'


class Employee(models.Model):
    """员工"""
    company = models.ForeignKey('Company', on_delete=models.CASCADE, verbose_name='所在公司')
    department = models.ForeignKey('Department', on_delete=models.CASCADE, verbose_name='所属部门', related_name='employees')
    user = models.ForeignKey('UserProfile', on_delete=models.CASCADE, verbose_name='uid')
    job = models.ForeignKey('JobClassification', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='职位')
    is_department_manager = models.BooleanField(default=False, verbose_name='部门经理')

    # from user_info real_name
    name = models.CharField('员工名称', max_length=255)
    code = models.CharField('工号', max_length=255)

    induction_date = models.DateField('入职日期', default=datetime.now)
    work_address = models.CharField('工作地址', max_length=255, default='')
    work_email = models.CharField('工作邮箱', max_length=255, default='')
    work_contact = models.CharField('工作联系方式', max_length=255, default='')

    is_active = models.BooleanField(default=True)

    # TODO 工作记录 工资记录  职位发展 银行账号表

    def __str__(self):
        return self.name

    def my_department_manager(self):
        return self.department.department_manager()

    class Meta:
        ordering = ['-name']
        db_table = 'base_employee'


class UserGroup(models.Model):
    """用户组"""
    name = models.CharField('用户组名', max_length=255)
    code = models.CharField('唯一编码', max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, verbose_name='上级用户组', related_name='child_groups')
    users = models.ManyToManyField('UserProfile', blank=True)
    create_time = models.DateTimeField('创建时间', default=datetime.now)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def my_child_groups(self):
        return self.child_groups.all().filter(is_active=True)

    class Meta:
        ordering = ['-name']
        db_table = 'base_user_group'


class UserProfile(AbstractBaseUser):
    """
    创建superuser 不验证 其他的验证公司
    创建用户
    """
    company = models.ForeignKey('Company', on_delete=models.CASCADE, null=True, blank=True, verbose_name='所在公司')

    email = models.EmailField(verbose_name='登录邮箱', max_length=255, unique=True)
    create_time = models.DateTimeField('创建时间', default=datetime.now)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserProfileManager()
    USERNAME_FIELD = 'email'

    def has_perm(self, perm, obj=None):
        print(self, perm, obj)
        return True

    def has_module_perms(self, app_label):
        print(self, app_label)
        return True

    @property
    def is_staff(self):
        return True

    def __str__(self):
        return self.email

    class Meta:
        ordering = ['-create_time']
        db_table = 'base_user'


class UserInfo(models.Model):
    user = models.ForeignKey('UserProfile', on_delete=models.CASCADE, verbose_name='uid')

    avatar = models.ImageField('头像', upload_to='user_avatar/', storage=CustomFileStorage(), default='default_logo.png')
    real_name = models.CharField('姓名', max_length=255, default='')
    nickname = models.CharField('昵称', max_length=255, default='')
    person_phone = models.CharField('个人联系号码', max_length=255, default='')
    sex = models.CharField('性别', max_length=255, choices=CHOICES_SEX, default=DEFAULT_SEX)
    country = models.ForeignKey('BaseCountry', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='国籍')
    id_number = models.CharField('身份证', max_length=255, default='')
    marital_status = models.CharField('婚姻状态', choices=[('NO', '未婚'), ('YES', '已婚')], default='NO', max_length=255)
    home_address = models.CharField('家庭住址', max_length=255, default='')
    birth_day = models.DateField('生日', default=datetime.now)
    graduate_school = models.CharField('毕业院校', max_length=255, default='')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.real_name

    class Meta:
        ordering = ['-real_name']
        db_table = 'base_user_info'


class BaseTax(models.Model):
    name = models.CharField('税', max_length=255)
    code = models.CharField('唯一编码', max_length=255)

    tax_type = models.CharField('税类型', max_length=255, choices=CHOICES_TAX_TYPE, default=DEFAULT_TAX_TYPE)
    compute_type = models.CharField('计算方法', max_length=255, choices=CHOICES_TAX_COMPUTE_TYPE, default=DEFAULT_TAX_COMPUTE_TYPE)
    rounding = models.CharField('精度', max_length=255, default='0.00')

    #  代表多个数据 保存时检查 计算方法 和 factor
    factor = models.CharField('百分比', max_length=255, default='13')
    is_active = models.BooleanField(default=True)

    def compute_untax(self, total: str):
        if self.compute_type == DEFAULT_TAX_COMPUTE_TYPE:
            _num = float(total) / (1 + float(self.factor) / 100)
            return compute_float(str(_num), self.rounding)
        else:
            raise ValueError('[ERROR] 暂不支持的操作')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-name']
        db_table = 'base_tax'


class CurrencyRate(models.Model):
    currency = models.ForeignKey('Currency', on_delete=models.CASCADE, verbose_name='所属货币', related_name='rates')
    rate = models.CharField('比率', max_length=255, default='100')
    create_time = models.DateTimeField('创建时间', default=datetime.now)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.rate

    class Meta:
        get_latest_by = 'create_time'
        ordering = ['create_time']
        db_table = 'base_currency_rate'


class Currency(models.Model):
    name = models.CharField('货币', max_length=255)
    code = models.CharField('唯一编码', max_length=255)
    symbol = models.CharField('符号', max_length=255)
    rounding = models.CharField('精度', max_length=255, default='0.00')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return '{}({})'.format(self.name, self.code)

    class Meta:
        ordering = ['-name']
        db_table = 'base_currency'

    def compute_standard_total(self, total: str):
        rate = self.rates.all().last().rate
        _num = float(total) / 100 * float(rate)
        return compute_float(str(_num), self.rounding)


class BaseUnit(models.Model):
    name = models.CharField('单位', max_length=255)
    code = models.CharField('唯一编码', max_length=255)
    unit_type = models.CharField('单位类别', max_length=255, choices=CHOICES_UNIT_TYPE, default=DEFAULT_UNIT_TYPE)
    factor = models.CharField('比例', max_length=255, default='1')
    rounding = models.CharField('精度', max_length=255, default='0.00')
    compute_type = models.CharField('计算方式', max_length=255, choices=CHOICES_UNIT_COMPUTE_TYPE, default=DEFAULT_UNIT_COMPUTE_TYPE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        if self.code:
            return '{}({})'.format(self.name, self.code)
        return self.name

    def convert2standard(self, number: str) -> str:
        try:
            float(number)
            float(self.rounding)
        except:
            raise ValueError('[ERROR] convert str to float error')
        if self.compute_type == DEFAULT_UNIT_COMPUTE_TYPE:
            return compute_float(number, self.rounding)

        elif self.compute_type == UNIT_COMPUTE_TYPE_BIGGER:
            _num = float(number) * float(self.factor)
            return compute_float(str(_num), self.rounding)

        elif self.compute_type == UNIT_COMPUTE_TYPE_SMALLER:
            _num = float(number) / float(self.factor)
            return compute_float(str(_num), self.rounding)

    class Meta:
        ordering = ['-unit_type', '-name']
        db_table = 'base_unit'


# ----------------------------------------------------------------------------------------------------------------------


class BaseCountry(models.Model):
    name = models.CharField('国家', max_length=255)
    short_name = models.CharField('简称(英文)', max_length=255)
    area_code = models.CharField('国家区号', max_length=255)
    national_flag = models.ImageField('国旗图标', upload_to='country_image/', storage=CustomFileStorage(), default='default_logo.png')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        db_table = 'base_country'


class BaseProvince(models.Model):
    country = models.ForeignKey('BaseCountry', on_delete=models.CASCADE, verbose_name='所在国家')
    name = models.CharField('省', max_length=255)
    short_name = models.CharField('简称', max_length=255)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-name']
        db_table = 'base_province'


class BaseCity(models.Model):
    """
    电话区号 车牌号
    """
    province = models.ForeignKey('BaseProvince', on_delete=models.CASCADE, verbose_name='所在省份')
    name = models.CharField('城市', max_length=255)
    area_code = models.CharField('城市区号', max_length=255)
    car_number = models.CharField('车牌号首字母', max_length=255)
    is_provincial_capital = models.BooleanField('省会城市', default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-province', '-name']
        db_table = 'base_city'


class BaseSequence(models.Model):
    """
    序列
    """
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='所属公司')
    name = models.CharField('名称', max_length=255)
    code = models.CharField('命名代号(适用模型)', max_length=255, unique=True)
    prefix = models.CharField('前缀', max_length=255)
    suffix = models.CharField('后缀', max_length=255, default='')
    padding = models.PositiveIntegerField('填充长度', default=4)
    increment = models.PositiveIntegerField('步长', default=1)
    next_number = models.PositiveIntegerField('下一个号码', default=1)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-name']
        db_table = 'base_sequence'

    def generate_next_code(self):
        _prefix = self.prefix
        _suffix = self.suffix
        _padding = self.padding
        _cur_number = self.next_number
        _increment = self.increment
        # 计算序列
        _prefix = self.replace_value(_prefix)
        if _suffix:
            _suffix = self.replace_value(_suffix)
        _grow_padding = False
        _max_num = int(str(9) * _padding)
        if _cur_number + _increment > _max_num:
            _grow_padding = True
        _ret = '{prefix}{num:0>{padding}d}'.format(prefix=_prefix, num=_cur_number, padding=_padding)
        if self.suffix:
            _ret = '{prefix}{num:0>{padding}d}{suffix}'.format(prefix=_prefix, num=_cur_number, padding=_padding, suffix=_suffix)
        _cur_number = _cur_number + _increment
        if _grow_padding:
            _padding = _padding + 1
            self.padding = _padding
        self.next_number = _cur_number
        self.save()
        return _ret

    @classmethod
    def generate_next_code_by_name(cls, code: str):
        o = cls.objects.filter(is_active=True, code=code)[0]
        return o.generate_next_code()

    @staticmethod
    def replace_value(val: str):
        _val = val
        _current_time = datetime.now()
        _to_match = RE_SEQUENCE_MATCHING.findall(_val)
        if len(_to_match) != 0:
            _d = {}
            for m in _to_match:
                _d[m] = _current_time.strftime(SPECIAL_SEQUENCE_VALUE.get(m))
            return _val.format(**_d)
        return _val

    @staticmethod
    def check_format_value(val: str):
        from .utils import match_parentheses
        _b = match_parentheses(val)
        if _b:
            _to_match = RE_SEQUENCE_MATCHING.findall(val)
            if len(_to_match) == 0:
                return True
            else:
                tag = True
                for m in _to_match:
                    if m == '':
                        tag = False
                    if m not in SPECIAL_SEQUENCE_VALUE.keys():
                        tag = False
                return tag
        else:
            return _b
