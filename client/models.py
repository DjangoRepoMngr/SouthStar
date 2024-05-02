from django.db import models
from utils.general_model import GeneralModel
from django.contrib.auth.models import User

Active = 1
Deactive = -1
StatusChoices = (
    (Active, "فعال"),
    (Deactive, "غیر فعال"),
)

class CustomUser(User):
    class Meta:
        proxy = True  # This ensures that you are creating a proxy model

    def __str__(self):
        return self.get_full_name() if self.get_full_name() else self.username

class route(GeneralModel):

    name = models.CharField(max_length=200, verbose_name='نام مسیر')
    code = models.IntegerField('کد مسیر ',)
    visitor = models.ForeignKey( CustomUser ,on_delete=models.PROTECT, null=True, verbose_name='فروشنده')

    class Meta:
        verbose_name_plural = "مسیر"
        verbose_name = "مسیر"

    def __str__(self):
        return str(self.name)


class client(GeneralModel):

    name = models.CharField(max_length=200, verbose_name='نام مشتری')
    phone_number = models.CharField(verbose_name='شماره همراه', max_length=11, null=True, unique=True)
    address = models.TextField(verbose_name='آدرس', default='آدرس')
    client_status = models.IntegerField('وضعیت مشتری', default=1,choices=StatusChoices)
    tablo = models.CharField(max_length=200, null=True, blank= True, verbose_name='تابلو')
    description = models.TextField(verbose_name='توضیحات', blank= True)
    route = models.ForeignKey("route",on_delete=models.PROTECT, null=True, verbose_name='مسیر')
    is_changed_location = models.BooleanField(default=False, verbose_name='آیا تغییر مسیر داده است')
    is_black_list = models.BooleanField(default=False, verbose_name='آیا لیست سیاه است')
    is_dishonest = models.BooleanField(default=False, verbose_name='آیا بد حساب است')
    national_code = models.CharField(verbose_name='کد ملی', max_length=10, null=True, blank= True, unique=True)
    economy_code = models.CharField(verbose_name='کد اقتصادی', max_length=200, null=True, blank= True, unique=True)

    class Meta:
        verbose_name_plural = "مشتری"
        verbose_name = "مشتری"

    def __str__(self):
        return str(self.name)


class client_buy(GeneralModel):

    count_products = models.IntegerField('تعداد کارتن',)
    client = models.ForeignKey("client",on_delete=models.PROTECT, null=True, verbose_name='مشتری')
    visitor = models.ForeignKey(CustomUser ,on_delete=models.PROTECT, null=True, verbose_name='ویزیتور')

    class Meta:
        verbose_name_plural = "خرید مشتری"
        verbose_name = "حرید مشتری"

    def __str__(self):
        return str(self.client)

