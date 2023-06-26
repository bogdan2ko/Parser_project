from django.urls import path
from otomoto_parser.views import OtomotoParserView

urlpatterns = [
    path('parser/', OtomotoParserView.as_view(), name='parser'),
]

