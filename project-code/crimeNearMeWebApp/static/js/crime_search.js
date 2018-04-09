var map;
var markerCluster = [];
var bounds;
var crimeList;
var crimeData;
var inforwindow = {};
var zoomlevel = 13;
var marker;
var markerArray = {};
var checkBoxList = [];
var crimeListRvsd = [];
var markerClusterInit = true;
var radiusPara;
var crimeGraphsToggle = true;
var crimeByMonth = "";
var crimeByYear = "";
var totalData = true;
var count = 0;

function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: 41.8781136, lng: -87.62979819999998},
        zoom: zoomlevel
    });

    var card = document.getElementById('pac-card');
    var input = document.getElementById('pac-input');
    var types = document.getElementById('type-selector');
    var strictBounds = document.getElementById('strict-bounds-selector');

    map.controls[google.maps.ControlPosition.TOP_RIGHT].push(card);

    var autocomplete = new google.maps.places.Autocomplete(input);

    // Bind the map's bounds (viewport) property to the autocomplete object,
    // so that the autocomplete requests use the current map bounds for the
    // bounds option in the request.
    autocomplete.bindTo('bounds', map);

    var infowindow = new google.maps.InfoWindow();
    var infowindowContent = document.getElementById('infowindow-content');
    infowindow.setContent(infowindowContent);
    marker = new google.maps.Marker({
        map: map,
        anchorPoint: new google.maps.Point(0, -29)
    });

    autocomplete.addListener('place_changed', function () {
        infowindow.close();
        deleteMarkers();
        deleteMarkerCluster();
        marker.setVisible(false);
        var place = autocomplete.getPlace();
        if (!place.geometry) {
            // User entered the name of a Place that was not suggested and
            // pressed the Enter key, or the Place Details request failed.
            window.alert("No details available for input: '" + place.name + "'");
            return;
        }

        // If the place has a geometry, then present it on a map.
        if (place.geometry.viewport) {
            map.fitBounds(place.geometry.viewport);
        } else {
            map.setCenter(place.geometry.location);
            map.setZoom(zoomlevel);  // Why 17? Because it looks good.
        }
        marker.setPosition(place.geometry.location);
        marker.setVisible(true);
        var address = '';
        if (place.address_components) {
            address = [
                (place.address_components[0] && place.address_components[0].short_name || ''),
                (place.address_components[1] && place.address_components[1].short_name || ''),
                (place.address_components[2] && place.address_components[2].short_name || '')
            ].join(' ');
        }

        infowindowContent.children['place-icon'].src = place.icon;
        infowindowContent.children['place-name'].textContent = " Your Searched: " + place.name;
        infowindowContent.children['place-address'].textContent = address;
        infowindow.open(map, marker);

        //searching for nearBy crimes
        var radius = document.getElementById('pac-input-radius');
        //var locationStr = place.geometry.location.toString();
        var latMap = place.geometry.location.lat().toString();
        var longMap = place.geometry.location.lng().toString();
        radiusPara = radius.value;
        $("#legend").hide();
        getNearCrimes(latMap, longMap, radius.value);
        map.setCenter(place.geometry.location);
        //map.setZoom(zoomlevel);
        markerClusterInit = true;

    });

    // Sets a listener on a radio button to change the filter type on Places
    // Autocomplete.
    function setupClickListener(id, types) {
        var radioButton = document.getElementById(id);
        radioButton.addEventListener('click', function () {
            autocomplete.setTypes(types);
        });
    }

    setupClickListener('changetype-all', []);
    setupClickListener('changetype-address', ['address']);
    setupClickListener('changetype-establishment', ['establishment']);
    setupClickListener('changetype-geocode', ['geocode']);

    document.getElementById('use-strict-bounds')
        .addEventListener('click', function () {
            console.log('Checkbox clicked! New state=' + this.checked);
            autocomplete.setOptions({strictBounds: this.checked});
        });

    createGoogleMapButtons();
}

function getCrimeList() {

    var formURL = "/crimeList";

    $.ajax({
        url: formURL,
        type: "GET",
        dataType: 'json',
        async: true,
        contentType: "application/json; charset=utf-8",
        success: function (data, status, jqXHR) {
            crimeList = data;
        },
        error: function (jqXHR, status, errorThrown) {
            // if fails 
            alert(jqXHR.responseText);
        }
    });
    // e.preventDefault();
}

