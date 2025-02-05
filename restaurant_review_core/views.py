from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from restaurant_review_core.models import Restaurant, Review
from restaurant_review_core.serializers import (
    RestaurantSerializer,
    ReviewSerializer,
)
from restaurant_review_core.permissions import IsOwnerAdminOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import F


class RestaurantListCreateAPIView(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    filter_backends = [OrderingFilter, SearchFilter]
    search_fields = ["name"]
    ordering_fields = ["total_score"]
    ordering = "-total_score"  # - for descending oder


class RestaurantRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class ReviewListCreateAPIView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["restaurant", "author"]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        review = serializer.save(author=self.request.user)

        # Update the total score of the restaurant
        restaurant = review.restaurant
        restaurant.total_score = F("total_score") + review.score
        restaurant.save()


class ReviewRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsOwnerAdminOrReadOnly]

    def perform_destroy(self, instance):
        instance.delete()

        # Update the total score of the restaurant
        restaurant = instance.restaurant
        restaurant.total_score = F("total_score") - instance.score
        restaurant.save()

    def perform_update(self, serializer):
        oldScore = self.get_object().score

        newReview = serializer.save()
        newScore, restaurant = newReview.score, newReview.restaurant
        restaurant.total_score = F("total_score") - oldScore + newScore
        restaurant.save()
