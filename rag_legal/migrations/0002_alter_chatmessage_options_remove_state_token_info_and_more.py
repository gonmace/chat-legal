# Generated by Django 5.1.7 on 2025-04-06 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rag_legal', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chatmessage',
            options={'ordering': ['-timestamp']},
        ),
        migrations.RemoveField(
            model_name='state',
            name='token_info',
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='cost',
            field=models.FloatField(default=0),
        ),
    ]
