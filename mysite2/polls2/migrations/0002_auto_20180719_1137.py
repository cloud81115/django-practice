# Generated by Django 2.0.5 on 2018-07-19 03:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls2', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='question_text',
            new_name='question',
        ),
    ]
