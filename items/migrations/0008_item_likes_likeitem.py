# Generated by Django 4.2.2 on 2023-06-26 13:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('items', '0007_alter_category_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='likeItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post', to='items.item')),
                ('relate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relate', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
