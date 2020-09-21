from django import forms
from .models import Exam,MCQQuestion


class AddExamForm(forms.Form):
    exam_title = forms.CharField()
    exam_code = forms.IntegerField()
    exam_marks = forms.IntegerField()
    #exam_datetime = forms.DateTimeField()
    exam_duration = forms.IntegerField()

    class Meta:
        model = Exam
        fields = [
            'exam_title',
            'exam_code',
            'exam_datetime',
            'exam_marks',
            'exam_duration',
        ]

    def clean(self):
        return super(AddExamForm, self).clean()



class AddMCQquestionform(forms.ModelForm):
    class Meta:
        model = MCQQuestion
        fields = ('question_text','option1','option2','option3','option4','ques_marks','question')
