from django.urls import path
from .views import signup, signUpPart2, signin, signout, index

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('signout/', signout, name='signout'),
    path('signup/step/2', signUpPart2, name='signUpPart2'),
    path('', index, name='home'),
    # Adicione outras URLs conforme necessário
]
