from django.contrib import admin
from django.urls import path
from firstapp import views
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='stats/')),
    path('building/',views.new),
    path('building/<int:id>/add-bricks/<int:n>',views.add),
    path('stats/', views.stats),
    path('building/<int:id>/add-bricks/',views.add)

]
