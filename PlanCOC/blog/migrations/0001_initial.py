# Generated by Django 4.0.4 on 2022-05-15 21:53

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PostPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.CharField(max_length=200)),
                ('adresse_plan', models.CharField(max_length=200)),
                ('image_vivi', models.CharField(max_length=200)),
                ('usage', models.CharField(max_length=200)),
                ('nb_dl', models.CharField(max_length=200)),
                ('level', models.CharField(max_length=200)),
                ('type_village', models.CharField(choices=[('hdv', 'HDV'), ('mdo', 'MDO'), ('capitale', 'CAPITALE')], default='hdv', max_length=10)),
                ('status', models.CharField(choices=[('attente', 'Attente'), ('publié', 'Publié')], default='attente', max_length=15)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('publication', models.DateTimeField(default=datetime.datetime(2022, 5, 15, 21, 53, 48, 425611, tzinfo=utc))),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posted', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
