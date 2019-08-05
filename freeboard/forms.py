from django.forms import ModelForm
from django import forms
from . models import Freeboard, Comment, FreeboardLikepoint
from django.utils.translation import gettext_lazy as _


class FreeboardForm(ModelForm):
    class Meta:
        model = Freeboard
        fields = ['title', 'content', 'username']
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


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['freeboard', 'content', 'username']
        labels = {
            'content': _('내용')
        }
        help_text = {
            'content': _('내용을 입력해주세요.')
        }
        error_message = {
            'content': {
                'max_length': _('댓글은 300자 이하로 작성해주세요.')
            }
        }
        widgets = {
            
            'freeboard': forms.HiddenInput(),
            'username': forms.HiddenInput()
        }


class FreeboardLikepointForm(ModelForm):
    class Meta:
        model = FreeboardLikepoint
        fields = ['username', 'freeboard', 'like_point']