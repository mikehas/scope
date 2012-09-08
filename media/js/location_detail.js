var geocoder;
   var map;
   var panorama;
   function initialize() {
     var initlatlng = new google.maps.LatLng(-34.397, 150.644);
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
     
     var panoramaOptions = {
           position: new google.maps.LatLng(initlatlng),
           pov: {
             heading: 115,
             pitch: -13,
             zoom: 1
           },
           visible: true
     };
     panorama = new google.maps.StreetViewPanorama(document.getElementById('pano_canvas'), panoramaOptions);
     
     codeAddress("{{ gaddy }}", function(mylatlng) {
         map.setCenter(mylatlng);
         var marker = new google.maps.Marker({
             map: map,
             position: mylatlng
         });
         marker.setMap(map);
         panorama.setPosition(mylatlng);
     });
     
 };
   
 function codeAddress(myloc,cbfunc) {
     geocoder = new google.maps.Geocoder();
     var address = myloc;
     geocoder.geocode( { 'address': address}, function(results, status) {
       if (status == google.maps.GeocoderStatus.OK) {
         cbfunc(results[0].geometry.location);
       } else {
         alert("Geocode was not successful for the following reason: " + status);
       }
     });
 };
 
 function savePanoramaPov() {
     pov = panorama.getPov();
     
     pano_heading = pov.heading;
     pano_pitch = pov.pitch;
     pano_zoom = pov.zoom;
     output = "Heading: " + String(pov.heading) + ", Pitch:  " + String(pov.pitch) + ", Zoom:  "+ String(pov.zoom)
     alert(output);
 };