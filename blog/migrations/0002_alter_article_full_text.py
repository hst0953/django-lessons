# Generated by Django 4.0.4 on 2022-05-13 17:44

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='full_text',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
