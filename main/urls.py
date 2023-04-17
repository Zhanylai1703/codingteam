from django.contrib import admin
from django.urls import path, include

from menu.views import FoodListView

api_v1 = [
    path('food/', FoodListView.as_view())
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include(api_v1))
]
