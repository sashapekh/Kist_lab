from django import forms


class Query2Form(forms.Form):
    # форма для поиска информации по определенному студенту
    surname = forms.CharField(label='surname', max_length=30, required=True)
    name = forms.CharField(label='name', max_length=30, required=True)
