var dxcord = 84.4; var dycord = 28.48; var mapzoomlevel=7; 

var map = L.map('map').setView([dycord, dxcord],mapzoomlevel);

		L.tileLayer('http://{s}.tile.cloudmade.com/{key}/22677/256/{z}/{x}/{y}.png', {
			attribution: 'Yomari Code Camp 2014',
			key: 'BC9A493B41014CAABB98F0471D759707'
		}).addTo(map);


function highlightFeature(e) {
    var layer = e.target;

    layer.setStyle({
        weight: 2,
        color: '#bbb',
        dashArray: '',
        fillOpacity: 0.7
    });

    if (!L.Browser.ie && !L.Browser.opera) {
        layer.bringToFront();
    }
    info.update(layer.feature.properties["Name"]);
}
function resetHighlight(e) {
    geojson.resetStyle(e.target);
    info.update();
}
function zoomToFeature(e) {
    map.fitBounds(e.target.getBounds());
}

function onEachFeature(feature, layer) {
    layer.on({
        // mouseover: highlightFeature,
        dblclick: highlightFeature,
        // mouseout: resetHighlight,
        click: zoomToFeature
    });
}


function getColor(d, t) {
    if (d>=300){
        map.fitBounds(t.getBounds());
        return '#ff0000';
}
        /*d > 15 ? '#99000d' :
           d > 10  ? '#cb181d' :
           d > 5  ? '#ef3b2c' :
           d > 1  ? '#fb6a4a' :
           /*d > 5   ? '#fc9272' :
           d > 3   ? '#fcbba1' :
           d > 1   ? '#fee0d2' : */
     return                 '#fff5f0';
    // return 'rgb(' + 255/d + "," + 155/d + "," + 255/d + "," + ')'; 
}



function style(feature, t) {
    return {
        fillColor: getColor(data[cfl(feature.properties.Name)],t),
        weight: 1.5,
        opacity: 1,
        color: 'black',
        dashArray: '3',
        fillOpacity: 0.7
    };
}
function cfl(string)
{
	string = string.toLowerCase();
    return string.charAt(0).toUpperCase() + string.slice(1);
}

var info = L.control();

info.onAdd = function (map) {
    this._div = L.DomUtil.create('div', 'info'); // create a div with a class "info"
    this.update();
    return this._div;
};

// method that we will use to update the control based on feature properties passed
info.update = function (props) {
    // alert(props);
    // console.log(props);
    this._div.innerHTML = '<h4>'+(props?props:'DISTRICT')+'</h4>' + ( (props) ?
        'Infected-critical' + ': <b>' + data[ cfl(props) ] + '</b><br />'+
        'Deaths' + ':<b>' + dead + '</b><br />'+
        'Recovered' + ':<b>' + recovered + '</b><br />'       
        : 'Double Click');
};

info.addTo(map);

var geojson = L.geoJson(districtmap, {style: style, onEachFeature: onEachFeature}).addTo(map);