# Generated by Django 3.0.6 on 2020-06-02 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trone', '0008_auto_20200602_0905'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='praksreg',
            name='vk2',
        ),
        migrations.RemoveField(
            model_name='praksreg',
            name='vk3',
        ),
        migrations.RemoveField(
            model_name='praksreg',
            name='vk4',
        ),
    ]
