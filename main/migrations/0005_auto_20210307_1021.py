# Generated by Django 3.1.4 on 2021-03-07 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210222_0828'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='descriprion',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='fingerprint',
            name='fingerprint',
        ),
    ]