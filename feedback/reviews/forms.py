from django import forms


class Reviews(forms.Form):
    user_name=forms.CharField(label="Enter your name",max_length=5,error_messages={
        "required":"gayrat et enter your name",
        "max_length":"10 charecters"
    })
    comment=forms.CharField(
        label="Feedback", max_length=200, widget=forms.Textarea)
    rating=forms.IntegerField(label="Rating",max_value=10,min_value=1)
