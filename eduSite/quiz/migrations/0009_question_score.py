# Generated by Django 4.1.6 on 2023-02-10 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0008_alter_question_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='score',
            field=models.IntegerField(default=1),
        ),
    ]
