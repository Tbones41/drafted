from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile, Curriculum_vitae, Education, Work_experience
# Create your views here.
def interns(request):
    intern = {
        
    }
    return render(request, 'interns/body.html')


def profile(request):
    profiles = Profile.objects.get(age=23)
    cv  = Curriculum_vitae.objects.get(owner=profiles.id)
    work = Work_experience.objects.filter(cv_id=cv.id)
    edu = Education.objects.filter(cv_id=cv.id)
    profile = {
        'name':profiles.name,
        'age':profiles.age,
        'gender':profiles.gender,
        'location':cv.location,
        'work':work,
        'edu':edu,
    }
    return render(request, 'interns/profile.html', context=profile)