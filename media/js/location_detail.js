var geocoder;
var map;
var panorama;

function initialize(gaddy) {
  var initlatlng = new google.maps.LatLng(0,0);
  var mapOptions = {
    zoom: 15,
    center: initlatlng,
    mapTypeId: google.maps.MapTypeId.ROADMAP
  }
  map = new google.maps.Map(document.getElementById("map_canvas"), mapOptions);

  var marker = new google.maps.Marker({
    map: map,
    position: initlatlng
  });

  initPovForm = document.forms['save_pov_form'];

  var panoramaOptions = {
    position: new google.maps.LatLng(initlatlng),
    pov: {
      heading: 0,
      pitch: 0,
      zoom: 1
    },
    visible: true
  };

  panorama = new google.maps.StreetViewPanorama(document.getElementById('pano_canvas'), panoramaOptions);
  
  // Add listener to update save_pov_form on panorama change
  google.maps.event.addListener(panorama, 'pov_changed', populateSavePovForm);
  
  // Prevent geocode lookup if a perspective has already been saved.
  if (havePerspective) {
    var mylatlng = new google.maps.LatLng(parseFloat(initPovForm["lat"].value), parseFloat(initPovForm["lng"].value));
    map.setCenter(mylatlng);
    var marker = new google.maps.Marker({
      map: map,
      position: mylatlng
    });
    marker.setMap(map);
    panorama.setPosition(mylatlng);
    panorama.setPov({heading:parseFloat(initPovForm["heading"].value), pitch:parseFloat(initPovForm["pitch"].value), zoom:parseInt(initPovForm["zoom"].value)});    
  }else {
    // Get the geocoded address coords, (mylatlng), then set the new 
    // map object's centers.
    codeAddress(gaddy, function(mylatlng) {
      map.setCenter(mylatlng);
      var marker = new google.maps.Marker({
        map: map,
        position: mylatlng
      });
      marker.setMap(map);
      panorama.setPosition(mylatlng);
    });
  }
  


};

function codeAddress(myloc, cbfunc) {
  geocoder = new google.maps.Geocoder();
  var address = myloc;
  geocoder.geocode({
    'address': address
  }, function(results, status) {
    if (status == google.maps.GeocoderStatus.OK) {
      cbfunc(results[0].geometry.location);
    } else {
      alert("Geocode was not successful for the following reason: " + status);
    }
  });
  
};

function populateSavePovForm() {
  var pov = panorama.getPov();
  var heading = pov.heading;
  var pitch = pov.pitch;
  var zoom = pov.zoom;
  
  var latlng = panorama.getPosition();
  var lat = latlng.lat();
  var lng = latlng.lng();
  
  // var output = "Longitude: " + lat + ", Latitude: " + lng + ", Heading: " + String(pov.heading) + ", Pitch:  " + String(pov.pitch) + ", Zoom:  " + String(pov.zoom)
  
  savePovForm = document.forms['save_pov_form'];
  savePovForm.elements["lat"].value = lat;
  savePovForm.elements["lng"].value = lng;
  savePovForm.elements["heading"].value = heading;
  savePovForm.elements["pitch"].value = pitch;
  savePovForm.elements["zoom"].value = zoom;
}
