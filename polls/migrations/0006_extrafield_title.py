# Generated by Django 3.0.3 on 2020-06-19 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_extrafield'),
    ]

    operations = [
        migrations.AddField(
            model_name='extrafield',
            name='title',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
