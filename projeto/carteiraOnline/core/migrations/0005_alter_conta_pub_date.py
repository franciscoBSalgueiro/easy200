# Generated by Django 4.0.3 on 2022-03-12 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_conta_email_text_conta_localidade_text_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conta',
            name='pub_date',
            field=models.CharField(max_length=69420),
        ),
    ]
