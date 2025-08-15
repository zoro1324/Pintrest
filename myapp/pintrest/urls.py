
from django.urls import path
from . import views

app_name = 'pintrest'

urlpatterns = [
    path('',views.dashboard, name='dashboard'),
]

# ...../myapp.urls / pintrest.urls /
           
# ..... /pintrest/dashboard/

# ..... /dashboard/

# .....

# myapp -> None + pintrest -> home = ...../home

# myapp -> home / pintrest -> None = ..... /home

# myapp -> home / pintrest -> home / = ..... /home/home

