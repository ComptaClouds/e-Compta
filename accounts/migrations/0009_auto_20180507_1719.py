# Generated by Django 2.0.2 on 2018-05-07 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20180507_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='logo',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
