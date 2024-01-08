# Generated by Django 5.0 on 2023-12-29 20:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Storage',
            new_name='Storage_Folder',
        ),
        migrations.CreateModel(
            name='Storage_File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('folder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.storage_folder')),
            ],
        ),
    ]
