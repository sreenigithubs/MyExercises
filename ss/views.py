from django.shortcuts import render,redirect
from django.http import HttpResponse
import datetime
#http://127.0.0.1:8000/articles/
def hello(request):
   today = datetime.datetime.now().date()
   daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
   return render(request, "home.html", {"today" : today, "days_of_week" : daysOfWeek})
 
#http://127.0.0.1:8000/articles/1/    
def viewArticle(request, articleId):
   """ A view that display an article based on his ID"""
   text = "Displaying article Number : %s" %articleId
   return HttpResponse(text)

#http://127.0.0.1:8000/articles/2019/09/    
def viewArticles(request, year, month):
   text = "Displaying articles of : %s/%s"%(year, month)
   return HttpResponse(text)
#http://127.0.0.1:8000/articles2/
def hello2(request):
    return redirect("https://www.google.com")

#http://127.0.0.1:8000/articles2/1/
def viewArticle2(request, articleId):
   """ A view that display an article based on his ID"""
   text = "Displaying article Number : %s" %articleId
   return redirect(viewArticles, year = "2045", month = "02")