from django.urls import path

from authenticate.apis import CheckUserAPIView

urlpatterns = [
    path('', CheckUserAPIView.as_view()),
]