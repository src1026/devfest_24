from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from .models import (PetProfile, Match, Message,
                     ESAOpportunity, ESARegistration, PetBehaviorLog)
from .serializers import (UserSerializer, PetProfileSerializer, MatchSerializer,
                          MessageSerializer, 
                          ESAOpportunitySerializer, ESARegistrationSerializer,
                          PetBehaviorLogSerializer)
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import PetProfile, Match

# each ModelViewSet class here provides an endpoint for a specific model
# so that each authenticated user can perform basic CRUD operations
# of these models via HTTP requests using the specified serializers
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class PetProfileViewSet(viewsets.ModelViewSet):
    queryset = PetProfile.objects.all()
    serializer_class = PetProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    permission_classes = [permissions.IsAuthenticated]

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

class ESAOpportunityViewSet(viewsets.ModelViewSet):
    queryset = ESAOpportunity.objects.all()
    serializer_class = ESAOpportunitySerializer
    permission_classes = [permissions.IsAuthenticated]

class ESARegistrationViewSet(viewsets.ModelViewSet):
    queryset = ESARegistration.objects.all()
    serializer_class = ESARegistrationSerializer
    permission_classes = [permissions.IsAuthenticated]

class PetBehaviorLogViewSet(viewsets.ModelViewSet):
    queryset = PetBehaviorLog.objects.all()
    serializer_class = PetBehaviorLogSerializer
    permission_classes = [permissions.IsAuthenticated]

# a viewset to handle highFives
class HighFiveView(APIView):
    # handle post request: send data to a server to create / update a resource
    def post(self, request, pet_id, direction):
        # extract current user from request 
        user = request.user
        try:
            # get the PetProfile for the current user and the target user 
            user_pet = PetProfile.objects.get(user=user)
            target_pet = PetProfile.objects.get(pk=pet_id)
        except PetProfile.DoesNotExist:
            return Response({'error': 'Pet not found.'}, status=status.HTTP_404_NOT_FOUND)
        
        if direction == 'like':
            # check if the target_pet already liked the user's pet
            if Match.objects.filter(pet1=target_pet, pet2=user_pet, liked=True).exists():
                # if yes, return a like 
                Match.objects.create(pet1=user_pet, pet2=target_pet, liked=True)
                return Response({'match': True}, status=status.HTTP_200_OK)
            else:
                # record the like if no mutual like is found 
                Match.objects.create(pet1=user_pet, pet2=target_pet, liked=True)
                return Response({'match': False}, status=status.HTTP_200_OK)

        elif direction == 'dislike':
            # create a Match object where liked=False
            Match.objects.create(pet1=user_pet, pet2=target_pet, liked=False)
            return Response({'match': False}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid swipe direction.'}, status=status.HTTP_400_BAD_REQUEST)
