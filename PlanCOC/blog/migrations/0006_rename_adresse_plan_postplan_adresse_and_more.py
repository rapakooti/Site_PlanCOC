# Generated by Django 4.0.4 on 2022-05-26 20:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_postplan_type_village_remove_postplan_usage_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postplan',
            old_name='adresse_plan',
            new_name='adresse',
        ),
        migrations.RenameField(
            model_name='postplan',
            old_name='image_vivi',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='postplan',
            old_name='nb_dl',
            new_name='nb_affichage',
        ),
        migrations.RenameField(
            model_name='postplan',
            old_name='level',
            new_name='niveau',
        ),
        migrations.AlterField(
            model_name='postplan',
            name='publication',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]