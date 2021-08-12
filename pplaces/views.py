from django.shortcuts import render, redirect
from .forms import ProjectForm, ProjectLocationForm
from .models import Project, PriorityPlacesREF, ProjectLocation

# Create your views here.
def projects(request):
    projects = Project.objects.all()
#    locations = ProjectLocation.objects.all()  projects.projectLocation_set.all()
    records = projects.count()
    context = {
        'projects': projects,
        'records': records,
#        'locations': locations,
     }
    return render(request, 'pplaces/projects.html', context)

def createProject(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            prject = form
# ---------  Translate section ---------------
#            translator = Translator()
#            Title_fr = translator.translate(project.ProjectTitleEnglish,dest='fr')
#            PurposeDescripton_fr = translator.translate(project.ProjectPurposeDescriptonEnglish,dest='fr')
#            LocationDescripton_fr = translator.translate(project.GeneralLocationDescriptonEnglish,dest='fr')
            prject.ProjectTitleFrench = 'Titulo en frances'
            prject.ProjectPurposeDescriptonFrench = "Descripcion en frances"
            prject.GeneralLocationDescriptonFrench = "General Location en frances"
# ---------  End Translate section ---------------
            prject.save()
            return redirect('projects')

    context = {'form': form, 'title': 'Create Project' }
    return render(request, "pplaces/project-form.html", context)