# Generated by Django 3.0.6 on 2020-05-29 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trone', '0004_auto_20200529_1251'),
    ]

    operations = [
        migrations.RenameField(
            model_name='easyreg',
            old_name='username',
            new_name='username1',
        ),
        migrations.RenameField(
            model_name='easyreg2',
            old_name='username',
            new_name='username1',
        ),
        migrations.AddField(
            model_name='easyreg',
            name='username2',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='easyreg2',
            name='username2',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='easyreg2',
            name='username3',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='easyreg2',
            name='username4',
            field=models.CharField(default='', max_length=50),
        ),
    ]
