from django.urls import path
from .views import signup, signUpPart2, signin, signout, index, category_list, create_category, TransactionList, CreateTransaction, CategoryTotalSpent

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('signout/', signout, name='signout'),
    path('signup/step/2', signUpPart2, name='signUpPart2'),
    path('categories/', category_list, name='category_list'),
    path('categories/create/', create_category, name='create_category'),
    path('transactions/', TransactionList, name='TransactionList'),
    path('transactions/create/', CreateTransaction, name='CreateTransaction'),
    path('transactions/category-total-spent/', CategoryTotalSpent, name='CategoryTotalSpent'),
    path('', index, name='home'),
]
