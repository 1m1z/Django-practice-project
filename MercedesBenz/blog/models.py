from django.db import models

class Blog(models.Model):
    class Meta:
        verbose_name="پست ها"
        verbose_name_plural="پست ها"

    BlogPic=models.ImageField(upload_to="media/blog" ,verbose_name="عکس پست")
    BlogName=models.CharField(max_length=32 ,verbose_name="اسم پست")
    BlogDescription=models.TextField(verbose_name="توضیحات مختصر")

    def __str__(self):
        return self.BlogName 