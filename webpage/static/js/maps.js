var map;
function initialize() {
	var mapOptions = {
		zoom: 10,
        center: new google.maps.LatLng(27.072637, -109.443792)
      };
      map = new google.maps.Map(document.getElementById('map-canvas'),
          mapOptions);

      var local = new google.maps.LatLng(27.072637, -109.443792);
      var contentString = '<div id="content">'+
      '<div id="siteNotice">'+
      '</div>'+
      '<h1 id="firstHeading" class="firstHeading">Oficionas</h1>'+
      '<div id="bodyContent">'+
      '<p><b>Avenida</b> Folsom, <b>Suite 600 </b> San Francisco, CA 94107</p>' +
      '<img style="width: 200px;height: 150px;" src="http://www.diarioabogado.com/attachments/Image/localRuta19.jpg?template=generic" alt="...">'
      '</div>'+
      '</div>';

  var infowindow = new google.maps.InfoWindow({
      content: contentString
  });

  var marker = new google.maps.Marker({
      position: local,
      map: map,
      title: 'Uluru (Ayers Rock)'
  });
  google.maps.event.addListener(marker, 'click', function() {
    infowindow.open(map,marker);
  });
}
      
	  marker.setIcon('http://maps.gstatic.com/mapfiles/api-3/images/spotlight-poi.png');
  
	
    google.maps.event.addDomListener(window, 'load', initialize);


  
