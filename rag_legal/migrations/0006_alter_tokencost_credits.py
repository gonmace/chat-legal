# Generated by Django 5.1.7 on 2025-04-07 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rag_legal', '0005_alter_chatmessage_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tokencost',
            name='credits',
            field=models.FloatField(default=0.5),
        ),
    ]
