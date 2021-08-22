from rest_framework.generics import GenericAPIView as View
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from accounts.models import User
from accounts.permissions import IsAdmin
from accounts.serializers import UserSerializer
from records.models import Transaction
from records.serializers import (
    TransactionSerializer,
    TransactionCreateSerializer
)


class TransactionListAPI(View):

    permission_classes = [
        IsAuthenticated
    ]
    serializer_class = TransactionSerializer

    def get(self, request):
        user = request.user
        transactions = Transaction.objects.filter(user=user)\
            .order_by('-updated')
        transactions_serializer = self.get_serializer(transactions, many=True)

        response = Response(
            transactions_serializer.data
        )
        return response


class TransactionCreateAPI(View):

    permission_classes = [
        IsAuthenticated
    ]
    serializer_class = TransactionCreateSerializer

    def post(self, request):
        user = request.user
        transaction_data = request.data
        product_slug = request.data.get('slug')
        transaction = Transaction()

        if transaction.exists():
            return Response(
                {
                    "product": [
                        'TRANSACTION_PRODUCT_EXISTS'
                    ]
                }
            )
        else:
            transaction_serializer = self.get_serializer(data=transaction_data)
            transaction_serializer.is_valid(raise_exception=True)
            transaction_serializer.save(user=user)

        response = Response(
            transaction_serializer.data
        )
        return response


class TransactionDetailsAPI(View):

    permission_classes = [
        IsAuthenticated
    ]
    serializer_class = TransactionSerializer

    def get(self, request, transaction_slug):
        transaction = get_object_or_404(
            Transaction,
            slug=transaction_slug
        )
        transaction_serializer = self.get_serializer(transaction)

        response = Response(
            transaction_serializer.data
        )
        return response


class TransactionConfirmAPI(View):

    permission_classes = [
        IsAuthenticated
    ]
    serializer_class = TransactionSerializer

    def get(self, request, transaction_slug):
        transaction = get_object_or_404(
            Transaction,
            slug=transaction_slug
        )

        if transaction.user != request.user:
            return Response(
                {
                    'permission_denied': [
                        'You do not have permission to perform this operation'
                    ]
                },
                status.HTTP_401_UNAUTHORIZED
            )

        transaction.status = True
        transaction.save()

        transaction_serializer = self.get_serializer(transaction)

        response = Response(
            transaction_serializer.data
        )
        return response


class DeleteCompletedAPI(View):

    permission_classes = [
        IsAuthenticated
    ]
    serializer_class = TransactionSerializer

    def get(self, request):
        user = request.user
        transactions = Transaction.objects.filter(
            user=user,
            status=True
        )

        if transactions.exists():
            transactions.all().delete()

            return Response(
                {
                    'success': [
                        'Completed deliveries deleted'
                    ]
                }
            )
        return Response(
            {
                'none': [
                    'You do not have completed deliveries'
                ]
            }
        )


class TransactionUserGroupAPI(View):

    permission_classes = [
        IsAuthenticated,
        IsAdmin
    ]

    def get(self, request):
        transaction_users = Transaction.objects.values_list('user', flat=True)
        transaction_users = list(set(transaction_users))

        users = [
            User.objects.get(pk=pk) for pk in transaction_users
        ]
        transactions = []

        for user in users:
            user_transactions = Transaction.objects.filter(user=user)
            data = {
                'user': UserSerializer(user).data,
                'transactions': TransactionSerializer(
                    user_transactions, many=True
                ).data
            }
            transactions.append(data)

        response = Response(
            transactions
        )

        return response


class GetUserTransactionsAPI(View):

    permission_classes = [
        IsAuthenticated,
        IsAdmin
    ]
    serializer_class = TransactionSerializer

    def get(self, request, username):
        user = get_object_or_404(
            User,
            username=username
        )
        transactions = Transaction.objects.filter(user=user)
        transactions_serializer = TransactionSerializer(
            transactions,
            many=True
        )

        response = Response(
            transactions_serializer.data
        )
        return response
