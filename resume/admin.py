from django.contrib import admin

# Register your models here.
from resume.models import Description,Education,Experience,Certification,SkillSet,Project

admin.site.register(Description)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Certification)
admin.site.register(SkillSet)
admin.site.register(Project)