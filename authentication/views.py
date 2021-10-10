from django.contrib.auth import get_user_model
from django.http.response import JsonResponse
from .models import User, Users
from django.contrib import messages
from django.contrib.auth import  login
from django.contrib.auth.hashers import check_password
from rest_framework.decorators import api_view, permission_classes, schema
from rest_framework.schemas import AutoSchema
from .serializers import UserSerializer 
from rest_framework import status
from rest_framework.response import Response
from django.core.exceptions import ValidationError
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token



# Create your views here.

class CustomAutoSchema(AutoSchema):
    def get_link(self, path, method, base_url):
        # override view introspection here...
        pass

@api_view(['GET', 'POST'])
@schema(CustomAutoSchema())
def register(request):
    
    """
    List all code users, or create a new users.
    """
    if request.method == 'GET':
        users = get_user_model().objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes([AllowAny])
def login_user(request):

        data = {}
        reqBody = JsonResponse.loads(request.body)
        email1 = reqBody['Email_Address']
        print(email1)
        password = reqBody['password']
        try:

            Account = User.objects.get(Email_Address=email1)
        except BaseException as e:
            raise ValidationError({"400": f'{str(e)}'})

        token = Token.objects.get_or_create(user=Account)[0].key
        print(token)
        if not check_password(password, Account.password):
            raise ValidationError({"message": "Incorrect Login credentials"})

        if Account:
            if Account.is_active:
                print(request.user)
                login(request, Account)
                data["message"] = "user logged in"
                data["email_address"] = Account.email

                Res = {"data": data, "token": token}

                return Response(Res)

            else:
                raise ValidationError({"400": f'Account not active'})

        else:
            raise ValidationError({"400": f'Account doesnt exist'})








# @api_view(['GET', 'POST'])
# def signin(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         password = request.POST['password']
#         user = authenticate(email=email, password=password)
#         if user is not None:
#             login(request, user)
#             messages.add_message(request, messages.SUCCESS, "You have successfully login!")
#             return redirect('index')
#         else:
#             messages.add_message(request, messages.WARNING, "Invalid credentials!")
#             return redirect('signin')
#     else:
#         return render(request, '')


