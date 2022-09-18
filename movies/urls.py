from django.urls import path

# from . views import MoviesListView
from  . import views

app_name = 'movies'
app_name='userprofiles'

urlpatterns = [
    path('', views.home, name="home"),
    # path('', MoviesListView.as_view(), name='home'),
    # path('<slug:slug>', MovieDetailView.as_view(), name='moviedetail'),
    path('movieDetail/<str:pk>/', views.movieDetail, name="movieDetail"),
    path('moviesinthisgenre/<slug:slug>/', views.movies_in_genre, name='movies_in_genre'),
    path('search_items',views.search_items,name="search_items"),
    path('moviespl/<str:pk>/', views.moviespl, name="moviespla"),
    path('myprofile/',views.userprofile,name="userprofile"),


    path('tvseries/',views.tvseries,name="tv_series"),

    path('season_in_series/<str:pk>/', views.season_in_series, name='season'),
    path('episodes_in_season/<str:pk>/', views.episodes_in_season, name='episodes'),
    path('episode_detail/<str:pk>/', views.episode_detail, name='episodedetail'),
    path('choose_subscription_plan/', views.choosesubscriptionplan, name='choosesubscriptionplan'),

    path('checkout/<int:plan_id>/',views.checkout,name="checkout_plan"),
    
    path('checkoutsession/<str:plan_id>/',views.checkoutsession,name="check_sessi"),


    path('paymentsuccess/',views.success,name="success"),
    path('paymentcanceled/',views.cancel,name="cancel"),


    


    

]