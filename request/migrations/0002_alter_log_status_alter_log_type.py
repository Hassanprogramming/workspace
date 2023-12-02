# Generated by Django 4.2 on 2023-12-02 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='status',
            field=models.CharField(choices=[('D', 'Danger'), ('S', 'Safe')], max_length=1),
        ),
        migrations.AlterField(
            model_name='log',
            name='type',
            field=models.CharField(choices=[('Person', 'Person'), ('Face', 'Face'), ('Bag', 'Bag')], max_length=10),
        ),
    ]
