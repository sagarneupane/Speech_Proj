# Generated by Django 4.1.1 on 2022-10-08 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='middle_name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]