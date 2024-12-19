console.log("Hello World")
document.getElementById('dataForm').addEventListener('submit', async (event) => {
    event.preventDefault();

    const inputData = document.getElementById('inputData').value;
    const response = await fetch('/process', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ data: inputData }),
    });

    const result = await response.json();
    document.getElementById('response').innerText = result.message;
});


