from .models import Profile
from pprint import pprint

def show_response(backend, user, response, *args, **kwargs):
    pprint(response)

def save_profile(backend, user, response, *args, **kwargs):

    if Profile == None:
        Profile.objects.create(
            user = user,
            website = response['user']['website'],
            instagram_username = response['user']['username']
        )
    # else:
    #     profile = Profile(user=user)
    #     profile.website = response['user']['website']
    #     profile.instagram_username = response['user']['username']
    #     profile.save()