function getNearCrimes(latitude, longitude, radius) {

    var sendData = {
        "latitude": latitude,
        "longitude": longitude,
        "radius": radius
    };

    var formURL = "/crimeSearch";

    $.ajax({
        url: formURL,
        type: "POST",
        data: JSON.stringify(sendData),
        dataType: 'json',
        async: true,
        contentType: "application/json; charset=utf-8",
        success: function (data, status, jqXHR) {
            crimeData = data;
            deleteMarkers();
            checkBoxList = []
            bounds = new google.maps.LatLngBounds();
            var checkBoxStr = "";
            var legend = document.getElementById('legend');
            legend.innerHTML = "";
            var legendText = "<h3>Legend</h3>";

            legendText = legendText + "<div class='button-center'><input class='button-style' onclick='clearMarkers();' type=button value='Hide Markers'>"
                + "&nbsp<input class='button-style' onclick='showMarkers();' type=button value='Show Markers'></div>";
            //+ "<input onclick='deleteMarkers();' type=button value='Delete Markers'>";

            legendText = legendText + "<div class='button-center'><input class='button-style' onclick='clearMarkerCluster();' type=button value='Hide Clusters'>"
                + "&nbsp<input class='button-style' onclick='showMarkerCluster();' type=button value='Show Clusters'></div><br>";
            //+ "<input onclick='deleteMarkerCluster();' type=button value='Delete Clusters'>";

            for (var i = 0; i < crimeData.length; i++) {

                var contentString = '<div id="content">' +
                    '<div id="siteNotice">' +
                    '</div>' +
                    '<h1 id="firstHeading" class="firstHeading">' + crimeData[i].primary_description + '</h1>' +
                    '<div id="bodyContent">' +
                    '<b>Type</b>: ' + crimeData[i].primary_description + '<br>' +
                    '<b>Details</b>: ' + crimeData[i].secondary_description + '<br>' +
                    '<b>Block</b>: ' + crimeData[i].block + '<br>' +
                    '<b>Year</b>: ' + crimeData[i].year + '<br>' +
                    '<b>Arrested</b>: ' + crimeData[i].arrested + '<br>' +
                    '<b>Reported Date</b>: ' + crimeData[i].date + '<br>' +
                    '<b>GPS</b>: ' + crimeData[i].gps_location + '<br>' +
                    //'<b>Clusterded correct?</b>: ' + crimeData[i].clustered + '<br>' +
                    '</div>' +
                    '</div>';

                inforwindow[i] = new google.maps.InfoWindow({
                    content: contentString
                });

                var location = {
                    lat: parseFloat(crimeData[i].latitude),
                    lng: parseFloat(crimeData[i].longitude)
                };

                crimeObj = crimeList[crimeData[i].primary_description];

                if (checkBoxList[crimeObj[0]] !== true) {

                    crimeListRvsd[crimeObj[0]] = crimeObj[1];
                    checkBoxList[crimeObj[0]] = true;

                    legendText = legendText + "<div><img src='" + '/static/images/markers/' + crimeObj[0] + '.png' + "'> ";
                    legendText = legendText + "<label class='container'>:<input type='checkbox' checked='checked' class='checkbox-cls' id='" + (crimeObj[0]).toString() + "'> </label>";
                    legendText = legendText + crimeObj[1].toString() + "</div>";

                }


                var icon = {
                    url: '/static/images/markers/' + crimeObj[0] + '.png', // url : image size is 32x32
                    scaledSize: new google.maps.Size(30, 30), // scaled size
                    origin: new google.maps.Point(0, 0), // origin
                    anchor: new google.maps.Point(0, 0) // anchor
                };

                var markerr;

                if (parseFloat(radiusPara) <= 0.1) {
                    markerr = new google.maps.Marker({
                        position: location,
                        icon: icon,
                        //label: crimeObj[0].toString(),
                        title: crimeData[i].primary_description,
                        animation: google.maps.Animation.DROP
                    });
                } else {

                    markerr = new google.maps.Marker({
                        position: location,
                        icon: icon,
                        //label: crimeObj[0].toString(),
                        title: crimeData[i].primary_description
                    });

                }

                markerr.set("id", i);
                markerr.set("primary_id", crimeObj[1]);
                //markerr.set("objectRef", markerr);
                //markerr.setMap(map);
                markerr.addListener('click', function (event) {
                    var clickedMarker = this;
                    toggleBounce(clickedMarker);
                    inforwindow[this.get("id")].open(map, clickedMarker);
                    window.setTimeout(function () {
                        toggleBounce(clickedMarker);
                    }, 3000);
                });

                bounds.extend(location);
                markerArray[i] = markerr;
            }
            setMapOnAllMarkers(map)
            map.fitBounds(bounds);


            legend.innerHTML = legendText;
            //map.controls[google.maps.ControlPosition.RIGHT_BOTTOM].push(legend);
            $("#legend").show();
            $(".checkbox-cls").click(function (event) {
                // Holds the product ID of the clicked element
                var id = event.target.id;
                var comName = crimeListRvsd[id];
                if ($(this).prop('checked') == true)
                    setMapOnSelectedMarkers(map, comName);
                else
                    unSetMapOnSelectedMarkers(comName);
            });
            get_crimeByMonth();
            get_crimeByYear();

        },
        error: function (jqXHR, status, errorThrown) {
            // if fails 
            alert(jqXHR.responseText);
        }
    });
    // e.preventDefault();

}

