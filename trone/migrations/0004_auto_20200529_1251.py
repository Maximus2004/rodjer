# Generated by Django 3.0.6 on 2020-05-29 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trone', '0003_auto_20200529_1149'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=50)),
                ('vk', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='easyreg',
            name='vk',
        ),
        migrations.RemoveField(
            model_name='easyreg2',
            name='vk',
        ),
    ]