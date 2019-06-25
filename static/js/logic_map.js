function buildMap() {
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

    var link = "/gz_2010_us_040_00_20m";

    // Grabbing our GeoJSON data..
    d3.json(link, function(data) {
          // Creating a GeoJSON layer with the retrieved datas
          L.geoJson(data).addTo(map);
    });

    
    var cancerData = "/api/incidence";

    function chooseColor(num) {
        num = parseInt(num);
        if (num<1000) {
            return "yellow";
            }
        else {
            console.log(num);
            return "black";
            }
        }     


    // Grabbing our GeoJSON data..
    d3.json(cancerData, function(data){
        
    var state_incident = {};
    console.log(data);
        
    data.forEach(row => state_incident[row.State] = row["Brain cancer incidence"])
    console.log(state_incident);
    
    d3.json(link, function(data){
    // Creating a geoJSON layer with the retrieved data
      L.geoJson(data, {
        // Style each feature (in this case a neighborhood)
        style: function(feature) {
          return {
            color: "white",
            // Call the chooseColor function to decide which color to color our neighborhood (color based on borough)
            fillColor: chooseColor(state_incident[feature.properties.NAME]),
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
}


function init() {
    buildMap();
}

init();
