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


class Analysis(models.Model):
    client = models.ForeignKey(Clients, on_delete=models.DO_NOTHING, verbose_name="Клиент")
    analysis_name = models.CharField(max_length=100, verbose_name="Название проекта анализа")
    analysis_type = models.ForeignKey('AnalysisType', on_delete=models.DO_NOTHING,
                                      db_column='analysis_type', verbose_name="Тип анализа")
    create_date = models.DateField(verbose_name="Дата создания")

    def __str__(self):
        return self.analysis_name

    class Meta:
        managed = True
        verbose_name = "Анализ проекта"
        verbose_name_plural = "Анализы проектов"


class AnalysisType(models.Model):
    analysis_name = models.CharField(max_length=50, verbose_name="Название типа анализа")

    def __str__(self):
        return self.analysis_name

    class Meta:
        managed = True
        verbose_name = "Тип анализа"
        verbose_name_plural = "Типы анализов"


class FullVideos(models.Model):
    title = models.CharField(max_length=300, verbose_name="Название видео")
    link = models.URLField(max_length=200, verbose_name="Ссылка на видео")
    preview_path = models.URLField(max_length=200, verbose_name="Ссылка на превью")
    views = models.IntegerField(verbose_name="Просмотры")
    subscribers = models.IntegerField(verbose_name="Подписчики")
    duration = models.CharField(max_length=10, verbose_name="Длительность видео (HH:MM:SS)")
    views_subs = models.FloatField(verbose_name="Просмотры/подписчики")
    publish_date = models.DateField(verbose_name="Дата публикации")
    product = models.CharField(max_length=200, blank=True, null=True, verbose_name="Продукт")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        managed = True
        verbose_name = "Полноформатное видео"
        verbose_name_plural = "Полноформатные видео"


class AnalysisFullVideos(models.Model):
    users = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name="Пользователь")
    clients = models.ForeignKey(Clients, on_delete=models.DO_NOTHING, verbose_name="Клиент")

    def __str__(self):
        return f"{self.users} | {self.clients}"

    class Meta:
        managed = True
        db_table = 'users_clients'
        verbose_name = "Связь пользователь-клиент"
        verbose_name_plural = "Связи пользователь-клиент"