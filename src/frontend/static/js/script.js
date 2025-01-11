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
        alert("No Path Found for desired vehicle height");
    }
    else {
        markersGroup.clearLayers();
        const paths = await response.json();
        console.log(paths)

        var bounds = [];
        var colors = ['blue', 'green', 'black', 'yellow', 'red']
        paths.forEach((path, pathIndex) => {
            markerColor = colors[pathIndex];
            for (const [id, coords] of Object.entries(path)) {
                lat = coords[1][0]
                longi = coords[1][1]
                node_id = coords[0]
                L.marker([lat, longi], { icon: createCustomIcon(markerColor) })
                    .addTo(markersGroup)
                    .bindPopup(`Node ID: ${node_id}\nLatitude: ${lat}\nLongitude: ${longi}`);
            
                bounds.push([lat, longi]);
            }
        })
        
        if (bounds.length > 0) {
            map.fitBounds(bounds);
        }
    }
    //document.getElementById('response').innerText = result.message;
});


