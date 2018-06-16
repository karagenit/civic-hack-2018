from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # The manager to get Profile objects
    objects = models.Manager()
    # The primary key
    # uid = models.IntegerField(primary_key=True)
    timezone = models.CharField(max_length=50, default='EST')
    # A one to many relationship to team members that is connected when the
    # Profile is a TEAM_LEADER with people in their team.
    team = models.ForeignKey(
        'self',
        models.CASCADE,
        null=True
    )
    # The user variable to allow authentication to work

    bio = models.CharField(max_length=1000, default = "")

    CHOICES = (('1', 'Senior Citizen',), ('2', 'Volunteer Driver',), ('3', 'Restaraunt'))
    member_type = models.CharField(max_length=50, choices=CHOICES)

    permission = {}  # the key is the permission itself which can be a url or just a word for the permission the value is a list of orgainizations it can do this action for

    def is_client(profile):
        return profile.member_type == '1'

    def is_driver(profile):
        return profile.member_type == '2'

    def is_restaurant(profile):
        return profile.member_type == '3'

    # add permission to the profile for the PERM and the ORG
    def addPermission(self, perm, org):
        if self.permission.get(perm,None) is None:
            self.permission[perm] = [org]
        else:
            self.permission[perm].extend(org)

    # checks to see if permission contains PERM for ORG
    def hasPerm(self, perm, org):
        for i in self.permission[perm]:
            if i == org:
                return True
        return False
    #checks to see if anyone has the permission adn returns authorized organizations
    def allWithPerm(self, perm):
        return self.permission.get(perm, None)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    #TODO: should be able to delete all the except: stuff after all the users have run this
    try:
        instance.profile.save()
    except:
        print("stuff")
