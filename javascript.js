// maps.js
document.addEventListener('DOMContentLoaded', function() {
    const mapsData = [
        { src: 'maps/map0.html', title: 'Day 1' },
        { src: 'maps/map1.html', title: 'Day 2' },
        { src: 'maps/map2.html', title: 'Day 3' },
        { src: 'maps/map3.html', title: 'Day 4' },
        { src: 'maps/map4.html', title: 'Day 5' },
        { src: 'maps/map5.html', title: 'Day 6' },
        { src: 'maps/map6.html', title: 'Day 7' }
    ];

    let currentIndex = 0;
    let intervalId;

    function updateMap() { 
        const titleContainer = document.getElementById('map-title-container');
        titleContainer.innerHTML = `<h2>${mapsData[currentIndex].title}</h2>`;

        const mapContainer = document.getElementById('map-container');
        mapContainer.innerHTML = `<iframe src="${mapsData[currentIndex].src}" class="w-100" style="height: 75vh;"></iframe>`;

        const slider = document.getElementById('map-slider');
        slider.value = currentIndex;
        currentIndex = (currentIndex + 1) % mapsData.length;
    }

    function startUpdating() {
        intervalId = setInterval(updateMap, 2000);
    }

    function stopUpdating() {
        clearInterval(intervalId);
    }


    updateMap();
    startUpdating();

    document.getElementById('pause-button').addEventListener('click', function() {
        const button = this;
        if (button.textContent === 'Pause') {
            stopUpdating();
            button.textContent = 'Resume';
        } else {
            startUpdating();
            button.textContent = 'Pause';
        }
    });

    document.getElementById('map-slider').addEventListener('input', function() {
        currentIndex = parseInt(this.value);
        updateMap();
    });
    document.getElementById('signup-form').addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent the default form submission behavior
        var email = document.getElementById('email').value;
    
        // Send the email to the server using AJAX
        fetch('http://127.0.0.1:5000/send_email', {  // Ensure this URL is correct
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ email: email })
        })
        .then(response => response.json())
        .then(data => {
            console.log(data.message);
    
            // Switch to signup.html
            window.location.href = 'signup.html';
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    });

});