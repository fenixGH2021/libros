from django.db.models.base import Model
from django.forms import ModelForm
from .models import Project, ProjectLocation


class ProjectForm(ModelForm):
     class Meta:
         model = Project
         fields = [
             'ECCCAssignedProjectIdentfer',
             'ProjectTitleEnglish',
             'ProjectPurposeDescriptonEnglish',
             'GeneralLocationDescriptonEnglish',
             'PriorityPlaceUID',
             'ProjectLocation',
             ]
     def __init__(self, *args, **kwargs):
         super(ProjectForm, self).__init__(*args, **kwargs)


class ProjectForm_fr(ModelForm):
     class Meta:
         model = Project
         fields = [
             'ECCCAssignedProjectIdentfer',
             'ProjectTitleFrench',
             'ProjectPurposeDescriptonFrench',
             'GeneralLocationDescriptonFrench',
             'PriorityPlaceUID',
             'ProjectLocation',
             ]
     def __init__(self, *args, **kwargs):
         super(ProjectForm, self).__init__(*args, **kwargs)


class ProjectLocationForm(ModelForm):
    class Meta:
        model = ProjectLocation
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ProjectLocationForm, self).__init__(*args, **kwargs)

    