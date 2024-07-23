// maps.js

document.addEventListener('DOMContentLoaded', function() {
    const mapsData = [
        { src: 'map.html', title: 'Day 1' },
        { src: 'map.html', title: 'Day 2' },
        { src: 'map.html', title: 'Day 3' },
        { src: 'map.html', title: 'Day 4' },
        { src: 'map.html', title: 'Day 5' },
        { src: 'map.html', title: 'Day 6' },
        { src: 'map.html', title: 'Day 7' }
    ];


    let currentIndex = 0;
    let intervalId;

    function updateMap() {
        // Update the map title
        const titleContainer = document.getElementById('map-title-container');
        titleContainer.innerHTML = `<h2>${mapsData[currentIndex].title}</h2>`;

        // Update the map iframe
        const mapContainer = document.getElementById('map-container');
        mapContainer.innerHTML = `<iframe src="${mapsData[currentIndex].src}" class="w-100" style="height: 75vh;"></iframe>`;

        // Update index to loop through maps
        currentIndex = (currentIndex + 1) % mapsData.length;
    }

    function startUpdating() {
        intervalId = setInterval(updateMap, 2000);
    }

    function stopUpdating() {
        clearInterval(intervalId);
    }

    // Initial render
    updateMap();
    startUpdating();

    // Pause button event listener
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
});
