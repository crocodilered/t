from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.TextField(verbose_name='Код')),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'Верный код'), (2, 'Ошибочный код'), (3, 'Ошибка сервиса')], null=True, verbose_name='Статус')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Время проверки')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
