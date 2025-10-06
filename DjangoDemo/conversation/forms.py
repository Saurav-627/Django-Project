from django import forms

from .models import ConversationMessage

class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model = ConversationMessage
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'placeholder': 'Write a message...',
                'rows': 4,
                'class': 'w-full p-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-teal-500 focus:border-teal-500 transition'
            })
        }