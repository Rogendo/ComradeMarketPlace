from django.urls import path, include
from rest_framework import routers
from .views import (
    ProductViewSet,
    CommentViewSet,
    ProductImageViewSet,
    CategoryViewSet,
    BookmarkViewSet,
)

router = routers.DefaultRouter(trailing_slash=False)

router.register("products", ProductViewSet, basename="products")
router.register("comments", CommentViewSet, basename="comments")
router.register("product-images", ProductImageViewSet, basename="product-images")
router.register("categories", CategoryViewSet, basename="categories")
router.register("bookmarks", BookmarkViewSet, basename="bookmarks")

urlpatterns = [
    path(
        "products/",
        ProductViewSet.as_view({"get": "get_products", "post": "create_product"}),
        name="product-list",
    ),
    path(
        "products/<int:id>/",
        ProductViewSet.as_view({"put": "update_product", "delete": "delete_product"}),
        name="product-detail",
    ),
    path(
        "comments/",
        CommentViewSet.as_view({"get": "get_comments", "post": "post_comment"}),
        name="comment-list",
    ),
    path(
        "comments/<int:id>/",
        CommentViewSet.as_view({"put": "update_comment", "delete": "delete_comment"}),
        name="comment-detail",
    ),
    path(
        "product-images/<int:pk>/images/",
        ProductImageViewSet.as_view(
            {"get": "images", "post": "images", "put": "images", "delete": "images"}
        ),
        name="product-image-list",
    ),
    path(
        "categories/",
        CategoryViewSet.as_view(
            {
                "get": "get_categories",
                "post": "create_category",
                "put": "update_category",
            }
        ),
        name="category-list",
    ),
    path(
        "bookmarks/",
        BookmarkViewSet.as_view(
            {
                "get": "get_bookmarks",
                "post": "create_bookmark",
                "put": "update_bookmark",
                "delete": "delete_bookmark",
            }
        ),
        name="bookmark-list",
    ),
    path("", include(router.urls)),
]
