console.log("Hello World")
document.getElementById('dataForm').addEventListener('click', async (event) => {
    event.preventDefault();

    const start_city = document.getElementById('start').value;
    const end_city = document.getElementById('dest').value;
    const height = document.getElementById('height').value;
    const buffer_ht = document.getElementById('buffer-height').value;
    let body_data = {
        start_city: start_city,
        end_city: end_city,
        height: height,
        buffer_ht: buffer_ht
    }
    const response = await fetch('/getRoute', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(body_data)
    })
    const result = await response.json();
    console.log(result)
    alert(result)
    //document.getElementById('response').innerText = result.message;
});


