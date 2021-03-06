from django.urls import path

from members.apis import AuthTokenAPIView, CreateUserAPIView, LogoutAPIView

urlpatterns = [
    path('create/', CreateUserAPIView.as_view()),
    path('login/', AuthTokenAPIView.as_view()),
    path('logout/', LogoutAPIView.as_view()),
]