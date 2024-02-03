from django.shortcuts import render

from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from .models import (PetProfile, Match, Message,
                     ESAOpportunity, ESARegistration, PetBehaviorLog)
from .serializers import (UserSerializer, PetProfileSerializer, MatchSerializer,
                          MessageSerializer, EventSerializer, EventAttendeeSerializer,
                          ESAOpportunitySerializer, ESARegistrationSerializer,
                          PetBehaviorLogSerializer, MentalHealthResourceSerializer)

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