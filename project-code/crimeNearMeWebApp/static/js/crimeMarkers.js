var map
var crimeList
var infowindow = {}

function getNearCrimes(latitude, longitude) {

    var sendData = {
        "latitude": latitude,
        "longitude": longitude
    };

    var formURL = "/crimeSearch";

    $.ajax({
        url: formURL,
        type: "POST",
        data: JSON.stringify(sendData),
        dataType: 'json',
        async: true,
        contentType: "application/json; charset=utf-8",
        success: function(data, status, jqXHR) {

            //alert(jqXHR.responseText);
            //alert(data[0].latitude);
            //alert(data[0].longitude);


            var enteredPoint = {
                lat: parseFloat(latitude),
                lng: parseFloat(longitude)
            };

            map = new google.maps.Map(document.getElementById('map'), {
                zoom: 13,
                center: enteredPoint
            });

            for (var i = 0; i < data.length; i++) {


                var contentString = '<div id="content">' +
                    '<div id="siteNotice">' +
                    '</div>' +
                    '<h1 id="firstHeading" class="firstHeading">'+data[i].primary_description+'</h1>' +
                    '<div id="bodyContent">' +
                    '<b>Type</b>: '+data[i].primary_description+'<br>' +
                    '<b>Details</b>: '+data[i].secondary_description+'<br>' +
                    '<b>Block</b>: '+data[i].block+'<br>' +
                    '<b>Year</b>: '+data[i].year+'<br>' +
                    '<b>Arrested</b>: '+data[i].arrested+'<br>' +
                    '<b>Reported Date</b>: '+data[i].date+'<br>' +
                    '<b>GPS</b>: '+data[i].gps_location+'<br>' +
                    '<b>Clusterded correct?</b>: '+data[i].clustered+'<br>' +
                    '</div>' +
                    '</div>';


                infowindow[i] = new google.maps.InfoWindow({
                    content: contentString
                });



                var location = {
                    lat: parseFloat(data[i].latitude),
                    lng: parseFloat(data[i].longitude)
                };


                crimeObj = crimeList[data[i].primary_description];
                
                var marker = new google.maps.Marker({
                    position: location,
                    icon: '/static/images/markers/' + crimeObj[0] + '.png',
                    title: data[i].primary_description
                });
                
                marker.set("id", i);
   
                marker.setMap(map);
                
                marker.addListener('click', function(event) {
                
                    infowindow[this.get("id")].open(map, this);
                    
                });
                
                

            }



        },
        error: function(jqXHR, status, errorThrown) {
            // if fails 

            alert(jqXHR.responseText);
        }
    });
    // e.preventDefault();

}

function getCrimeList() {

    var formURL = "/crimeList";

    $.ajax({
        url: formURL,
        type: "GET",
        dataType: 'json',
        async: true,
        contentType: "application/json; charset=utf-8",
        success: function(data, status, jqXHR) {

            crimeList = data;

        },
        error: function(jqXHR, status, errorThrown) {
            // if fails 

            alert(jqXHR.responseText);
        }
    });
    // e.preventDefault();

}


function initMap() {

    var enteredPoint = {
        lat: -31.563910,
        lng: 147.154312
    };
    var uluru = {
        lat: -25.363,
        lng: 131.044
    };
    map = new google.maps.Map(document.getElementById('map'), {
        zoom: 10,
        center: enteredPoint
    });
    var marker = new google.maps.Marker({
        position: enteredPoint,
        icon: '/static/images/markers/3.png'
    });
    marker.setMap(map);
}



$(document).ready(function() {

    getCrimeList();

});


$('#search').on('click', function(event) {

    //initMap();

    var lat = $("#latitude").val();
    var lon = $("#longitude").val();
    if (lat !== '' && lon !== '')
        getNearCrimes(lat, lon);
    else
        alert('Latitude and Longitude cant be empty')


});