from rest_framework.viewsets import ReadOnlyModelViewSet
from django.db.models import Avg, Count

from .models import Category, Product, Review
from .serializers import (
    CategorySerializer,
    ProductSerializer,
    ReviewSerializer,
)


class CategoryViewSet(ReadOnlyModelViewSet):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.annotate(
            products_count=Count('products')
        )


class ProductViewSet(ReadOnlyModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.annotate(
            rating=Avg('reviews__stars')
        ).prefetch_related('reviews')


class ReviewViewSet(ReadOnlyModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
