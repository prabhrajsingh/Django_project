from sqlite3 import Timestamp
import random
from ssl import RAND_add
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save

# https://docs.djangoproject.com/en/4.0/ref/models/fields/

# Create your models here.
class Review(models.Model):
    
    title = models.CharField(max_length=100)

    slug = models.SlugField(unique = True, blank= True, null= True)  

    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add = True) 
    # auto_now is like whenever the model is saved the auto_now is going to be set
    # whenever the model is added the auto_now_add is goint to be set
    # a timestamp make sense whenever its added so we will remove the auto_now one
    updated = models.DateTimeField(auto_now = True)
    # these two (timestamp and updated) feature help in tracking the interaction between user and the data

    def save(self, *args, **kwargs):
        #obj = Article.object.get(id=1)
        #set = something
        #obj.save()

        # if (self.slug is None):
        #     self.slug = slugify(self.title)
        super().save(*args, **kwargs)

def slugify_instance_title(instance, save = False, new_slug = None):
    
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)

    Klass=instance.__class__ # this is another way to access the class of the instance and using Klass we can apply it to different models as well

    qs = Klass.objects.filter(slug = slug).exclude(id = instance.id) #replacing reviews with Klass
    
    if qs.exists():
        rand_int = random.randint(300_000, 500_000)
        slug = f"{slug}-{rand_int}"
        return slugify_instance_title(instance, save = save, new_slug = slug) #recursion for new slug that doesnt exist

    instance.slug = slug

    if save:
        instance.save()

    return instance
    
def review_pre_save(sender, instance, *args, **kwargs):
    if (instance.slug is None):
        slugify_instance_title(instance, save=False)
    
pre_save.connect(review_pre_save, sender = Review) 


def review_post_save(sender, instance, created, *args, **kwargs):
    if created:
        #instance.slug = " tempslug"
        slugify_instance_title(instance, save=True)
        

post_save.connect(review_post_save, sender = Review)             