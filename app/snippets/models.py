from django.db import models


class Snippet(models.Model):
    STATUS_SUCCESS = 1
    STATUS_FAILURE = 2
    STATUS_ERROR = 3

    STATUS_ENUM = [
        (STATUS_SUCCESS, 'Верный код'),
        (STATUS_FAILURE, 'Ошибочный код'),
        (STATUS_ERROR, 'Ошибка сервиса'),
    ]

    code = models.TextField('Код')
    status = models.PositiveSmallIntegerField('Статус', choices=STATUS_ENUM, null=True)
    created = models.DateTimeField('Время проверки', auto_now_add=True, db_index=True)

    def __str__(self):
        status_str = '-'

        if self.status == self.STATUS_SUCCESS:
            status_str = 'S'
        elif self.status == self.STATUS_FAILURE:
            status_str = 'F'
        elif self.status == self.STATUS_ERROR:
            status_str = 'E'

        return f'{self.pk} - {self.created} - {status_str}'

    class Meta:
        ordering = ['-id']
