# Generated by Django 2.0.2 on 2018-05-07 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20180507_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='logo',
            field=models.ImageField(blank=True, max_length=170, upload_to=''),
        ),
    ]