from django.urls import path
from . import views


urlpatterns = [
    
    path('',views.about,name="about"),
    
    path('login/',views.loginPage,name="login"),
    path('logout/',views.logoutUser,name="logout"),
    path('register/',views.registerPage,name="register"),
    
    path('home',views.home,name="home"),
    path('room_page/<str:pk>/',views.room,name="room"),
    path('profile/<str:pk>/',views.userProfile,name="user-profile"),
    path('privatechat/<str:pk>/',views.privatechat,name="privatechat"),

    
    path('create_room/',views.createRoom,name="create-room"),
    path('update_room/<str:pk>/',views.updateRoom,name="update-room"),
    path('delete_room/<str:pk>/',views.deleteRoom,name="delete-room"),
    path('delete_message/<str:pk>/',views.deleteMessage,name="delete-message"),
    
    path('update_user/',views.updateUser,name="update-user"),
    
    path('topics/',views.topicsPage,name="topics"),
    path('activity/',views.activityPage,name="activity"),
    
    
    
    path('checkout/<str:pk>/',views.checkout,name="checkout"),
    
]
