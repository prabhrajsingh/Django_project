from django.shortcuts import render, redirect

from .models import Review #since we are already in reviews folder so we can relatively remove and simple keep .models
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
from django.http import Http404

 

# Create your views here.

def review_search_view(request):    
    #print(request.GET)
    query_dict = request.GET # this is a dictionary
    # query = query_dict.get("q") # as this was the term in the base.html------ <input type = 'text' name = 'q' />
    #so now this is our actual query we can use this query to find a review object
    try:
        query = int( query_dict.get("q"))
    except:
        query = None

    review_obj = None

    if query is not None:
        review_obj = Review.objects.get(id=query)

    context = {
                "object" : review_obj
              }
    return render(request, "reviews/search.html", context = context) 
    # here we may not need to mention reviews/ because of the folder it is stored in
                                                                      

#csrf is a security measure that make sure that nobody is just sending data to you 
#but if you wanted to recieve data from another source there is a secure way to do that 
#but in our case we are working on a webpage we should actually be able to handle this.
#one of them is the {% csrf_token %}
#In the template, there is a {% csrf_token %} template tag inside each POST form that targets an internal URL

#there is a decorator @csrf_exempt which allow you to circumvent that
#we dont want to circumvent that , that is a security risk used in "REST API"

@login_required
def review_create_view(request):

    form = ReviewForm(request.POST or None) # this is only request.get coming through here but passing the parameter will allow us in rendering the data in a better way
    context = {
                "form" : form
              }

    if (form.is_valid()):
        review_obj = form.save()
        context['form'] = ReviewForm()
        return redirect(review_obj.get_absolute_url())
        # context['object'] = review_obj
        # context['created'] = True

    return render(request, "reviews/create.html", context = context)

# def review_create_view(request):
#     #print(request.POST)
#     form = ReviewForm() # this is only request.get coming through here
    
#     #print(dir(form))

#     context = {
#         "form" : form
#     }

#     if ( request.method == "POST"):
#         # new instance of ReviewForm but keeping it as same name variable
#         form = ReviewForm(request.POST) #passing all of the uncleaned data and having it be a part of this form instance
#         context['form'] = form

#         if (form.is_valid()):
#             title = form.cleaned_data.get("title")
#             content = form.cleaned_data.get("content")
#             print(title, content)
#             review_obj = Review.objects.create(title = title, content= content) 
#             context['object'] = review_obj
#             context['created'] = True

#     return render(request, "reviews/create.html", context = context)


def review_detail_view(request, slug=None):
    review_obj = None
    if (slug is not None):
        try:
            review_obj = Review.objects.get(slug=slug)

        except Review.DoesNotExist:
            raise Http404

        except Review.MultipleObjectsReturned:
            review_obj = Review.objects.filter(slug=slug).first()

        except:
            raise Http404
            

    context = {
                "object" : review_obj
              }


    return render(request, "reviews/detail.html", context = context)