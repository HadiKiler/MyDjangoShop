# Generated by Django 4.2.2 on 2023-06-25 06:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashbord', '0009_rename_rubika_userinfo_instagram'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfo',
            old_name='info',
            new_name='user',
        ),
    ]