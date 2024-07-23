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
        const container = document.getElementById('maps-container');
        container.innerHTML = `
            <h2>${mapsData[currentIndex].title}</h2>
            <iframe src="${mapsData[currentIndex].src}" class="w-100" style="height: 75vh;"></iframe>
        `;
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
