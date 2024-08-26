// scripts.js
document.addEventListener('DOMContentLoaded', () => {
    const apiKey = 'pk.36be7313614284d35fabb38322ef6053';
    const startingPointInput = document.querySelector('#starting-point');
    const destinationInput = document.querySelector('#destination');
    const startingPointResults = document.querySelector('#starting-point-results');
    const destinationResults = document.querySelector('#destination-results');

    function fetchSuggestions(query, callback) {
        fetch(`https://us1.locationiq.com/v1/search.php?key=${apiKey}&q=${encodeURIComponent(query)}&format=json`)
            .then(response => response.json())
            .then(data => {
                callback(data);
            })
            .catch(error => console.error('Error:', error));
    }

    function showResults(results, container) {
        container.innerHTML = '';
        results.forEach(result => {
            const li = document.createElement('li');
            li.textContent = result.display_name;
            li.addEventListener('click', () => {
                if (container === startingPointResults) {
                    startingPointInput.value = result.display_name;
                } else {
                    destinationInput.value = result.display_name;
                }
                container.innerHTML = '';
            });
            container.appendChild(li);
        });
    }

    startingPointInput.addEventListener('input', () => {
        const query = startingPointInput.value;
        if (query.length > 2) {
            fetchSuggestions(query, data => showResults(data, startingPointResults));
        }
    });

    destinationInput.addEventListener('input', () => {
        const query = destinationInput.value;
        if (query.length > 2) {
            fetchSuggestions(query, data => showResults(data, destinationResults));
        }
    });
});