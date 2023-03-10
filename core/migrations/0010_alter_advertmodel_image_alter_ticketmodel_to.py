# Generated by Django 4.1.2 on 2023-01-18 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_ticketmodel_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='ticketmodel',
            name='to',
            field=models.CharField(choices=[('bosaso to garowe', 'bosaaso to gaowe'), ('non', 'non'), ('bosaso to lascano', 'bosaso to lascano'), ('bosaso to qardho', 'bosaaso to qardho'), ('bosaso to galkacyo', 'bosaso to galkacyo')], default='non', max_length=255, verbose_name='toto'),
        ),
    ]
