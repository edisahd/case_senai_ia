from django.views.generic import TemplateView
from django.urls import path

urlpatterns = [
    path('', TemplateView.as_view(
        template_name='documentation/swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='documentation'),
]