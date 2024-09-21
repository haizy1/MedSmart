# Generated by Django 5.0.4 on 2024-05-05 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentic', '0002_finalis'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='uploaded_images/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
