from django.db import models


class EasyReg(models.Model):
    username1 = models.CharField(max_length=50, default='')  # ограниченый размер переменной
    username2 = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.username1


class EasyReg2(models.Model):
    username1 = models.CharField(max_length=50, default='')  # ограниченый размер переменной
    username2 = models.CharField(max_length=50, default='')
    username3 = models.CharField(max_length=50, default='')
    username4 = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.username1


class Pay(models.Model):
    username = models.CharField(max_length=50, default='')  # ограниченый размер переменной
    vk = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.username
