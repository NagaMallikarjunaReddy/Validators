from django import forms

def Check(value):
    if 'a'<= value <='z':
        raise forms.ValidationError('name should not start with lower')


class Studentform(forms.Form):
    name=forms.CharField(max_length=100,validators=[Check])
    age=forms.IntegerField()
    email=forms.EmailField()
    re_enter_mail=forms.EmailField()
    botcatcher=forms.CharField(max_length=100,required=False,widget=forms.HiddenInput)


    def clean(self):
        e=self.cleaned_data['email']
        r=self.cleaned_data['re_enter_mail']
        if e!=r:
            raise forms.ValidationError('email is not matched')
    def clean_botcatcher(self):
        bot=self.cleaned_data['botcatcher']
        if len(bot)>0:
            raise forms.ValidationError('bot is catched')
            