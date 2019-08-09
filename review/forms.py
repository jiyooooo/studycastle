from django.forms import ModelForm
from django import forms
from . models import Review
from django.utils.translation import gettext_lazy as _


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'content', 'username', 'volume', 'runningtime', 'fun', 'total']

        labels = {
            'title': _('제목'),
            'content': _('내용'),
            'volume': _('전체 강좌의 수는 어떻나요?'),
            'runningtime': _('강의 시간은 적당했나요?'),
            'fun': _('강의가 얼마나 몰입됐나요?'),
            'total': _('친구에게 얼마나 추천해주고 싶나요?'),
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

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.fields['volume'].widget.attrs['class'] = 'form-control'
        self.fields['runningtime'].widget.attrs['class'] = 'form-control'
        self.fields['fun'].widget.attrs['class'] = 'form-control'
        self.fields['total'].widget.attrs['class'] = 'form-control'



