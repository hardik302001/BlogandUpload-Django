# Generated by Django 3.0.7 on 2021-03-17 04:52

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20210316_2217'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='thumb',
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]