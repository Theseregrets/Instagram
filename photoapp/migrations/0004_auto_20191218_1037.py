# Generated by Django 2.2.8 on 2019-12-18 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photoapp', '0003_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FileField(null=True, upload_to='images/'),
        ),
    ]
