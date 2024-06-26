# Generated by Django 4.0 on 2024-03-23 05:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fathername', models.CharField(max_length=100)),
                ('mothername', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=100)),
                ('pincode', models.CharField(max_length=6)),
                ('mobilenumber', models.CharField(max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]
