from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Customer
from .serializers import CustomerSerializer


from django.http import HttpResponse


# ==================================================
def all(request):
    print("all")
    print(request.path)
    print(request.method)
    return HttpResponse("<h3>Hello Django!</h3>")


# ==================================================
def home(request):
    print("home")
    print(request.method)
    return render(request, 'customers/home.html')


# ==================================================
class CustomersList(APIView):
    def _common(self, request):
        print("customers_list")
        print(request.method)

    # --------------------------------------------------
    def get(self, request, *args, **kwargs):
        self._common(request)
        data = []
        next_page = 1
        previous_page = 1
        customers = Customer.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(customers, 10)

        try:
            data = paginator.page(page)
            print('try success')
        except PageNotAnInteger:
            data = paginator.page(1)
            print('PageNotAnInteger')
        except EmptyPage:
            data = paginator.page(paginator.num_pages)
            print('EmptyPage')
        print('data =', data)

        serializer = CustomerSerializer(data, context={'request': request}, many=True)
        if data.has_next():
            next_page = data.next_page_number()
        if data.has_previous():
            previous_page = data.previous_page_number()

        return Response({'data': serializer.data,
                         'count_customers': paginator.count,
                         'num_pages': paginator.num_pages,
                         'next_link': '/api/customers/?page=' + str(next_page),
                         'prev_link': '/api/customers/?page=' + str(previous_page)})

    # --------------------------------------------------
    def post(self, request, *args, **kwargs):
        self._common(request)
        print(request.data)
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)


# ==================================================
class CustomersDetail(APIView):
    def _common(self, request, pk):
        print("customers_detail")
        print(request.method)

    def _get_customer(self, request, pk):
        self._common(request, pk)
        try:
            customer = Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            return None
        return customer

    # --------------------------------------------------
    def get(self, request, pk):
        customer = self._get_customer(request, pk)
        if not customer:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CustomerSerializer(customer, context={'request': request})
        return Response(serializer.data)

    # --------------------------------------------------
    def put(self, request, pk):
        customer = self._get_customer(request, pk)
        if not customer:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CustomerSerializer(customer, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
                        status=status.HTTP_404_NOT_FOUND)

    # --------------------------------------------------
    def delete(self, request, pk):
        customer = self._get_customer(request, pk)
        if not customer:
            return Response(status=status.HTTP_404_NOT_FOUND)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
