# Generated by Django 3.0.6 on 2020-06-02 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trone', '0009_auto_20200602_1028'),
    ]

    operations = [
        migrations.AddField(
            model_name='praksreg',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
    ]