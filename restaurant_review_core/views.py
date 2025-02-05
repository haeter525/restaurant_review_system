from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from drf_spectacular.utils import (
    extend_schema_view,
    extend_schema,
    OpenApiParameter,
    OpenApiExample,
)
from restaurant_review_core.models import Restaurant, Review
from restaurant_review_core.serializers import (
    RestaurantSerializer,
    ReviewSerializer,
)
from restaurant_review_core.permissions import IsOwnerAdminOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import F


@extend_schema_view(
    get=extend_schema(
        summary="List restaurants",
        description="List restaurants in the system. You can filter restaurants by name. By default, the list is ordered by total score.",
        parameters=[
            OpenApiParameter(
                "ordering",
                str,
                default="-total_score",
                description="Which field to use when ordering the results.",
            )
        ],
        auth=[],  # Require no authentication
    ),
    post=extend_schema(
        summary="Create a new restaurant",
        description="Create a new restaurant in the system. Only admin users have permission to create restaurants.",
    ),
)
class RestaurantListCreateAPIView(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    filter_backends = [OrderingFilter, SearchFilter]
    search_fields = ["name"]
    ordering_fields = ["total_score"]
    ordering = "-total_score"  # - for descending oder


@extend_schema_view(
    get=extend_schema(
        summary="Get details of a specific restaurant",
        description="Get details of a specific restaurant, including id, name, address, and score.",
        auth=[],  # Require no authentication
    ),
    put=extend_schema(
        summary="Update a specific restaurant",
        description="Update a specific restaurant. Only admin users have permission to update restaurants.",
    ),
    patch=extend_schema(
        summary="Partially Update a specific restaurant",
        description="Partially Update a specific restaurant. Only admin users have permission to update restaurants.",
    ),
    delete=extend_schema(
        summary="Delete a specific restaurant",
        description="Delete a specific restaurant. Only admin users have permission to delete restaurants.",
    ),
)
class RestaurantRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


@extend_schema_view(
    get=extend_schema(
        summary="List reviews",
        description="List reviews in the system. You can filter reviews by author or restaurant.",
        auth=[],  # Require no authentication
    ),
    post=extend_schema(
        summary="Create a new review",
        description="Create a new review. Only login users have permission to create review.",
    ),
)
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


@extend_schema_view(
    get=extend_schema(
        summary="Get details of a specific review",
        description="Get details of a specific review, including id, author, restaurant, text, and score.",
    ),
    put=extend_schema(
        summary="Update a specific review",
        description="Update a specific review. Only authors or admin users have permission to update reviews.",
    ),
    patch=extend_schema(
        summary="Partially Update a specific review",
        description="Partially update a specific review. Only authors or admin users have permission to update reviews.",
    ),
    delete=extend_schema(
        summary="Delete a specific review",
        description="Delete a specific review. Only authors or admin users have permission to delete reviews.",
    ),
)
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
