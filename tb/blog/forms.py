from django import forms

class Singupform(forms.ModelForm):
    username = forms.CharField(label='signup', max_length=100,error_messages={'requested':'請填寫你的用戶名','max_length':'最多輸入15個字','min_length':'最少輸入3個字'},
    





    	)