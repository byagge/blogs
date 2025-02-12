# Generated by Django 5.1.1 on 2024-09-17 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('image', models.ImageField(upload_to='blogs/', verbose_name='Image')),
                ('create_at', models.DateField(auto_now_add=True, verbose_name='Create at')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
    ]