//Marker toggle bounce
function toggleBounce(marker) {
    if (marker.getAnimation() !== null) {
        marker.setAnimation(null);
    } else {
        marker.setAnimation(google.maps.Animation.BOUNCE);
    }
}


// Sets the map on all markers in the array.
function setMapOnAllMarkers(map) {
    for (var i = 0; i < markerArray.length; i++) {
        markerArray[i].setAnimation(null);
        if (parseFloat(radiusPara) <= 0.1) {
            markerArray[i].setAnimation(google.maps.Animation.DROP);
        }
        markerArray[i].setMap(map);
    }
}

function unSetMapOnSelectedMarkers(descriptionMarker) {
    for (var i = 0; i < markerArray.length; i++) {
        if (markerArray[i].get("primary_id") === descriptionMarker)
            markerArray[i].setMap(null);
    }
}

function setMapOnSelectedMarkers(map, descriptionMarker) {
    for (var i = 0; i < markerArray.length; i++) {
        if (markerArray[i].get("primary_id") === descriptionMarker)
            markerArray[i].setMap(map);
    }
}

// Removes the markers from the map, but keeps them in the array.
function clearMarkers() {
    $('.checkbox-cls').prop('checked', false);
    setMapOnAllMarkers(null);
}

// Shows any markers currently in the array.
function showMarkers() {
    $('.checkbox-cls').prop('checked', true);
    setMapOnAllMarkers(map);
}

// Deletes all markers in the array by removing references to them.
function deleteMarkers() {
    clearMarkers();
    markerArray = [];
}

//Turn on all marker clusters
function setMapOnAllMarkerClusters(status) {
    for (var i = 0; i < markerCluster.length; i++) {
        if (status)
            markerCluster[i].addMarkers(markerArray);
        else
            markerCluster[i].clearMarkers();
    }
    //refreshMap();

}

//clear all maker clusters
function clearMarkerCluster() {
    setMapOnAllMarkerClusters(null, false);
}

// Shows all marker clsuters.
function showMarkerCluster() {
    if (markerClusterInit) {
        markerClusterInit = false;
        initMarkerClusters();
    }
    setMapOnAllMarkerClusters(map, true);
}

// Deletes all marker clsuters.
function deleteMarkerCluster() {
    clearMarkerCluster();
    markerCluster = [];
}

// Refresh Map.
function refreshMap() {
    map.setZoom(map.getZoom() + 1);
    map.setZoom(map.getZoom() - 1);
}

function hideClustersShowMarkers() {
    clearMarkerCluster();
    showMarkers();
}

function hideMarkersShowClusters() {
    clearMarkers();
    showMarkerCluster();
}

function initMarkerClusters() {
    markerCluster[0] = new MarkerClusterer(map, markerArray, {imagePath: '/static/images/m'});
}

