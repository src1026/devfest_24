from django.shortcuts import render

from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from .models import (PetProfile, Match, Message, Event, EventAttendee,
                     ESAOpportunity, ESARegistration, PetBehaviorLog, MentalHealthResource)
from .serializers import (UserSerializer, PetProfileSerializer, MatchSerializer,
                          MessageSerializer, EventSerializer, EventAttendeeSerializer,
                          ESAOpportunitySerializer, ESARegistrationSerializer,
                          PetBehaviorLogSerializer, MentalHealthResourceSerializer)

# 使用Django REST Framework的ViewSets来简化视图的创建

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]  # 例如，这里我们要求用户必须认证

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

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]

class EventAttendeeViewSet(viewsets.ModelViewSet):
    queryset = EventAttendee.objects.all()
    serializer_class = EventAttendeeSerializer
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

class MentalHealthResourceViewSet(viewsets.ModelViewSet):
    queryset = MentalHealthResource.objects.all()
    serializer_class = MentalHealthResourceSerializer
    permission_classes = [permissions.IsAuthenticated]
