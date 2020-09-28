from django import forms
from .models import Exam, MCQQuestion


class AddExamForm(forms.Form):
    exam_title = forms.CharField(label='Exam Title')
    exam_code = forms.IntegerField(label='Exam Code')
    exam_marks = forms.IntegerField(label='Exam Marks')
    # exam_datetime = forms.DateTimeField()
    exam_duration = forms.IntegerField(label='Exam Duration')
    exam_question = forms.FileField(label='Exam Questions')

    class Meta:
        model = Exam
        fields = [
            'exam_title',
            'exam_code',
            'exam_datetime',
            'exam_marks',
            'exam_duration',
            'exam_question'
        ]

    def clean(self):
        return super(AddExamForm, self).clean()


class AddMCQquestionform(forms.ModelForm):
    class Meta:
        model = MCQQuestion
        fields = ('question_text', 'option1', 'option2', 'option3', 'option4', 'ques_marks', 'question')


class AddQuestionForm(forms.Form):
    # qus_id = forms.IntegerField()
    # exam_id = forms.IntegerField()
    qus_marks = forms.IntegerField()
    time_limit = forms.IntegerField()

    class Meta:
        model = Exam
        fields = [
            'qus_id',
            'exam_id',
            'qus_marks',
            'time_limit',
        ]

    def clean(self):
        return super(AddQuestionForm, self).clean()


class AddCustomQuestionForm(forms.Form):
    # qus_id=forms.IntegerField()
    qus_text = forms.CharField()

    class Meta:
        model = Exam
        fields = [
            'qus_id',
            'qus_text',
        ]

    def clean(self):
        return super(AddCustomQuestionForm, self).clean()
