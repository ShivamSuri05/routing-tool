console.log("Hello World")
var map = L.map('map').setView([51.1657, 10.4515], 6);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 18,
}).addTo(map);
var markersGroup = L.layerGroup().addTo(map);

function createCustomIcon(color) {
    return L.icon({
        iconUrl: `../static/images/${color}_drop.png`,  // Use colored icons
        iconSize: [25, 25],
        iconAnchor: [12, 25],
        popupAnchor: [1, -34]
    });
}

document.getElementById('dataForm').addEventListener('click', async (event) => {
    event.preventDefault();

    const start_city = document.getElementById('start').value;
    const end_city = document.getElementById('dest').value;
    const height = document.getElementById('height').value;
    const buffer_ht = document.getElementById('buffer-height').value;
    const num_paths = document.getElementById('num-paths').value;
    let body_data = {
        start_city: start_city,
        end_city: end_city,
        height: height,
        buffer_ht: buffer_ht,
        num_paths: num_paths
    }
    const spinner = document.getElementById('spinner');
    spinner.style.display = 'block'
    const spinner_background = document.getElementById('spinner-background')
    spinner_background.style.display = 'block'
    const response = await fetch('/getRoute', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(body_data)
    })

    spinner.style.display = 'none';
    spinner_background.style.display = 'none';

    if(response.status == 409){
        alert(response.message);
    }
    else {
        markersGroup.clearLayers();
        const paths = await response.json();
        //console.log(paths)

        var bounds = [];
        var colors = [
            'blue', 'green', 'black', 'yellow', 'red', 'purple', 'orange', 'pink', 
            'brown', 'cyan', 'magenta', 'lime', 'teal', 'indigo', 'gold', 'gray'
        ];
        paths.forEach((path, pathIndex) => {
            let markerColor = colors[pathIndex % colors.length]; // Ensure color cycles if more paths exist

            const startCoord = path[0];  // First coordinate
            const endCoord = path[path.length - 1];  // Last coordinate
            //console.log(startCoord);
            //console.log(endCoord);
            //const polylineCoords = path.slice(1, -1).map(coords => [coords[1][0], coords[1][1]]); // All except first & last
            const polylineCoords = path
            // Add Start Marker (Red)
            L.marker([startCoord[0], startCoord[1]], { icon: createCustomIcon('red') })
                .addTo(markersGroup)
                .bindPopup(`Start Point<br>Latitude: ${startCoord[0]}<br>Longitude: ${startCoord[1]}`);

            // Add End Marker (Green)
            L.marker([endCoord[0], endCoord[1]], { icon: createCustomIcon('green') })
                .addTo(markersGroup)
                .bindPopup(`End Point<br>Latitude: ${endCoord[0]}<br>Longitude: ${endCoord[1]}`);

            // Add Polyline for intermediate points
            if (polylineCoords.length > 0) {
                L.polyline(polylineCoords, { color: markerColor, weight: 4 }).addTo(markersGroup);
            }

            bounds.push([startCoord[0], startCoord[1]]);
            bounds.push([endCoord[0], endCoord[1]]);
        })
        
        if (bounds.length > 0) {
            map.fitBounds(bounds);
        }
    }
    //document.getElementById('response').innerText = result.message;
});


