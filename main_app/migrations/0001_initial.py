# Generated by Django 5.1.1 on 2024-09-18 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yelp_id', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('image_url', models.CharField(max_length=100)),
                ('favorited', models.BooleanField(default=False)),
            ],
        ),
    ]