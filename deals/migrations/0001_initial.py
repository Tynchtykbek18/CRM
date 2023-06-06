# Generated by Django 4.2.1 on 2023-06-06 08:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0005_alter_customuser_date_joined'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('about', models.TextField(max_length=500, verbose_name='о сделке')),
                ('status', models.CharField(choices=[('новый', 'Новый'), ('в процессе', 'В процессе'), ('выполнен', 'Выполнен')], max_length=20)),
                ('amount', models.DecimalField(decimal_places=3, max_digits=8, verbose_name='сумма сделки')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client', to='accounts.client')),
                ('responsible', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='custom_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
