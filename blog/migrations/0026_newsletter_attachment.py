# Generated by Django 2.2.11 on 2020-03-26 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_auto_20200325_1357'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsletter',
            name='attachment',
            field=models.FileField(default='', upload_to='email_attachments/'),
        ),
    ]