from django.contrib.auth.models import User
from django.db import models


class Clients(models.Model):
    client_name = models.CharField(max_length=100, verbose_name="Имя клиента")
    project_name = models.CharField(max_length=100, verbose_name="Название проекта")
    city = models.CharField(max_length=100, verbose_name="Город")
    photo = models.CharField(max_length=200, blank=True, null=True, verbose_name="Фото")
    contact = models.CharField(max_length=100, verbose_name="Контакт")
    start_date = models.DateField(verbose_name="Дата начала работы")
    status = models.ForeignKey('ClientsStatus', on_delete=models.DO_NOTHING, db_column='status', verbose_name="Статус")

    def __str__(self):
        return f"{self.client_name} | {self.project_name}"

    class Meta:
        managed = True
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"


class ClientsStatus(models.Model):
    status_name = models.CharField(max_length=50, verbose_name="Название статуса")

    def __str__(self):
        return self.status_name

    class Meta:
        managed = True
        verbose_name = "Статус клиента"
        verbose_name_plural = "Статусы клиентов"


class UsersClients(models.Model):
    users = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name="Пользователь")
    clients = models.ForeignKey(Clients, on_delete=models.DO_NOTHING, verbose_name="Клиент")

    def __str__(self):
        return f"{self.users} | {self.clients}"

    class Meta:
        managed = True
        db_table = 'users_clients'
        verbose_name = "Связь пользователь-клиент"
        verbose_name_plural = "Связи пользователь-клиент"