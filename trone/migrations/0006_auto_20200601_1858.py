# Generated by Django 3.0.6 on 2020-06-01 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trone', '0005_auto_20200529_1309'),
    ]

    operations = [
        migrations.CreateModel(
            name='PraksReg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username1', models.CharField(default='', max_length=50)),
                ('vk1', models.CharField(default='', max_length=50)),
                ('username2', models.CharField(default='', max_length=50)),
                ('vk2', models.CharField(default='', max_length=50)),
                ('username3', models.CharField(default='', max_length=50)),
                ('vk3', models.CharField(default='', max_length=50)),
                ('username4', models.CharField(default='', max_length=50)),
                ('vk4', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.RenameModel(
            old_name='EasyReg',
            new_name='DuoEasy',
        ),
        migrations.DeleteModel(
            name='EasyReg2',
        ),
    ]
