from django.db import models
import uuid


# Create your models here.
class User(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    profile = models.OneToOneField('Profile', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    phone = models.BigIntegerField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Profile(models.Model):
    GENDER = (
        ('F', 'Female'),
        ('M', 'Male'),
        ('NB', 'Non-binary'),
        ('Tr-M', 'Transgender Male'),
        ('Tr-F', 'Transgender Female'),
        ('NA', 'Prefer not to say'),
    )
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    profile_image = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(choices = GENDER, max_length=200)
    #c_v = models.OneToman('Curriculum_vitae', on_delete=models.CASCADE)
    #applications = models.ForeignKey('Applications', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Curriculum_vitae(models.Model):
    id = models.IntegerField(unique=True, primary_key=True, editable=False)
    owner = models.OneToOneField(Profile, on_delete=models.CASCADE, null=True)
    location = models.CharField(max_length=200)
    #work_experience = models.ForeignKey('Work_experience', on_delete=models.CASCADE)
    #education = models.ForeignKey('Education', on_delete=models.CASCADE)

    def __str__(self):
        return self.location


class Applications(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    company = models.CharField(max_length=200)
    role = models.CharField(max_length=200)

    def __str__(self):
        return self.company + ' - ' + self.role


class Work_experience(models.Model):
    SECTOR = (
        ('Health', 'Health'),
        ('Insurance', 'Insurance'),
        ('Education', 'Education'),
        ('Banking', 'Banking')
    )
    id = models.IntegerField(unique=True, primary_key=True, editable=False)
    cv_id = models.ForeignKey(Curriculum_vitae, on_delete=models.CASCADE, null=True)
    workplace = models.CharField(max_length=200)
    workplace_address = models.TextField()
    job_title = models.CharField(max_length=200)
    job_description = models.TextField()
    date_started = models.DateField(null=True)
    date_ended = models.DateField(null=True)
    ongoing = models.BooleanField(null=True)
    referee = models.OneToOneField('Referee', on_delete=models.CASCADE)
    sector = models.CharField(choices=SECTOR, max_length=200)

    def __str__(self):
        return self.workplace



class Referee(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=200)
    number = models.BigIntegerField()
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Education(models.Model):
    GRADE = (
        ('First Class', '1'),
        ('Second Class Upper', '2'),
        ('Second Class Lower', '3'),
        ('Third Class', '4'),
        ('Passed', '5'),
        ('Failed', '6'),
        ('No Grade', '7'),
    )

    LEVEL = (
        ('Primary', 'Primary School'),
        ('Secondary', 'Secondry School'),
        ('University', 'University'),
        ('Masters', 'Masters'),
        ('PhD', 'PhD'),
    )
    id = models.IntegerField(unique=True, primary_key=True, editable=False)
    cv_id = models.ForeignKey(Curriculum_vitae, on_delete=models.CASCADE, null=True)
    school = models.CharField(max_length=200)
    Level_of_edu = models.CharField(choices=LEVEL, max_length=200)
    degree = models.CharField(max_length=50)
    grade = models.CharField(choices=GRADE, max_length=200)
    date_started = models.DateField(null=True)
    date_ended = models.DateField(null=True)
    ongoing = models.BooleanField(null=True)

    def __str__(self):
        return self.school
