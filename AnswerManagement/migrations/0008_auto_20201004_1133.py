# Generated by Django 3.1.2 on 2020-10-04 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AnswerManagement', '0007_auto_20201004_1111'),
    ]

    operations = [
        migrations.RenameField(
            model_name='examineeanswer',
            old_name='marks',
            new_name='graded',
        ),
        migrations.AddField(
            model_name='examineeanswer',
            name='done_late',
            field=models.BooleanField(default=False),
        ),
    ]