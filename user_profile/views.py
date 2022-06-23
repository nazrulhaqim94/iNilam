from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserProfile
from .serializers import UserProfileSerializer

class GetUserProfileView(APIView):
    def get(self, request, format=None):
        try:
            user = self.request.user
            email = user.email

            # user = User.objects.get(id=user.id)

            user_profile = UserProfile.objects.get(user=user)
            user_profile = UserProfileSerializer(user_profile)

            return Response({'profile': user_profile.data, 'email': str(email)})
        except:
            return Response({'error': 'Something went wrong when retrieving user profile'})

class GetUserProfileAllView(APIView):
    def get(self, request):
        users = UserProfile.objects.all()
        serializers = UserProfileSerializer(users, many=True)
        return Response(serializers.data)

class UpdateUserProfileView(APIView):
    def put(self, request, format=None):

        try:
            user = self.request.user
            email = user.email

            data = self.request.data
            first_name = data['first_name']
            last_name = data['last_name']
            role = data['role']
            darjah = data['darjah']
            kelas = data['kelas'] 

            # user = User.objects.get(id=user.id)

            UserProfile.objects.filter(user=user).update(first_name=first_name, last_name=last_name, role=role, darjah=darjah, kelas=kelas)

            user_profile = UserProfile.objects.get(user=user)
            user_profile = UserProfileSerializer(user_profile)

            return Response({'profile': user_profile.data, 'email': str(email), 'success':'Profile Updated'})
        except:
            return Response({'error': 'Something went wrong when updating profile'})
