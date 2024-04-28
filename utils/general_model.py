from django.db import models
from . import persian_date_time


Active = 1
Deactive = -1
StatusChoices = (
    (Active, "فعال"),
    (Deactive, "غیر فعال"),
)

class GeneralModel(models.Model):

    status = models.IntegerField('وضعیت', default=1,choices=StatusChoices)
    create_date = models.IntegerField('تاریخ ثبت', default=persian_date_time.get_persian_date_normalized())

    class Meta:
        abstract = True
