from rest_framework import serializers
from restaurant_review_core.models import Restaurant, Review
from drf_spectacular.utils import extend_schema_serializer, OpenApiExample


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            name="Restaurant Example For Request",
            value={
                "name": "First Restaurant",
                "address": "First Address",
                "total_score": 0,
            },
            request_only=True,
        ),
        OpenApiExample(
            name="Restaurant Example For Response",
            value={
                "id": 1,
                "name": "First Restaurant",
                "address": "First Address",
                "total_score": 0,
            },
            response_only=True,
        ),
    ]
)
class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ["id", "name", "address", "total_score"]


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            name="Review Example For Request",
            value={
                "restaurant": 0,
                "text": "Comment on the restaurant.",
                "score": 10,
            },
            request_only=True,
        ),
        OpenApiExample(
            name="Review Example For Response",
            value={
                "id": 0,
                "author": 0,
                "restaurant": 0,
                "text": "Comment on the restaurant.",
                "score": 10,
            },
            response_only=True,
        ),
    ]
)
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["id", "author", "restaurant", "text", "score"]
        read_only_fields = ("author",)
