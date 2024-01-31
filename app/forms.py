from django import forms
from app.models import *



class TopicForm(forms.ModelForm):
    class Meta():
        model=Topic
        fields='__all__'

class WebpageForm(forms.ModelForm):
    class Meta():
        model=Webpage
        fields='__all__'
        #labels={'topic_name':'TN','name':'N'} 
        #widgets={'topic_name':forms.Textarea()} 

class AccessRecordForm(forms.ModelForm):
    class Meta():
        model=AccessRecord
        fields='__all__'              