# Generated by Django 5.2.4 on 2025-07-10 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_userprofile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='sex',
            field=models.CharField(blank=True, choices=[('', ''), ('M', 'Male'), ('F', 'Female')], default='', max_length=1, null=True),
        ),
    ]
