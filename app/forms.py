from django import forms


def check_for_m(value):
    if value[0]=='m':
        raise forms.ValidationError('name should not start with m')

def check_for_age(value):
    if value<18:
        raise forms.ValidationError('age should be above 18')       

def check_for_len(value):
    if len(value)<3:
        raise forms.ValidationError('length should be below 5')         


class StudentForm(forms.Form):
    name=forms.CharField(max_length=100,validators=[check_for_m,check_for_len])
    age=forms.IntegerField(validators=[check_for_age])
    email=forms.EmailField(max_length=100)
    reenteremail=forms.EmailField(max_length=100)


    def clean(self):
        e=self.cleaned_data['email']
        r=self.cleaned_data['reenteremail']
        if e!=r :
            raise forms.ValidationError('enter correct mail')
