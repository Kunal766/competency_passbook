# Generated by Django 4.0.5 on 2022-07-04 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('templateManager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='template',
            name='template_templateData',
            field=models.TextField(blank=True, null=True),
        ),
    ]