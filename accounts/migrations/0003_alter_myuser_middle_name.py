# Generated by Django 4.1.1 on 2022-10-08 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_myuser_age_alter_myuser_middle_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='middle_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]