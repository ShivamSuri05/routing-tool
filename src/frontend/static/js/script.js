
var map = L.map('map').setView([51.1657, 10.4515], 6);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 18,
}).addTo(map);
let locationMarker = null;

map.on('click', function(e) {
    const lat = e.latlng.lat;
    const lng = e.latlng.lng;

    if (locationMarker) {
        map.removeLayer(locationMarker);
    }

    locationMarker = L.marker([lat, lng]).addTo(map)
        .bindPopup(`<strong>Latitude:</strong> ${lat}<br><strong>Longitude:</strong> ${lng}`)
        .openPopup();

    locationMarker.on('popupclose', function() {
        map.removeLayer(locationMarker);
        locationMarker = null;
    });
});

var markersGroup = L.layerGroup().addTo(map);

function createCustomIcon(color) {
    return L.icon({
        iconUrl: `../static/images/${color}_drop.png`,  // Use colored icons
        iconSize: [25, 25],
        iconAnchor: [12, 25],
        popupAnchor: [1, -34]
    });
}

function groupAndFilter(arr) {
    const grouped = {};

    // Step 1: Group by the third index
    arr.forEach(item => {
        const key = item[2]; // Grouping key (3rd index)
        if (!grouped[key]) grouped[key] = [];
        grouped[key].push(item);
    });

    //console.log(grouped)

    // Step 2: Filter each group to keep only items where the 4th index is 1
    const result = Object.values(grouped).map(group => group.filter(item => item[3] === 1));
    //console.log(result)

    return result.filter(group => group.length > 0); // Remove empty groups
}

function removeDuplicateSubarrays(arr) {
    const unique = new Set(arr.map(JSON.stringify)); // Convert subarrays to strings and store in a Set
    return Array.from(unique, JSON.parse); // Convert back to arrays
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

    if(response_coordinates.status == 412){
        alert("No Paths, Input is in wrong format");
    }
    if(response_numeric.status == 412){
        alert("No Paths, Input is in wrong format");
    }
    if(response_integer.status == 412){
        alert("No Paths, Input is in wrong format");
    }
    if(response.status == 409){
        alert("No Paths Found");
    }
    else {
        markersGroup.clearLayers();
        const json_response = await response.json();
        let paths = json_response.paths
        let lengths = json_response.lengths.map(num => (num/1000).toFixed(2))
        //console.log(lengths)

        var bounds = [];
        var colors = [
            'blue', 'green', 'yellow', 'purple', 'orange', 'pink', 
            'brown', 'cyan', 'magenta', 'lime', 'teal', 'indigo', 'gold', 'gray'
        ];
        paths.forEach((path, pathIndex) => {
            let markerColor = colors[pathIndex % colors.length]; // Ensure color cycles if more paths exist
            let pathLength = lengths[pathIndex]

            const startCoord = path[0];  // First coordinate
            const endCoord = path[path.length - 1];  // Last coordinate
            //console.log(startCoord);
            //console.log(endCoord);
            //const polylineCoords = path.slice(1, -1).map(coords => [coords[1][0], coords[1][1]]); // All except first & last
            const polylineCoords = removeDuplicateSubarrays(path.map(item => item.slice(0,2)));
            // Add Start Marker (Red)
            L.marker([startCoord[0], startCoord[1]], { icon: createCustomIcon('red') })
                .addTo(markersGroup)
                .bindPopup(`Start Point<br>Latitude: ${startCoord[0]}<br>Longitude: ${startCoord[1]}`);

            // Add End Marker (Green)
            L.marker([endCoord[0], endCoord[1]], { icon: createCustomIcon('green') })
                .addTo(markersGroup)
                .bindPopup(`End Point<br>Latitude: ${endCoord[0]}<br>Longitude: ${endCoord[1]}`);

            // Add Polyline for intermediate points
            let tempMarker = null;
            if (polylineCoords.length > 0) {
                const poly = L.polyline(polylineCoords, { color: markerColor, weight: 4 }).addTo(markersGroup);
                poly.on('mouseover', function(e) {
                    poly.setStyle({
                        color: 'black',  // Change color on hover
                        weight: 8,     // Increase weight on hover
                    });
                });

                // Reset path style on mouseout
                poly.on('mouseout', function(e) {
                    poly.setStyle({
                        color: markerColor,  // Reset to original color
                        weight: 4,           // Reset to original weight
                    });
                });
                
                poly.on('click', function(e) {
                    L.DomEvent.stopPropagation(e)
                    const lat = e.latlng.lat;
                    const lng = e.latlng.lng;
                    
                    if (tempMarker) {
                        map.removeLayer(tempMarker);
                    }
            
                    // Optionally, add a marker at the clicked point
                    tempMarker = L.marker([lat, lng]).addTo(map)
                        .bindPopup(`<strong>Latitude:</strong> ${lat} <br><strong>Longitude:</strong> ${lng} <br><strong>Total Length of whole path:</strong> ${pathLength} kms`)
                        .openPopup();
                    
                    tempMarker.on('popupclose', function() {
                        map.removeLayer(tempMarker);
                        tempMarker = null;
                    });
                });
            }
            
            const notMeasuredPaths = groupAndFilter(path);
            
            let mtempMarker = null;
            notMeasuredPaths.forEach((mpath)=>{
                polymcoords = removeDuplicateSubarrays(mpath.map(item => item.slice(0,2)));
                const mpoly = L.polyline(polymcoords, {color: 'red', weight: 6}).addTo(markersGroup);
                mpoly.on('mouseover', function(e) {
                    mpoly.setStyle({
                        color: 'yellow',  // Change color on hover
                        weight: 8,        // Increase weight on hover
                    });
                });

                // Reset path style on mouseout
                mpoly.on('mouseout', function(e) {
                    mpoly.setStyle({
                        color: 'red',     // Reset to red color
                        weight: 6,        // Reset to original weight
                    });
                });

                mpoly.on('click', function(e) {
                    const lat = e.latlng.lat;
                    const lng = e.latlng.lng;

                    if (mtempMarker) {
                        map.removeLayer(mtempMarker);
                    }
            
                    mtempMarker = L.marker([lat, lng]).addTo(map)
                        .bindPopup(`<strong>Latitude:</strong> ${lat} <br><strong>Longitude:</strong> ${lng}`)
                        .openPopup();
                    
                    mtempMarker.on('popupclose', function() {
                        map.removeLayer(mtempMarker);
                        mtempMarker = null;
                    });
                });
            })

            bounds.push([startCoord[0], startCoord[1]]);
            bounds.push([endCoord[0], endCoord[1]]);
        })
        
        if (bounds.length > 0) {
            map.fitBounds(bounds);
        }
    }
    //document.getElementById('response').innerText = result.message;
});


