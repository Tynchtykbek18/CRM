from django.db import models
from accounts.models import Client, CustomUser


class Deal(models.Model):
    STATUS = (('новый', 'Новый'),
              ('в процессе', 'В процессе'),
              ('выполнен', 'Выполнен'))
    title = models.CharField(max_length=30)
    about = models.TextField(max_length=500, verbose_name='о сделке')
    status = models.CharField(max_length=20, choices=STATUS)
    owner = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='client')
    amount = models.DecimalField(max_digits=8, decimal_places=3, verbose_name='сумма сделки')
    responsible = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='custom_user')
    consumption = models.CharField(max_length=30, verbose_name='расходы')

    def __str__(self):
        return self.title