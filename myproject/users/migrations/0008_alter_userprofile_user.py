# Generated by Django 5.0.6 on 2024-06-14 09:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_rename_user1_user_rename_userprofiles_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='users.user'),
        ),
    ]