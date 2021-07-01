from django.urls import path,include
from django.conf.urls.static import static
from .views import *

urlpatterns = [
	path('', Homepage, name='home-page'),
	path('about/', Aboutpage, name='about-page'),
	path('portfolio/', Portfolio, name='portfolio-page'),

]