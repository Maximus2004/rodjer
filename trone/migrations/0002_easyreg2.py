# Generated by Django 3.0.6 on 2020-05-28 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trone', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EasyReg2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
