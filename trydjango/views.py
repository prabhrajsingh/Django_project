""" 
To render HTML web pages
"""
from lib2to3.refactor import get_all_fix_names
import random 
from django.http import HttpResponse
from urllib import response

from reviews.models import Review
from django.template.loader import render_to_string
#from django.template.loader import get_template


def home_view(request, id=None, *args, **kwargs):
    """ 
    to take in a request (Django sends the request)
    and
    return HTML as a response (We pick to return the response)
    """
    # name = "PRABHRAJ" # HARD CODED
    random_number = random.randint(1,3) #Psuedo Random

    review_obj = Review.objects.get(id=random_number)
    
    #it is a query set that behave like a list because instead having individual objects it can do much more advance things
    review_queryset = Review.objects.all()

    # H1_STRING = f""" <h1> {review_obj.title} <p><h4>( ID : {review_obj.id})</p></h4> </h1>"""
    # P_STRING = f""" <p> {review_obj.content}</p>"""

    # HTML_STRING = H1_STRING + P_STRING


    #(USE DJANGO TEMPLATES FOR CUSTOMIZATION )

    context = {
        "object_list": review_queryset,
        "title":  review_obj.title, 
        "content": review_obj.content, 
        "id": review_obj.id
    }
    
    # HTML_STRING = """ <h1> {title}
    #                  <p><h4>( ID : {id})</p></h4> </h1 <p> {content}</p>""".format(**context)

    # tmp = get_template("home_view.html") 
    # tmp_string = tmp.render(context = context)
    # render_to_string does the same thing but in one step
    # get_template would be useful if we have to use same template again and again but with different context 

    HTML_STRING = render_to_string("home_view.html", context = context)

    return HttpResponse(HTML_STRING)


