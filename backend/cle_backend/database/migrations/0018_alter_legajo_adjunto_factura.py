# Generated by Django 4.2.7 on 2024-02-28 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0017_alter_recepcion_estado_recepcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='legajo',
            name='adjunto_factura',
            field=models.FileField(default=True, upload_to='facturas/'),
        ),
    ]
