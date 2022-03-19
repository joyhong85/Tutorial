from django import forms


def validator_min_length(value):
    if len(value) < 3:
        raise forms.ValidationError('최소 글자는 3자 입니다.')


class MyForm(forms.Form):
    name = forms.CharField(max_length=10)
    hobby = forms.CharField(help_text="취미를 입력해주세요.", validators=[validator_min_length])

