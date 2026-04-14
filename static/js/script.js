document.addEventListener('DOMContentLoaded', () => {
    // Shared Chart Options
    const chartOptions = {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
            legend: {
                labels: {
                    color: '#ffffff',
                    font: {
                        family: 'Outfit',
                        size: 14
                    }
                }
            },
            tooltip: {
                backgroundColor: 'rgba(5, 7, 10, 0.9)',
                titleFont: { family: 'Outfit', size: 14 },
                bodyFont: { family: 'Outfit', size: 14 },
                cornerRadius: 8,
                padding: 12
            }
        },
        scales: {
            x: {
                grid: { color: 'rgba(255, 255, 255, 0.05)' },
                ticks: { color: '#a0a0a0', font: { family: 'Outfit' } }
            },
            y: {
                grid: { color: 'rgba(255, 255, 255, 0.05)' },
                ticks: { color: '#a0a0a0', font: { family: 'Outfit' } }
            }
        }
    };

    // 1. Climate Change Chart (Global Temperature Anomaly)
    const climateCtx = document.getElementById('climateChart').getContext('2d');
    new Chart(climateCtx, {
        type: 'line',
        data: {
            labels: ['1960', '1970', '1980', '1990', '2000', '2010', '2020', '2024'],
            datasets: [{
                label: 'Temperature Anomaly (°C)',
                data: [0.03, 0.02, 0.26, 0.45, 0.40, 0.72, 1.02, 1.15],
                borderColor: '#00f2ff',
                backgroundColor: 'rgba(0, 242, 255, 0.1)',
                fill: true,
                tension: 0.4,
                borderWidth: 3,
                pointBackgroundColor: '#00f2ff'
            }]
        },
        options: chartOptions
    });

    // 2. Air Pollution Chart (AQI Comparison - Typical peak values)
    const pollutionCtx = document.getElementById('pollutionChart').getContext('2d');
    new Chart(pollutionCtx, {
        type: 'bar',
        data: {
            labels: ['New Delhi', 'Beijing', 'Cairo', 'Mexico City', 'Jakarta', 'London', 'New York'],
            datasets: [{
                label: 'Avg Daily AQI (PM2.5)',
                data: [185, 142, 110, 95, 88, 35, 28],
                backgroundColor: [
                    '#ff2d55', '#ff2d55', '#ff9f40', '#ff9f40', '#ffcc00', '#00e396', '#00e396'
                ],
                borderRadius: 10
            }]
        },
        options: {
            ...chartOptions,
            plugins: {
                ...chartOptions.plugins,
                legend: { display: false }
            }
        }
    });

    // 3. Poverty Chart (Global Extreme Poverty Rate)
    const povertyCtx = document.getElementById('povertyChart').getContext('2d');
    new Chart(povertyCtx, {
        type: 'line',
        data: {
            labels: ['1990', '2000', '2010', '2015', '2019', '2022', '2024'],
            datasets: [{
                label: '% Living below $2.15/day',
                data: [37.8, 29.1, 15.7, 10.1, 8.4, 9.3, 8.9],
                borderColor: '#ffcc00',
                backgroundColor: 'transparent',
                borderWidth: 3,
                pointRadius: 6,
                pointHoverRadius: 8,
                pointBackgroundColor: '#ffcc00'
            }]
        },
        options: chartOptions
    });

    // 4. Internet Access Chart (Regional Penetration %)
    const internetCtx = document.getElementById('internetChart').getContext('2d');
    new Chart(internetCtx, {
        type: 'doughnut',
        data: {
            labels: ['N. America', 'Europe', 'East Asia', 'Latin Am.', 'S. Asia', 'Africa'],
            datasets: [{
                data: [94, 88, 75, 70, 45, 36],
                backgroundColor: [
                    '#00f2ff', '#00b8ff', '#0080ff', '#4b00ff', '#9100ff', '#e100ff'
                ],
                borderWidth: 0,
                hoverOffset: 15
            }]
        },
        options: {
            ...chartOptions,
            cutout: '70%',
            plugins: {
                ...chartOptions.plugins,
                legend: {
                    position: 'right',
                    labels: {
                        color: '#ffffff',
                        padding: 20
                    }
                }
            }
        }
    });

    // Simple reveal animation on scroll
    const reveals = document.querySelectorAll('.data-section');
    const windowHeight = window.innerHeight;

    function revealSections() {
        reveals.forEach(reveal => {
            const elementTop = reveal.getBoundingClientRect().top;
            if (elementTop < windowHeight - 150) {
                reveal.style.opacity = '1';
                reveal.style.transform = 'translateY(0)';
            }
        });
    }

    // Initial styles for animation
    reveals.forEach(reveal => {
        reveal.style.opacity = '0';
        reveal.style.transform = 'translateY(50px)';
        reveal.style.transition = 'all 1s ease-out';
    });

    window.addEventListener('scroll', revealSections);
    revealSections(); // Trigger on load
});