function createGoogleMapButtons() {

    var centerControlDiv = document.createElement('div');
    var centerControl = new CenterControl(centerControlDiv, map);

    centerControlDiv.index = 1;
    map.controls[google.maps.ControlPosition.LEFT_BOTTOM].push(centerControlDiv);
}

function CenterControl(controlDiv, map) {

    // Set CSS for the control border.
    var controlUI = document.createElement('div');
    controlUI.id = "google-map-Buttons";
    controlUI.title = 'Click to the load the crime analysis';
    controlDiv.appendChild(controlUI);

    // Set CSS for the control interior.
    var controlText = document.createElement('div');

    controlText.id = "google-map-Buttons-text";
    controlText.innerHTML = 'Show Graphs';
    controlUI.appendChild(controlText);

    // Setup the click event listeners:
    controlUI.addEventListener('click', function () {
        var crimePannel = document.getElementById("floating-panel");
        var controlText = document.getElementById('google-map-Buttons-text');
        if (crimeGraphsToggle) {

            $("#floating-panel").show(500);
            controlText.innerHTML = "Hide Graphs";
            crimeGraphsToggle = false;

        } else {
            $("#floating-panel").hide(500);
            controlText.innerHTML = 'Show Graphs';
            crimeGraphsToggle = true;
            document.getElementById("graphdiv2").innerHTML = "";
        }

        if (count == 0) {
            window.setTimeout(loadGraphsTotal, 550);
            totalData = false;
            document.getElementById("graphdiv2-btn").value = "Analyze search result";
        } else {
            if (crimeByMonth !== "") {
                window.setTimeout(loadGraphs, 550);
                totalData = true;
                document.getElementById("graphdiv2-btn").value = "Analyze complete data set";
            } else
                alert("Please search crimes first!");

        }
    });

}

var g1;
var g2;
var g3;
var g4;
var g5;
var graph5Height;

function loadGraphs() {

    document.getElementById("graphdiv3").innerHTML = "";
    graph5Height = document.getElementById("graphdiv3").style.height;
    $("#graphdiv3").animate({
        height: 0
    }, 600);

    Crime_data_Split = crimeByMonth;//.split('\n').slice(0, 20).join('\n');
    Crime_data_Split2 = crimeByYear;//.split('\n').slice(0, 20).join('\n');
    g1 = new Dygraph(
        document.getElementById("graphdiv1"),
        Crime_data_Split,  //"/static/data/bargraph.csv", // path to CSV file
        {
            rollPeriod: 7,
            showRoller: true,
            title: 'Top 10 Crimes Near you by month',
            ylabel: 'No of Crimes',
            xlabel: 'Time',
            legend: 'always',
            animatedZooms: true
        }          // options
    );
    g2 = new Dygraph(
        document.getElementById("graphdiv2"),
        Crime_data_Split2,
        {
            includeZero: true,
            rollPeriod: 7,
            showRoller: true,
            title: 'Top 10 Crimes Near you by year',
            ylabel: 'No of Crimes',
            xlabel: 'Time',
            legend: 'always',
            animatedZooms: true,
            plotter: multiColumnBarPlotter
        });


}

