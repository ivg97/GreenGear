# Generated by Django 5.0.4 on 2024-05-05 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='communicationservice',
            name='full_name',
            field=models.CharField(default='Test name', max_length=255, verbose_name='Full Name'),
            preserve_default=False,
        ),
    ]
