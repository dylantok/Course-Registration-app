from django.contrib import admin
from.models import SubjectTable,AcquiredCredits,UserAcquiredCredits

# Register your models here.
admin.site.register(SubjectTable)
admin.site.register(AcquiredCredits)
admin.site.register(UserAcquiredCredits)