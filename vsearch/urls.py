from django.urls import path
from vsearch import views
urlpatterns = [
    path('', views.home_search, name="home-search-btn"),
    path('userQuery/', views.user_second_home_query, name="result-btn"),
    path('business/', views.business_query, name="business-btn"),
    path("sports/", views.sports_query, name="sports-btn"),
    path('education/', views.education_query, name="education-btn"),
    path('agriculture/', views.agriculture_query, name="agriculture-btn"),
]
