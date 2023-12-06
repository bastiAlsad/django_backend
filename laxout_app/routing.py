from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home" ),
    path("home/", views.home, name="home"),
    path("create-user/", views.create_user, name="create-user"),
    path("home/create-user/", views.create_user, name="create-user"),
    path("home/delete-user/<int:id>/", views.delete_user, name= "delete-user"),
    path("delete-user/<int:id>/", views.delete_user, name= "delete-user"),
    path("home/edit-user/<int:id>", views.edit_user, name="edit-user"),
    path("edit-user/<int:id>", views.edit_user, name="edit-user"),
    path("home/edit-user/edit-user-workout/", views.edit_user_workout, name="edit-user"),
    path("edit-user/edit-user-workout/", views.edit_user_workout, name="edit-user"),
    path("home/edit-user/delete-user-workout/", views.delete_user_workout, name="edit-user"),
    path("edit-user/delete-user-workout/", views.delete_user_workout, name="edit-user"),
    #path("magic/", views.execute_data_transfer),
    #path("home/magic/", views.execute_data_transfer),
    path("home/edit-user/add-exercises/<int:id>/", views.add_exercises, name="add-exercises"),
    path("edit-user/add-exercises/<int:id>/", views.add_exercises, name="add-exercises"),
    path("home/edit-user/add-exercises/<int:first>/<int:second>/", views.add_exercises, name="add-exercises"),
    path("edit-user/add-exercises/<int:first>/<int:second>/", views.add_exercises, name="add-exercises"),
    path("laxout/show-login-code/<str:logincode>/", views.display_login_code, name="show-login-code"),
    path("restful-api/get-user-uid/<str:access_code>/",views.get_user_uid, name= "get-user-uid"),
]