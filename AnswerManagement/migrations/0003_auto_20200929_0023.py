# Generated by Django 3.1.1 on 2020-09-28 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ExamManagement', '0003_exam_exam_question'),
        ('AnswerManagement', '0002_examineemcqanswer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='examineecustomanswer',
            name='custom_question',
        ),
        migrations.RemoveField(
            model_name='examineecustomanswer',
            name='submitted_answer',
        ),
        migrations.AddField(
            model_name='examineecustomanswer',
            name='answer',
            field=models.FileField(default='exam/answers/sample.pdf', upload_to='exam/answers/'),
        ),
        migrations.AddField(
            model_name='examineecustomanswer',
            name='exam',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ExamManagement.exam'),
        ),
    ]
