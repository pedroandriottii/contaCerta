from django.urls import path
from .views import signup, signin, signout, index

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('signout/', signout, name='signout'),
    path('', index, name='home'),
    # Adicione outras URLs conforme necessário
]
