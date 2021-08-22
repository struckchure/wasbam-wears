from django.urls import path

from records.api import (
	TransactionListAPI,
	TransactionCreateAPI,
	TransactionDetailsAPI,
	TransactionConfirmAPI,
	DeleteCompletedAPI,
	TransactionUserGroupAPI,
	GetUserTransactionsAPI
)

app_name = 'records'

urlpatterns = [
	path('records/', TransactionListAPI.as_view(), name='list'),
	path('records/create/', TransactionCreateAPI.as_view(), name='create'),
	path('records/<slug:transaction_slug>/details/', TransactionDetailsAPI.as_view(), name='details'),
	path('records/<slug:transaction_slug>/confirm-order/', TransactionConfirmAPI.as_view(), name='confirm'),
	path('records/delete-completed/', DeleteCompletedAPI.as_view(), name='delete-completed'),
	path('records/user-groups/', TransactionUserGroupAPI.as_view(), name='user-groups'),
	path('records/<str:username>/all/', GetUserTransactionsAPI.as_view(), name='user-transactions')
]
