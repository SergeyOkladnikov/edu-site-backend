# Generated by Django 4.1.6 on 2023-02-08 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0007_remove_quiz_name_question_order_alter_question_quiz'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='order',
            field=models.IntegerField(),
        ),
    ]
