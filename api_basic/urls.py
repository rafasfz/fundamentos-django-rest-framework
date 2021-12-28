from django.urls import path
from .views import article_list, article_detail, ArticleAPIView, ArticleDetails

urlpatterns = [
    # path('', article_list),
    path('', ArticleAPIView.as_view()),
    # path('<str:pk>/', article_detail)
    path('<str:id>/', ArticleDetails.as_view())
]
