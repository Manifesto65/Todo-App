from django.urls import path
from .views import index,login,signup,signout,deletetodo,changestatus

urlpatterns = [
    path('', index, name='homepage'),
    path('login', login, name='login'),
    path('signup', signup, name='signup'),
    path('logout', signout, name='logout'),
    path('delete-todo/<int:id>', deletetodo, name='deletetodo'),
    path('change-status-todo/<int:id>/<str:status>', changestatus, name='change-todo-status'),
]