function loadGraphsTotal() {

    $("#graphdiv3").css({
        height: graph5Height
    });

    g3 = new Dygraph(
        document.getElementById("graphdiv1"),
        "/static/data/crimeByMonthVsArrested.csv", // path to CSV file
        {
            includeZero: true,
            rollPeriod: 7,
            showRoller: true,
            title: 'Total Crimes by time',
            //ylabel: 'No of Crimes',
            xlabel: 'Time',
            legend: 'always',
            animatedZooms: true
        }          // options
    );

    g4 = new Dygraph(
        document.getElementById("graphdiv2"),
        "/static/data/crimeByType.csv",
        {
            //legend: 'always',
            rollPeriod: 7,
            showRoller: true,
            title: 'Total Crimes by types',
            //ylabel: 'No of Crimes',
            xlabel: 'Crime Types',
            includeZero: false,
            animatedZooms: true,
            plotter: multiColumnBarPlotter2,
            axes: {
                x: {
                    drawGrid: false,
                    drawAxis: false
                }
            }

        }
    );
    g5 = new Dygraph(
        document.getElementById("graphdiv3"),
        "/static/data/crimeByLocation.csv",
        {
            //legend: 'always',
            rollPeriod: 7,
            showRoller: true,
            title: 'Total Crimes by locations',
            //ylabel: 'No of Crimes',
            xlabel: 'Crime Locations',
            includeZero: false,
            animatedZooms: true,
            plotter: multiColumnBarPlotter2,
            axes: {
                x: {
                    drawGrid: false,
                    drawAxis: false
                }
            }

        }
    );
    /*
      g3 = new Dygraph(
          document.getElementById("graphdiv1"),
          "/static/data/crimeByType.csv", // path to CSV file
          {
              includeZero: true,
              rollPeriod: 7,
              showRoller: true,
              title: 'Total Crimes by types',
              ylabel: 'No of Crimes',
              xlabel: 'Crime Types',
              legend: 'always',
              animatedZooms: true,
              plotter: multiColumnBarPlotter
          }          // options
      );
      g4 = new Dygraph(
          document.getElementById("graphdiv2"),
          "/static/data/crimeByLocation.csv", // path to CSV file
          {
              includeZero: true,
              rollPeriod: 7,
              showRoller: true,
              title: 'Total Crimes by location',
              ylabel: 'No of Crimes',
              xlabel: 'Location',
              legend: 'always',
              animatedZooms: true,
              plotter: multiColumnBarPlotter
          });
  */
}

function unzoomGraphs() {
    if (totalData) {
        if (crimeByMonth !== "") {
            g1.updateOptions({
                dateWindow: null,
                valueRange: null
            });
            g2.updateOptions({
                dateWindow: null,
                valueRange: null
            });
        }
    } else {
        g3.updateOptions({
            dateWindow: null,
            valueRange: null
        });
        g4.updateOptions({
            dateWindow: null,
            valueRange: null
        });
        g5.updateOptions({
            dateWindow: null,
            valueRange: null
        });
    }
}

function totalDataGraphs() {

    if (totalData) {
        loadGraphsTotal();
        totalData = false;
        count = 0;
        document.getElementById("graphdiv2-btn").value = "Analyze search result";

    } else {
        if (crimeByMonth !== "") {
            loadGraphs();
            totalData = true;
            count = 1;
            document.getElementById("graphdiv2-btn").value = "Analyze complete data set";
        } else
            alert("Please search crimes first!");

    }


}

// This function draws bars for a single series. See
// multiColumnBarPlotter below for a plotter which can draw multi-series
// bar charts.
function barChartPlotter(e) {
    var ctx = e.drawingContext;
    var points = e.points;
    var y_bottom = e.dygraph.toDomYCoord(0);

    ctx.fillStyle = darkenColor(e.color);

    // Find the minimum separation between x-values.
    // This determines the bar width.
    var min_sep = Infinity;
    for (var i = 1; i < points.length; i++) {
        var sep = points[i].canvasx - points[i - 1].canvasx;
        if (sep < min_sep) min_sep = sep;
    }
    var bar_width = Math.floor(2.0 / 3 * min_sep);

    // Do the actual plotting.
    for (var i = 0; i < points.length; i++) {
        var p = points[i];
        var center_x = p.canvasx;

        ctx.fillRect(center_x - bar_width / 2, p.canvasy,
            bar_width, y_bottom - p.canvasy);

        ctx.strokeRect(center_x - bar_width / 2, p.canvasy,
            bar_width, y_bottom - p.canvasy);
    }
}


