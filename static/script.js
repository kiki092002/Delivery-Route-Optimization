document.getElementById('route-form').addEventListener('submit', function(event) {
    event.preventDefault();

    let start = document.getElementById('start').value;
    let end = document.getElementById('end').value;

    fetch('/optimize', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ start: start, end: end })
    })
    .then(response => response.json())
    .then(data => {
        let resultDiv = document.getElementById('result');
        resultDiv.textContent = `Cost: ${data.cost}, Path: ${data.path.join(' -> ')}`;
        resultDiv.style.display = 'block';
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
