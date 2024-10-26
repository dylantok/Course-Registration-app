from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    SCHOOL_YEAR_CHOICES = [
        ('1', '1年'),
        ('2', '2年'),
        ('3', '3年'),
        ('4', '4年')
    ]

    UNDERGRADUATE_CHOICES = [
        ('management', '経営学部'),
        ('commerce', '商学部'),
        ('human_sciences', '人間科学部')
    ]

    COURSE_CHOICES = [
        ('management', '経営学部'),
        ('commerce', '商学部'),
        ('human_sciences', '人間科学部')
    ]
    ENGLISH_CLASS_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C')
    ]
    REPEATING_A_COURSE_CHOICE = [
        ('あり', 'あり'),
        ('なし', 'なし')
    ]
    FIRST_AND_SECOND_TERMS_SEMESTER_CHOICE = [
        ('前期', '前期'),
        ('後期', '後期')
    ]
    SEMINAR_MEMBERSHIP_CHOICE = [
        ('加入', '入っている'),
        ('未加入', '入っていない')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school_year = models.CharField(max_length=1, choices=SCHOOL_YEAR_CHOICES)
    undergraduate = models.CharField(max_length=20, choices=UNDERGRADUATE_CHOICES)
    course = models.CharField(max_length=20, choices=COURSE_CHOICES)
    english_class = models.CharField(max_length=20, choices=ENGLISH_CLASS_CHOICES)
    repeating_a_course = models.CharField(max_length=20, choices=REPEATING_A_COURSE_CHOICE)
    First_and_second_terms_semester = models.CharField(max_length=20, choices=FIRST_AND_SECOND_TERMS_SEMESTER_CHOICE)
    Seminar_membership = models.CharField(max_length=20, choices=SEMINAR_MEMBERSHIP_CHOICE)
    def __str__(self):
        return self.user.username