
from django.urls import path,include
from . import views
urlpatterns = [
    path('signup',views.student_form,name="student_insert"),
    path('<int:id>/',views.student_form,name='student_update'),
    path('delete/<int:id>/', views.student_delete, name='student_delete'), 
    path('list/',views.student_list,name='student_list'),
    path('', views.student_sign_in, name='student_sign_in'),
    path('home/', views.home_view, name='home'),
    path('signup', views.student_signup, name="student_insert"),
    path('choose',views.options_view,name='admin_choose'),
    path('menu',views.menu_view,name='admin_menu'),
    path('about',views.about_view,name='about'),
    path('menu_edit',views.menu_list_view,name='user_menu'),

]
