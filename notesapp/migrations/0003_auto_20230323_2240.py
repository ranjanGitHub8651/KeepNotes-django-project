# Generated by Django 3.2.12 on 2023-03-23 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notesapp', '0002_rename_keepnotes_keepnote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keepnote',
            name='notes',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='keepnote',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]