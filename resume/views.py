from django.shortcuts import render
from resume.models import Description,Education,Experience,Certification,SkillSet,Project

# Create your views here.
def resume(request):
    description = Description.objects.all()
    education = Education.objects.all()
    experience = Experience.objects.all()
    certification = Certification.objects.all()
    skillset = SkillSet.objects.all()
    project = Project.objects.all()
    params = {
        'description':description, 'education':education, 'experience':experience, 
        'certification':certification, 'skillset':skillset, 'project':project
    }
    return render(request, 'resume/index.html', params)