#import
from django.shortcuts import render
import datetime
# Create your views here.
#functions
def if_one(request):#start example_if
  #local variables
  #code
  #https://www.decodejava.com/django-template-if-tag.htm
  #Creating a dictionary of key-value pairs
  dic = { 
    'var1' : 200,
    'var2' : 200,
    'var3' : 300 
  }
  #Calling the render() method to render the request from es_if.html page by using the dictionary, dic
  return render(request, "if_one.html", dic)
#end example_if
def if_else(request):#start if_else
  #local variables
  #code
  #https://www.decodejava.com/django-template-if-else-tag.htm
    dic = { 
      'var1' : 'admin',
      'var2' : 'admin',
      'var3' : 600 
    }
    return render(request, "if_else.html", dic)
#end if_else
def if_elif(request):#start if_elif
  #local variables
  #code
  dic = { 
    'var1' : 100,
    'var2' : 100.0,
    'var3' : 100.50,
    'str1' : 'Hello',
    'str2' : 'hello',
    'str3' : "Hello",
    'list1': [1, datetime.date(2019,7,16), 'Make your life productive!'],
    'list2': [2, datetime.date(2019,7,16), 'Do not give up!']
  }
  return render(request, "if_elif.html", dic)
#end if_elif
def for_one(request):#start for_one
  #local variables
  #code
  #https://www.decodejava.com/django-template-for-tag.htm
    dic = { 'list1': [1, datetime.date(2019,7,16), 'Do not give up!'],'list2': [1, datetime.date(2019,7,16), 'Do not give up!'] }
    return render(request, "for_one.html", dic)
#end for_one