#from -- import
from django.shortcuts import render
from django.http import HttpResponse
from .models import Article, Journalist
#code
def home(request):#start home function
    #variables
    articles = Article.objects.all()
    journalists = Journalist.objects.all()
    #code
    context = {"Articles": articles, "Journalists": journalists}
    print(context)
    return render(request, "homepage_news.html", context)
#end home function