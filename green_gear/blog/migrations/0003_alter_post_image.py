# Generated by Django 5.0.4 on 2024-05-05 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_newpostemail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='posts/%Y/', verbose_name='Image'),
        ),
    ]
