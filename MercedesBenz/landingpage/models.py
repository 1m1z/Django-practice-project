
from django.db import models

# Create your models here.


class CartModel (models.Model):

    class Meta:
        verbose_name=" ماشین ها"
        verbose_name_plural="ماشین ها"  

    CartImage=models.ImageField(upload_to="media/",verbose_name="عکس ماشین")
    CartTitle=models.CharField(max_length=100,verbose_name="اسم ماشین")
    CartDescription=models.CharField(max_length=250,verbose_name="توضیحات ماشین")
    CartBtnTitle=models.CharField(max_length=50,verbose_name="فروشی یا اجاره ایی؟")


    def __str__(self):
        return self.CartTitle



class MotortModel (models.Model):
    class Meta:
        verbose_name=" موتور ها"
        verbose_name_plural="موتور ها"  

    MotorImage=models.ImageField(upload_to="media/",verbose_name="عکس موتور")
    MotorTitle=models.CharField(max_length=100,verbose_name="مدل موتور")
    MotorDescription=models.TextField(verbose_name="توضیحات موتور")
    # MotorBtnTitle=models.CharField(max_length=50,verbose_name=" فروشی یا اجاره ایی؟")

    # Sold=1
    # Rent=2
    # STATUS_CHOICES=(("Sold","فروشی"),("Rent","اجاره ایی"))

    # status_chioces = (
    # (1,  _Feature('فروشی')),
    # (2, _Feature('اجاره ایی')),
    # )


    CHOICES = (
        (1 , 'پلنگ'),
        (2 , 'گربه'),
    )
    BuyOption = models.IntegerField(choices=CHOICES ,default=1)


    def __str__(self):
        return self.MotorTitle