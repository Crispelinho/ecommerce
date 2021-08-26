# Generated by Django 3.2.6 on 2021-08-26 02:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shippingmanagement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('asunto', models.CharField(max_length=200)),
                ('mensaje', models.CharField(max_length=2000)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'get_latest_by': 'id',
            },
        ),
    ]