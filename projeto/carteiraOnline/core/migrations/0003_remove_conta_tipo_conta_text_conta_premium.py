# Generated by Django 4.0.3 on 2022-03-12 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_conta_delete_choice_delete_question'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conta',
            name='tipo_conta_text',
        ),
        migrations.AddField(
            model_name='conta',
            name='premium',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]