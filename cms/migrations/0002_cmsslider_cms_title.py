# Generated by Django 4.1.3 on 2022-11-12 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cmsslider',
            name='cms_title',
            field=models.CharField(default=1, max_length=100, verbose_name='Заголовок'),
            preserve_default=False,
        ),
    ]
