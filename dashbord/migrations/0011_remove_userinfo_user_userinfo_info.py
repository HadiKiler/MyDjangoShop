# Generated by Django 4.2.2 on 2023-06-25 06:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashbord', '0010_rename_info_userinfo_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='user',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='info',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='info', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
