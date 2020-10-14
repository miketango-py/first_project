#from -- import
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#functions
def homepage (request):#start homepage
  #local variables
  #code
  return render(request, 'welcome.html')
#end homepage
def menu (request):#start menu
  #local variables
  #code
  return render(request, 'menu.html')
#end menu
def who_we_are(request):#start who_we_are
  #local variables
  #code
  return render(request, 'who_we_are.html')
#end who_we_are
def variables(request):#start variables
  #local variables
  #code
  context = {'var_one':'Something','var_two':'Nothing','var_three':'Void'}
  return render(request, 'variables.html', context)
#end variables
def index(request):#start index
  #local variables
  #code
  return render(request, 'index.html')
#end index