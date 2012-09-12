from django.template import Context, loader
from django.shortcuts import render_to_response
from directory.models import Project, Location, Perspective
from django.http import HttpResponse
from django.http import Http404
from django.template import RequestContext
import re

def css_screen(request):
  return render_to_response('css/screen.css')

def css_print(request):
  return render_to_response('css/print.css')
  
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
  latest_location_list = Location.objects.all().order_by('-mod_date')[:1000]
  return render_to_response('location/index.html', {'latest_location_list': latest_location_list})

def location_detail(request, location_id):
  path = request.path
  urlbase = "/".join(re.split("/",path)[0:-2])
  try:
    l = Location.objects.get(pk=location_id)
    perspectives = Perspective.objects.filter(location=l).order_by('-create_date')
    if len(perspectives) > 0:
      perspective = perspectives[0]
      initpers = {
        'lat': perspective.lat,
        'lng': perspective.lng,
        'heading': perspective.heading,
        'pitch': perspective.pitch,
        'zoom': perspective.zoom
        }
    else:
      initpers = False
    
    try:
      pid = int(location_id) - 1
      p = Location.objects.get(pk=pid)
      prev = urlbase + "/" + str(pid)
    except:
      prev = urlbase
    try: 
      nid = int(location_id) + 1
      n = Location.objects.get(pk=nid)
      next = urlbase + "/" + str(nid)
    except:
      next = urlbase
    
    googleaddress = re.sub('\+',' ',re.sub('\+\(.*','', l.googleaddress))
    
  except Location.DoesNotExist:
    raise Http404
  return render_to_response(
    'location/detail.html', 
    {'location': l,
     'prev': prev,
     'next': next,
     'gaddy': googleaddress,
     'initpers': initpers
    }, 
    context_instance=RequestContext(request)
  )

def save_pov_form(request):
  return render_to_response('location/save_pov_form.html')
  
def save_pov(request):
  if ('loc' in request.GET and request.GET['loc']) and ('lat' in request.GET and request.GET['lat']) and ('lng' in request.GET and request.GET['lng']) and ('heading' in request.GET and request.GET['heading']) and ('pitch' in request.GET and request.GET['pitch']) and ('zoom' in request.GET and request.GET['zoom']):
    loc = request.GET['loc']
    lat = request.GET['lat']
    lng = request.GET['lng']
    heading = request.GET['heading']
    pitch = request.GET['pitch']
    zoom = request.GET['zoom']

    newpers = Perspective(
      location=Location.objects.get(pk=loc),
      name="",
      lat=lat,
      lng=lng,
      heading=heading,
      pitch=pitch,
      zoom=zoom
      )
    newpers.save()
    
    return render_to_response('location/save_pov_results.html',
      {"loc":loc,
      "query": "Success"})
  else:
    return HttpResponse('Please submit a search term.')


def manage_add(request):
  return HttpResponse("Add data...")

def display_meta(request):
  values = request.META.items()
  values.sort()
  html = []
  for k, v in values:
    html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
  return HttpResponse('<table>%s</table>' % '\n'.join(html))
  

  
  