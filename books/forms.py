from .models import Books
from django import forms

class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        exclude = ["created_by"]
