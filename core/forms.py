from django import forms


class WalletForm(forms.Form):
    recovery_phrase = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 5
    }))
