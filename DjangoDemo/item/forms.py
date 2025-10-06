from django import forms

from .models import Item

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['category', 'name', 'description', 'price', 'image']
        widgets = {
            'category': forms.Select(attrs={
                'placeholder': 'Select a category',
                'class': 'w-full p-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-teal-500 focus:border-teal-500 transition'
            }),
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter item name',
                'class': 'w-full p-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-teal-500 focus:border-teal-500 transition'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Write a short description...',
                'rows': 4,
                'class': 'w-full p-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-teal-500 focus:border-teal-500 transition'
            }),
            'price': forms.NumberInput(attrs={
                'placeholder': 'Enter price (e.g. 299)',
                'class': 'w-full p-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-teal-500 focus:border-teal-500 transition'
            }),
            'image': forms.FileInput(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-xl bg-white focus:ring-2 focus:ring-teal-500 focus:border-teal-500 transition'
            }),
        }

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description', 'price', 'image', 'is_sold']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter item name',
                'class': 'w-full p-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-teal-500 focus:border-teal-500 transition'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Write a short description...',
                'rows': 4,
                'class': 'w-full p-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-teal-500 focus:border-teal-500 transition'
            }),
            'price': forms.NumberInput(attrs={
                'placeholder': 'Enter price (e.g. 299)',
                'class': 'w-full p-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-teal-500 focus:border-teal-500 transition'
            }),
            'image': forms.FileInput(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-xl bg-white focus:ring-2 focus:ring-teal-500 focus:border-teal-500 transition'
            }),
        }


