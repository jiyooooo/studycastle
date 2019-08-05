from django.forms import ModelForm
from django import forms
from . models import Review
from django.utils.translation import gettext_lazy as _


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'content', 'username', 'star']
        labels = {
            'title': _('제목'),
            'content': _('내용'),
        }
        help_text = {
            'title': _('제목을 입력해주세요.'),
            'content': _('내용을 입력해주세요.'),
        }
        error_message = {
            'title': {
                'max_length': _('제목은 50자 이하로 작성해주세요.')
            },
            'content': {
                'max_length': _('내용은 500자 이하로 작성해주세요.')
            },
        }
        widgets = {
            'username': forms.HiddenInput(),
            'content': forms.Textarea()
        }




