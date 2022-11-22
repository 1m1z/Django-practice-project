# Generated by Django 4.1.3 on 2022-11-22 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0004_alter_cartmodel_cartimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='MotortModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MotorImage', models.ImageField(upload_to='media/', verbose_name='عکس موتور')),
                ('MotorTitle', models.CharField(max_length=100, verbose_name='مدل موتور')),
                ('MotorDescription', models.TextField(verbose_name='توضیحات موتور')),
                ('MotorBtnTitle', models.CharField(max_length=50, verbose_name=' فروشی یا اجاره ایی؟')),
            ],
            options={
                'verbose_name': ' موتور ها',
                'verbose_name_plural': 'موتور ها',
            },
        ),
    ]
