# Generated by Django 4.2.6 on 2023-10-19 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hashuser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10),
        ),
    ]
