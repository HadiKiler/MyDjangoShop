# Generated by Django 4.2.2 on 2023-06-26 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0010_alter_likeitem_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likeitem',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post', to='items.item'),
        ),
    ]
