// Creating map object
var map = L.map("map", {
      center: [38.0748599,-94.5554788],
      zoom: 4.48,
//      layers: [cancers]
});

// Adding tile layer
L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
      attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
      maxZoom: 18,
      id: "mapbox.streets",
      accessToken: API_KEY
}).addTo(map);

var link = "gz_2010_us_040_00_20m.json";

// Grabbing our GeoJSON data..
d3.json(link, function(data) {
      // Creating a GeoJSON layer with the retrieved datas
      L.geoJson(data).addTo(map);
});

var states = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado",
  "Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois",
  "Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
  "Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana",
  "Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York",
  "North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
  "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah",
  "Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]

var statesOccurrence = {"Alabama":1000,"Alaska":1000,"Arizona":1000,"Arkansas":1000,"California":8000,"Colorado":1000,
  "Connecticut":1000,"Delaware":1000,"Florida":1000,"Georgia":1000,"Hawaii":1000,"Idaho":1000,"Illinois":1000,
  "Indiana":1000,"Iowa":1000,"Kansas":1000,"Kentucky":1000,"Louisiana":1000,"Maine":1000,"Maryland":1000,
  "Massachusetts":1000,"Michigan":1000,"Minnesota":1000,"Mississippi":1000,"Missouri":1000,"Montana":1000,
  "Nebraska":1000,"Nevada":1000,"New Hampshire":1000,"New Jersey":1000,"New Mexico":1000,"New York":1000,
  "North Carolina":1000,"North Dakota":1000,"Ohio":1000,"Oklahoma":1000,"Oregon":1000,"Pennsylvania":1000,
  "Rhode Island":1000,"South Carolina":1000,"South Dakota":1000,"Tennessee":1000,"Texas":1000,"Utah":1000,
  "Vermont":1000,"Virginia":1000,"Washington":1000,"West Virginia":1000,"Wisconsin":1000,"Wyoming":1000}



function chooseColor(NAME) {
  switch (statesOccurrence[NAME]) {
      case 1000:
        return "yellow";
      default:
        return "black";
  }
}

// Grabbing our GeoJSON data..
d3.json(link, function(data) {
  // Creating a geoJSON layer with the retrieved data
  L.geoJson(data, {
    // Style each feature (in this case a neighborhood)
    style: function(feature) {
      return {
        color: "white",
        // Call the chooseColor function to decide which color to color our neighborhood (color based on borough)
        fillColor: chooseColor(feature.properties.NAME),
        fillOpacity: 0.5,
        weight: 1.5
      };
    },
    // Called on each feature
    onEachFeature: function(feature, layer) {
      // Set mouse events to change map styling
      layer.on({
        // When a user's mouse touches a map feature, the mouseover event calls this function, that feature's opacity changes to 90% so that it stands out
        mouseover: function(event) {
          layer = event.target;
          layer.setStyle({
            fillOpacity: 0.9
          });
        },
        // When the cursor no longer hovers over a map feature - when the mouseout event occurs - the feature's opacity reverts back to 50%
        mouseout: function(event) {
          layer = event.target;
          layer.setStyle({
            fillOpacity: 0.5
          });
        },
        // When a feature (neighborhood) is clicked, it is enlarged to fit the screen
        click: function(event) {
          map.fitBounds(event.target.getBounds());
        }
      });
      // Giving each feature a pop-up with information pertinent to it
      layer.bindPopup("<h1>" + feature.properties.NAME + "</h1> <hr> <h2>" + feature.properties.NAME + "</h2>");

    }
  }).addTo(map);
});


// add legend
var legend = L.control({position: 'bottomright'});

legend.onAdd = function (map) {

    var div = L.DomUtil.create('div', 'info legend'),
        limits = [0, 2000, 4000, 6000, 8000, 10000],
        colors = ["#FFE400", "#FFB200", "#FF8000", "#FF6100", "#FF2A00", "red"],
        labels = [];

    // loop through our density intervals and generate a label with a colored square for each interval
    for (var i = 0; i < limits.length; i++) {
        div.innerHTML +=
            '<i style="background:' + colors[i] + '"></i> ' +
            limits[i] + (limits[i + 1] ? '&ndash;' + limits[i + 1] + '<br>' : '+');
    }

    return div;
};

legend.addTo(map);

// add info
var info = L.control();

info.onAdd = function (map) {
    this._div = L.DomUtil.create('div', 'info'); // create a div with a class "info"
    this.update();
    return this._div;
};

// method that we will use to update the control based on feature properties passed
info.update = function (props) {
    this._div.innerHTML = '<h4>US Cancer Occurrence</h4>';
};

info.addTo(map);
