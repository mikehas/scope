from django.template import Context, loader
from django.shortcuts import render_to_response
from directory.models import Project, Location
from django.http import HttpResponse
from django.http import Http404
from django.template import RequestContext


def index(request):
    latest_project_list = Project.objects.all().order_by('-create_date')[:5]
    return render_to_response('projects/index.html', {'latest_project_list': latest_project_list})

def detail(request, project_id):
    try:
        p = Project.objects.get(pk=project_id)
    except Project.DoesNotExist:
        raise Http404
    return render_to_response('project/detail.html', {'project': p})
    
def location_index(request):
    latest_location_list = Location.objects.all().order_by('-mod_date')[:5]
    return render_to_response('location/index.html', {'latest_location_list': latest_location_list})

def location_detail(request, location_id):
    try:
        l = Location.objects.get(pk=location_id)
    except Location.DoesNotExist:
        raise Http404
    return render_to_response(
      'location/detail.html', 
      {'location': l}, 
      context_instance=RequestContext(request)
    )

def manage_add(request):
  return HttpResponse("Add data...")
