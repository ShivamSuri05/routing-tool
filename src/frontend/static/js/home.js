function AdvancedOptionsToggle() {
    const bufferRow = document.getElementById("buffer-height-row");
    if (bufferRow.style.display === "none" || bufferRow.style.display === "") {
        bufferRow.style.display = "table-row"; // Show the row
    } else {
        bufferRow.style.display = "none"; // Hide the row
    }
    const pathRow = document.getElementById("num-paths-row");
    if (pathRow.style.display === "none" || pathRow.style.display === "") {
        pathRow.style.display = "table-row"; // Show the row
    } else {
        pathRow.style.display = "none"; // Hide the row
    }
}

function populateDropdown(dropdown, data) {
    dropdown.innerHTML = '';  
    const defaultOption = document.createElement('option');
    defaultOption.text = 'Select a city';
    defaultOption.value = '';
    dropdown.appendChild(defaultOption);
    data.forEach(function(pair) {
        const name = pair[0];
        const coord = pair[1];
        const option = document.createElement('option');
        option.value = coord; 
        option.textContent = name;  
        dropdown.appendChild(option);
    });
}
document.addEventListener('DOMContentLoaded', function() {
    
    fetch('/dropdown_data')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();  
        })
        .then(data => {
            populateDropdown(document.getElementById('start_dropdown'), data.start_name_coord_pairs);
            populateDropdown(document.getElementById('end_dropdown'), data.end_name_coord_pairs);

            const start_city = document.getElementById('start_dropdown');
            const end_city = document.getElementById('end_dropdown');

            start_city.addEventListener('change', function() {
            const selectedOption = start_city.options[start_city.selectedIndex]; // Get selected option
            const coordinates = selectedOption.value; // Get coordinates from option value
            document.getElementById('start').value = coordinates; // Set coordinates to the start input field
            });

            end_city.addEventListener('change', function() {
                const selectedOption = end_city.options[end_city.selectedIndex]; // Get selected option
                const coordinates = selectedOption.value; // Get coordinates from option value
                document.getElementById('dest').value = coordinates; // Set coordinates to the destination input field
            });
        })
        .catch(error => {
            console.error('Error fetching data:', error);
        });
});


function OnOverviewClick() {
    // Placeholder function for Overview
}

function OnInformationClick() {
    // Placeholder function for Information
}

function OnContactClick() {
    // Placeholder function for Contact Us
}

function OnHelpClick() {
    // Placeholder function for Help
}

function OnSearchClick() {
    // Placeholder function for Search
}

function OnResetClick() {
    // Placeholder function for Rest
}