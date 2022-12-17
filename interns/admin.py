from django.contrib import admin
from .models import User, Profile, Curriculum_vitae, Applications, Work_experience, Referee, Education

# Register your models here.
admin.site.register(Education),
admin.site.register(User),
admin.site.register(Profile),
admin.site.register(Curriculum_vitae),
admin.site.register(Applications),
admin.site.register(Work_experience),
admin.site.register(Referee),