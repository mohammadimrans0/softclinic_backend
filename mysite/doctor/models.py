from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from patient.models import Patient


class SlugMixin(models.Model):
    slug = models.SlugField(max_length=40, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        abstract = True

class Specialization(SlugMixin):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

class Designation(SlugMixin):
    name = models.CharField(max_length = 30)

    def __str__(self):
            return self.name

class AvailableTime(models.Model):
    name = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.name


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(upload_to="doctor/images/", default="doctor/images/default.jpg")
    designation = models.ManyToManyField(Designation)
    specialization =  models.ManyToManyField(Specialization)
    available_time = models.ManyToManyField(AvailableTime)
    fee = models.PositiveIntegerField()
    meet_link = models.URLField(max_length=200)
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


# review doctor
STAR_CHOICES = [
    (1, '⭐'),
    (2, '⭐⭐'),
    (3, '⭐⭐⭐'),
    (4, '⭐⭐⭐⭐'),
    (5, '⭐⭐⭐⭐⭐'),
]
class Review(models.Model):
    reviewer = models.ForeignKey(Patient, on_delete = models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete = models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    rating = models.IntegerField(choices=STAR_CHOICES)
    
    def __str__(self):
        return f"Patient : {self.reviewer.user.first_name} reviewed Doctor : {self.doctor.user.first_name}"