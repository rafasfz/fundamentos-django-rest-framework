from django.urls import path
from .views import article_list, article_detail, ArticleAPIView, ArticleDetails, GenericAPIView

urlpatterns = [
    # path('', article_list),
    path('generic_article/', GenericAPIView.as_view()),
    path('generic_article/<uuid:id>/', GenericAPIView.as_view()),
    path('', ArticleAPIView.as_view()),
    # path('<str:pk>/', article_detail)
    path('<uuid:id>/', ArticleDetails.as_view()),
]
