from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name="index"),
    path('category/<slug:category>/', views.post_list, name="category"),
    path('<int:year>/<int:month>/<int:day>/<slug>/', views.post_detail, name="Detail_Plan"),
    #path('', views.PostListView.as_view(), name='index'),

]
