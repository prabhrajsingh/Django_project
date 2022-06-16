from filecmp import clear_cache
from importlib.resources import contents
from django import forms
from .models import Review #using the class Review in models.py of reviews

class ReviewForm(forms.ModelForm):
    class Meta: #describing the actual model of the form class
        model = Review
        fields = ['title', 'content']


    def clean(self):
        data = self.cleaned_data
        title = data.get('title')

        qs = Review.objects.filter(title__icontains = title)
        # this queryset is the type of queryset that gonna filterdown our entire database for the string (title) coming in here
        # icontains mean that if it contains that then it will actually have some values 

        if (qs.exists()):
            self.add_error("title", f"\"{title}\" exists.") # f is string substitution

        return data

class ReviewFormold(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    # this function is to see the cleaned data only title
    # def clean_title(self):
    #     cleaned_data = self.cleaned_data #dictionary
    #     title = cleaned_data.get('title')

    #     if (title.lower().strip() == title):
    #         raise forms.ValidationError("A title already Exists")

    #     print(cleaned_data)
    #     print("TITLE: ", title)
    #     return title




    # this function is to see all the cleaned data
    def clean(self):
        cleaned_data = self.cleaned_data
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        if (title.lower().strip() == title):
            self.add_error('title', "A title already Exists") # this is for a specific to a field
            #raise forms.ValidationError("A title already Exists") # this is for the entire form
            

        print("ALL DATA :" , cleaned_data)
        return cleaned_data