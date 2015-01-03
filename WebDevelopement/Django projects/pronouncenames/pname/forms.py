from django import forms
from django.forms.fields import DateField, ChoiceField, MultipleChoiceField


pos_choices = ['Proper Noun','Noun', 'Verb','Adjective','Pronoun','Others']

class WordForm(forms.Form):
        name = forms.CharField(label = 'Word')
	phomene = forms.CharField(label = 'Phonemic Breakup')
	audiofile = forms.FileField(label = 'Upload file',required=False,initial = 'None')
	pos = forms.CharField(label = 'Part Of speech',help_text = 'Eg: noun,pronoun ect',required=False)
	origin = forms.CharField(label = 'Origin',required=False)
	f_l_name = forms.CharField(label = 'First/Last Name',required=False)
	gender = forms.CharField(label = 'Gender',required=False)
	meaning = forms.CharField(label = 'Meaning',required=False)

class RequestWordForm(forms.Form):
       name = forms.CharField(label = 'Word')
