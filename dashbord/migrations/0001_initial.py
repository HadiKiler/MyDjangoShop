# Generated by Django 4.2.2 on 2023-06-23 22:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('github', models.CharField(max_length=100, null=True)),
                ('telegram', models.CharField(max_length=100, null=True)),
                ('website', models.CharField(max_length=100, null=True)),
                ('rubika', models.CharField(max_length=100, null=True)),
                ('relate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relate', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
