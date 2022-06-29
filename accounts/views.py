from .models import User
from numpy import append, empty
from rest_framework.views import APIView
from rest_framework import permissions
from django.contrib import auth
from rest_framework.response import Response
from user_profile.models import UserProfile
from .serializers import UserSerializer
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect, csrf_exempt
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import ROLE_CHOICES, DARJAH, KELAS
from rest_framework import status
from django.utils.decorators import method_decorator

class RoleChoices(APIView):
    permission_classes = (AllowAny, )
    def get(self, request, format=None):

        my_choices = []
        choice_dict = dict(ROLE_CHOICES)
        for key, value in choice_dict.items():

            itered_dict = {"key": key, "value": value}
            my_choices.append(itered_dict)
        return Response(my_choices)

class DarjahChoices(APIView):
    permission_classes = (AllowAny, )
    def get(self, request, format=None):

        my_choices = []
        choice_dict = dict(DARJAH)
        for key, value in choice_dict.items():

            itered_dict = {"key": key, "value": value}
            my_choices.append(itered_dict)
        return Response(my_choices)

class KelasChoices(APIView):
    permission_classes = (AllowAny, )
    def get(self, request, format=None):

        my_choices = []
        choice_dict = dict(KELAS)
        for key, value in choice_dict.items():

            itered_dict = {"key": key, "value": value}
            my_choices.append(itered_dict)
        return Response(my_choices)

class CheckAuthenticatedView(APIView):
    def get(self, request, format=None):
        user = self.request.user
        try:
            # isAuthenticated = User.is_authenticated
            isAuthenticated = user.is_authenticated
            role = user.role

            print(role)

            if isAuthenticated and role == "Teacher":
                return Response({'isAuthenticated':'success teacher'})
            elif isAuthenticated and role == "Student":
                return Response({'isAuthenticated':'success student'})
            else:
                return Response({'isAuthenticated': 'error'})
        except:
            return Response({'error': 'Something went wrong'})

@method_decorator(csrf_protect, name='dispatch')
class SignupView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        data = self.request.data

        email = data['email']
        password = data['password']
        re_password = data['re_password']
        first_name = data['first_name']
        last_name = data['last_name']
        role = data['role']
        darjah = data['darjah']
        kelas = data['kelas']

        print(data)

        try:
            if password == re_password:
                if User.objects.filter(email=email).exists():
                    return Response({'error': 'Username already exists'})
                else:
                    if len(password) < 6:
                        return Response({'error': 'Password must be at least 6 character'})
                    else:
                        if role == "Teacher":

                            joined_darjah = ",".join(darjah)
                            joined_kelas = ",".join(kelas)

                            print(joined_darjah, joined_kelas)

                            user = User.objects.create_user(email=email, password=password, first_name=first_name , last_name=last_name, role=role, darjah=joined_darjah, kelas=joined_kelas)

                            # user.save()

                            user = User.objects.get(id=user.id)

                            user_profile = UserProfile.objects.create(user=user, first_name=first_name, last_name=last_name, role=role, darjah=joined_darjah, kelas=joined_kelas)
                            # user_profile.save()

                        else:

                            user = User.objects.create_user(email=email, password=password, first_name=first_name , last_name=last_name, role=role, darjah=darjah, kelas=kelas)

                            # user.save()

                            user = User.objects.get(id=user.id)

                            user_profile = UserProfile.objects.create(user=user, first_name=first_name, last_name=last_name, role=role, darjah=darjah, kelas=kelas)
                            # user_profile.save()


                        return Response({'success': 'User created successfully'})
            elif not role:
                return Response({'error': 'No Role Selected'})
            else:
                return Response({'error': 'Password do no match'})
        except:
            return Response({'error': 'Something went wrong'})

@method_decorator(csrf_protect, name='dispatch')
class LoginView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        data = self.request.data

        email = data['email']
        password = data['password']

        try:

            user = auth.authenticate(email=email, password=password)

            if user is not None:
                auth.login(request, user)
                return Response({'success': 'User authenticated'})
            else:
                return Response({'error': 'Error Authenticating'})
        except:
            return Response({'error': 'Something went wrong'})

class LogoutView(APIView):
    def post(self, request, format=None):
        try:
            auth.logout(request)
            return Response({'success': 'Logged Out'})
        except:
            return Response({'error': 'Something went wrong when logging out'})

@method_decorator(ensure_csrf_cookie, name='dispatch')
class GetCSRFToken(APIView):
    permission_classes = (permissions.AllowAny, )

    def get(self, request, format=None):
        return Response({'success': 'CSRF cookie set'})

class DeleteAccountView(APIView):
    def delete(self, request, format=None):
        user = self.request.user

        try:
            User.objects.filter(id=user.id).delete()

            return Response({'success': 'User Deleted Successfully'})
        except :
            return Response({'error': 'Something went wrong'})

class GetUsersView(APIView):
    permission_classes = (permissions.AllowAny, )

    def get(self, request, format=None):
        users= User.objects.all()
        users = UserSerializer(users, many=True)
        return Response(users.data)
