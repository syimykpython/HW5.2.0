from django.urls import path
import product.views as fv

urlpatterns = [
    
    path("/categories/", fv.category_list),
    path("/categories/<int:id>/", fv.category_detail),

    path("/products/", fv.product_list),
    path("/products/<int:id>/", fv.product_detail),

    path("/reviews/", fv.review_list),
    path("/reviews/<int:id>/", fv.review_detail),


]