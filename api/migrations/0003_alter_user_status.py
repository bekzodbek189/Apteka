# Generated by Django 4.1.1 on 2022-10-09 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.SmallIntegerField(choices=[(1, 'Director'), (2, 'Omborchi'), (3, 'Sotuvchi'), (4, 'User')], default=4),
        ),
    ]
