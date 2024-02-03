from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()



class Owner(models.Model):
    username = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True)


class PetProfile(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='pet_profiles')
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    breed = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='pet_photos/', blank=True, null=True)

    def __str__(self):
        return self.name
class Preferences(models.Model):
    user = models.OneToOneField(Owner, on_delete=models.CASCADE)
    theme = models.CharField(max_length=50, default='light')
    language = models.CharField(max_length=50, default='english')
    notification_enabled = models.BooleanField(default=True)
    preferred_pet_profile = models.ForeignKey(PetProfile, on_delete=models.SET_NULL, blank=True, null=True)
    def __str__(self):
        return f"Preferences for {self.user.username}"
    
class Match(models.Model):
    pet1 = models.ForeignKey(PetProfile, on_delete=models.CASCADE, related_name='initiated_matches')
    pet2 = models.ForeignKey(PetProfile, on_delete=models.CASCADE, related_name='received_matches')
    status = models.CharField(max_length=10)  # e.g., 'Liked', 'Matched'
    timestamp = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    message_text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class ESAOpportunity(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=255)
    date_time = models.DateTimeField()
    requirements = models.TextField(blank=True)

class ESARegistration(models.Model):
    opportunity = models.ForeignKey(ESAOpportunity, on_delete=models.CASCADE, related_name='registrations')
    pet = models.ForeignKey(PetProfile, on_delete=models.CASCADE, related_name='esa_registrations')
    status = models.CharField(max_length=10)  # e.g., 'Applied', 'Accepted'

class PetBehaviorLog(models.Model):
    pet = models.ForeignKey(PetProfile, on_delete=models.CASCADE, related_name='behavior_logs')
    behavior_description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)