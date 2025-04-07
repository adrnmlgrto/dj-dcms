from django.urls import path
from django.contrib.auth.views import logout_then_login
from .views import CustomLoginView

urlpatterns = [
    path(
        route='login/',
        view=CustomLoginView.as_view(),
        name='login'
    ),
    path(
        route='logout/',
        view=logout_then_login,
        name='logout'
    ),
    # path(
    #     route='signup/',
    #     view=SignupView.as_view(),
    #     name='signup'
    # )
]