// Multiple column bar chart
function multiColumnBarPlotter(e) {
    // We need to handle all the series simultaneously.
    if (e.seriesIndex !== 0) return;

    var g = e.dygraph;
    var ctx = e.drawingContext;
    var sets = e.allSeriesPoints;
    var y_bottom = e.dygraph.toDomYCoord(0);

    // Find the minimum separation between x-values.
    // This determines the bar width.
    var min_sep = Infinity;
    for (var j = 0; j < sets.length; j++) {
        var points = sets[j];
        for (var i = 1; i < points.length; i++) {
            var sep = points[i].canvasx - points[i - 1].canvasx;
            if (sep < min_sep) min_sep = sep;
        }
    }
    var bar_width = Math.floor(2.0 / 3 * min_sep);

    var fillColors = [];
    var strokeColors = g.getColors();
    for (var i = 0; i < strokeColors.length; i++) {
        fillColors.push(darkenColor(strokeColors[i]));
    }

    for (var j = 0; j < sets.length; j++) {
        ctx.fillStyle = fillColors[j];
        ctx.strokeStyle = strokeColors[j];
        for (var i = 0; i < sets[j].length; i++) {
            var p = sets[j][i];
            var center_x = p.canvasx;
            var x_left = center_x - (bar_width / 2) * (1 - j / (sets.length - 1));

            ctx.fillRect(x_left, p.canvasy,
                bar_width / sets.length, y_bottom - p.canvasy);

            ctx.strokeRect(x_left, p.canvasy,
                bar_width / sets.length, y_bottom - p.canvasy);
        }
    }
}

// Multiple column bar chart
function multiColumnBarPlotter2(e) {
    // We need to handle all the series simultaneously.
    if (e.seriesIndex !== 0) return;

    var g = e.dygraph;
    var ctx = e.drawingContext;
    var sets = e.allSeriesPoints;
    var y_bottom = e.dygraph.toDomYCoord(0);

    // Find the minimum separation between x-values.
    // This determines the bar width.
    var min_sep = Infinity;//516
    for (var j = 0; j < sets.length; j++) {
        var points = sets[j];
        for (var i = 1; i < points.length; i++) {
            var sep = points[i].canvasx - points[i - 1].canvasx;
            if (sep < min_sep) min_sep = sep;
        }
    }
    //alert(min_sep);

    //adjust this to change the initial position
    var bar_width = Math.floor(2.0 * 15 / 16 * min_sep);

    var fillColors = [];
    var strokeColors = g.getColors();
    for (var i = 0; i < strokeColors.length; i++) {
        fillColors.push(darkenColor(strokeColors[i]));
    }

    for (var j = 0; j < sets.length; j++) {
        ctx.fillStyle = fillColors[j];
        ctx.strokeStyle = strokeColors[j];
        for (var i = 1; i < sets[j].length; i++) {
            var p = sets[j][i];
            var setsLen = sets.length;
            var center_x = p.canvasx;
            var x_left = center_x - (bar_width / 2) * (1 - j / (sets.length - 1));

            ctx.fillRect(x_left, p.canvasy,
                bar_width / sets.length, y_bottom - p.canvasy);

            ctx.strokeRect(x_left, p.canvasy,
                bar_width / sets.length, y_bottom - p.canvasy);


        }
    }
}

// Darken a color
function darkenColor(colorStr) {
    // Defined in dygraph-utils.js
    var color = Dygraph.toRGB_(colorStr);
    color.r = Math.floor((255 + color.r) / 2);
    color.g = Math.floor((255 + color.g) / 2);
    color.b = Math.floor((255 + color.b) / 2);
    return 'rgb(' + color.r + ',' + color.g + ',' + color.b + ')';
}

function get_crimeByMonth() {

    var formURL = "/crimeByMonth";
    crimeByDate = "";
    $.ajax({
        url: formURL,
        type: "GET",
        dataType: 'json',
        async: true,
        contentType: "application/json; charset=utf-8",
        success: function (data, status, jqXHR) {
            crimeByMonth = data;
        },
        error: function (jqXHR, status, errorThrown) {
            // if fails 
            alert(jqXHR.responseText);
        }
    });
    // e.preventDefault();
}

function get_crimeByYear() {

    var formURL = "/crimeByYear";
    crimeByYear = "";
    $.ajax({
        url: formURL,
        type: "GET",
        dataType: 'json',
        async: true,
        contentType: "application/json; charset=utf-8",
        success: function (data, status, jqXHR) {
            crimeByYear = data;
        },
        error: function (jqXHR, status, errorThrown) {
            // if fails 
            alert(jqXHR.responseText);
        }
    });
    // e.preventDefault();
}

$(document).ready(function () {
    $("#legend").hide();
    $("#floating-panel").hide();
    //initMap();
    getCrimeList();
});
