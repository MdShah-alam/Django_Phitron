# Generated by Django 4.2.1 on 2023-06-21 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='father_name',
            field=models.CharField(default='Rahim', max_length=15),
        ),
    ]