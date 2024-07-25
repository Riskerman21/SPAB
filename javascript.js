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

    
    // Fetch province and amphoe data from the JSON file
    $.getJSON('province_amphoe.json', function(data) {
        var provinceData = data; // Store the province data

        var provinces = Object.keys(provinceData);
        $('#province').empty();
        $('#province').append('<option value="">Select a province</option>');
        provinces.forEach(function(province) {
            $('#province').append('<option value="' + province + '">' + province + '</option>');
        });

        $('#province').on('change', function() {
            var selectedProvince = $(this).val();
            var amphoes = provinceData[selectedProvince] || [];

            $('#amphoe').empty();
            $('#amphoe').append('<option value="">Select an amphoe</option>');

            amphoes.forEach(function(amphoe) {
                $('#amphoe').append('<option value="' + amphoe + '">' + amphoe + '</option>');
            });
        });
    });


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
    });
 
    document.getElementById('predict-button').addEventListener('click', function(event) {
        event.preventDefault(); // Prevent the default form submission behavior
    
        var amphoe = document.getElementById('amphoe').value;
        var province = document.getElementById('province').value;
        var month = document.getElementById('month').value;
    
        // Send an AJAX request to the server to predict the flood risk
        $.ajax({
            url: 'http://127.0.0.1:5000/long_predict',
            type: 'POST',
            data: JSON.stringify({
                month: month,
                amphoe: amphoe,
                province: province
            }),
            contentType: 'application/json',
            success: function(response) {
                console.log(response);
                const riskContainer = document.getElementById('risk-container');
                riskContainer.innerHTML = `<h2>Predicted Risk: ${data.risk}</h2>`;
            },
            error: function(xhr, status, error) {
                console.error(xhr.responseText);
            }
        });
    });    
});

async function sendMessage() {
    const userInput = document.getElementById('user-input').value;
    const chatContent = document.getElementById('chat-content');

    // Add user's message to the chat
    const userMessageDiv = document.createElement('div');
    userMessageDiv.textContent = userInput;
    chatContent.appendChild(userMessageDiv);

    // Style "You: " part separately
    const youSpan = document.createElement('span');
    youSpan.textContent = 'You: ';
    youSpan.style.fontWeight = 'bold';  // Apply bold font weight
    userMessageDiv.insertBefore(youSpan, userMessageDiv.firstChild);  // Insert "You: " at the beginning of userMessageDiv

    // Send user's message to the server
    const response = await fetch('http://127.0.0.1:5000/send_to_bot', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: userInput })
    });

    const responseData = await response.json();

    // Add bot's response to the chat
    const botMessageDiv = document.createElement('div');
    const botResponse = responseData.answer;

    // Creating elements and applying styles
    const steveSpan = document.createElement('span');
    steveSpan.textContent = 'Steve: ';
    steveSpan.style.fontWeight = 'bold';  // Make "Steve" bold

    const responseSpan = document.createElement('span');
    responseSpan.textContent = botResponse;

    // Add both spans to the div
    botMessageDiv.appendChild(steveSpan);
    botMessageDiv.appendChild(responseSpan);

    // Add botMessageDiv to chatContent (assuming chatContent is your chat area)
    chatContent.appendChild(botMessageDiv);

    // Scroll to the bottom of the chat content
    chatContent.scrollTop = chatContent.scrollHeight;

    // Clear the input field
    document.getElementById('user-input').value = '';
}

function toggleChatbot() {
    var chatbot = document.getElementById('chatbot-overlay');
    if (chatbot.style.display === 'none' || chatbot.style.display === '') {
        chatbot.style.display = 'block';
    } else {
        chatbot.style.display = 'none';
    }
}  
