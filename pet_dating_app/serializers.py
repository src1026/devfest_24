from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model

from .models import (PetProfile, Match, Message,
                     ESAOpportunity, ESARegistration, PetBehaviorLog)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class PetProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetProfile
        fields = '__all__'

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class ESAOpportunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ESAOpportunity
        fields = '__all__'

class ESARegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ESARegistration
        fields = '__all__'

class PetBehaviorLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetBehaviorLog
        fields = '__all__'
