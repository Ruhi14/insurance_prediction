from django import forms

class FeedbackForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class':'w-full bg-white rounded border border-gray-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out',
        'placeholder':'enter your email'
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'w-full bg-white rounded border border-gray-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 h-32 text-base outline-none text-gray-700 py-1 px-3 resize-none leading-6 transition-colors duration-200 ease-in-out',
        'placeholder':'enter your message...'
    }))
    