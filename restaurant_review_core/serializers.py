from rest_framework import serializers
from restaurant_review_core.models import Restaurant, Review


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ["id", "name", "address", "total_score"]


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["id", "author", "restaurant", "text", "score"]
        read_only_fields = ("author",)
