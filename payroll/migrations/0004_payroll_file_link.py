# Generated by Django 4.1.4 on 2023-01-03 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0003_payroll_payroll_filename'),
    ]

    operations = [
        migrations.AddField(
            model_name='payroll',
            name='file_link',
            field=models.CharField(blank=True, max_length=150, null=True, unique=True),
        ),
    ]
