# Generated by Django 4.2.7 on 2024-02-23 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0007_alter_dataservicio_adjunto_solicitudservicio'),
    ]

    operations = [
        migrations.RenameField(
            model_name='informearea',
            old_name='adjunto_informeServicio',
            new_name='adjunto_informeArea',
        ),
    ]