// maps.js
document.addEventListener('DOMContentLoaded', function() {
    const mapsData = [
        { src: 'maps/map0.html', title: 'Fri 26 Jul, 2024' },
        { src: 'maps/map1.html', title: 'Sat 27 Jul, 2024' },
        { src: 'maps/map2.html', title: 'Sun 28 Jul, 2024' },
        { src: 'maps/map3.html', title: 'Mon 29 Jul, 2024' },
        { src: 'maps/map4.html', title: 'Tue 30 Jul, 2024' },
        { src: 'maps/map5.html', title: 'Wed 31 Jul, 2024' },
        { src: 'maps/map6.html', title: 'Thu 1 Aug, 2024' }
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

    document.addEventListener('DOMContentLoaded', (event) => {
        document.getElementById('predict-risk-button').addEventListener('click', predictRisk);
    });

    updateMap();
    console.log('Maps initialized');
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

        
        function predictRisk() {
            // Your function logic here
            alert("Predict Risk button pressed!");
            var amphoe = document.getElementById('amphoe').value;
            var province = document.getElementById('province').value;
            var month = document.getElementById('month').value;
        
            // Send an AJAX request to the server to predict the flood risk
            $.ajax({
                url: '/long_predict',
                type: 'POST',
                data: {
                    amphoe: amphoe,
                    province: province,
                    month: month
                },
                success: function(response) {
                    // Handle the response from the server
                    console.log('Flood risk prediction:', response);
                    // Update the UI with the predicted risk information
                },
                error: function(error) {
                    // Handle any errors that occur during the AJAX request
                    console.error('Error:', error);
                }
            });
        }

    });
});
