from django.urls import path


from ss import views 

urlpatterns = [
 path('articles/',views.hello,name='hello'),  
 path('articles/<int:articleId>/', views.viewArticle, name = 'viewArticle'),
 path('articles/<int:year>/<int:month>/', views.viewArticles, name = 'viewArticles'),
 path('articles2/',views.hello2,name='hello2'),  
 path('articles2/<int:articleId>/',views.viewArticle2,name='viewArticle2'),  



]

