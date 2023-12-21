from django.contrib import admin
from django.urls import path,include
# from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('api/', include('product.urls')),
    path('api/account/',include('account.urls')),
]

# from django.urls import path
# from django.views.generic import TemplateView
# from . import views

# urlpatterns = [
#     # Other URL patterns

#     # Route for React app (index.html)
#     path('', TemplateView.as_view(template_name='index.html'), name='index'),
# ]