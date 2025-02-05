from django.urls import path

from restaurant_review_core.views import (
    RestaurantListCreateAPIView,
    RestaurantRetrieveUpdateDestroyAPIView,
    ReviewListCreateAPIView,
    ReviewRetrieveUpdateDestroyAPIView,
)

app_name = "restaurant_review_core"
urlpatterns = [
    path("restaurant/", RestaurantListCreateAPIView.as_view(), name="list_restaurant"),
    path(
        "restaurant/<int:pk>/",
        RestaurantRetrieveUpdateDestroyAPIView.as_view(),
        name="retrieve_update_delete_restaurant",
    ),
    path("review/", ReviewListCreateAPIView.as_view(), name="review"),
    path(
        "review/<int:pk>/",
        ReviewRetrieveUpdateDestroyAPIView.as_view(),
        name="retrieve_update_delete_review",
    ),
]
