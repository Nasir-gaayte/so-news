# Generated by Django 4.1.2 on 2023-01-18 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_alter_ticketmodel_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketmodel',
            name='to',
            field=models.CharField(choices=[('bosaso to lascano', 'bosaso to lascano'), ('non', 'non'), ('bosaso to qardho', 'bosaaso to qardho'), ('bosaso to galkacyo', 'bosaso to galkacyo'), ('bosaso to garowe', 'bosaaso to gaowe')], default='non', max_length=255, verbose_name='toto'),
        ),
    ]