# Generated by Django 4.1.3 on 2022-12-05 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BlogPic', models.ImageField(upload_to='media/blog', verbose_name='عکس پست')),
                ('BlogName', models.CharField(max_length=32, verbose_name='اسم پست')),
                ('BlogDescription', models.TextField(verbose_name='توضیحات مختصر')),
            ],
            options={
                'verbose_name': 'پست ها',
                'verbose_name_plural': 'پست ها',
            },
        ),
    ]
