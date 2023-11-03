from django import forms
from .models import Article
# 파이썬 코드로 html을 만들기 위함함
class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = '__all__'