from django import forms

class ToDoForm(forms.Form):
    task = forms.CharField(max_length=50,
            widget=forms.TextInput(
                attrs={'class':'form-control', 'placeholder':'Enter a task to do', 'aria-label':'Todo', 'aria-describedby':'add-btn'}
            ))
