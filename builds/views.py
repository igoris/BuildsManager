from django.http import Http404
from django.views.generic import list_detail
from builds.models import Build, Project

def builds_by_project(request, project_name):
    
    try:
        project = Project.objects.get(title__iexact=project_name)
    except Project.DoesNotExist:
        raise Http404

    return list_detail.object_list(
        request,
        queryset = Build.objects.filter(project=project).order_by('-pub_date'),
        template_name = "builds/builds_by_project.html",
        template_object_name = "builds",
        extra_context = {"project" : project}
    )
