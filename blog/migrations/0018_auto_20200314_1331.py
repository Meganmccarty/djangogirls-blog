# Generated by Django 2.2.10 on 2020-03-14 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20200314_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
