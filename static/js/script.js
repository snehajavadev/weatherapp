document.addEventListener('DOMContentLoaded', () => {
    // Shared Chart Options
    const chartOptions = {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
            legend: {
                labels: {
                    color: '#ffffff',
                    font: { family: 'Outfit', size: 14 }
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

    // Helper function to safe-init charts
    const initChart = (id, config) => {
        const el = document.getElementById(id);
        if (el) return new Chart(el.getContext('2d'), config);
        return null;
    };

    // 1. Climate Change Chart
    initChart('climateChart', {
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

    // 2. Air Pollution Chart
    initChart('pollutionChart', {
        type: 'bar',
        data: {
            labels: ['India', 'China', 'Egypt', 'Mexico', 'Indonesia', 'UK', 'USA'],
            datasets: [{
                label: 'Avg Daily AQI (PM2.5)',
                data: [185, 142, 110, 95, 88, 35, 28],
                backgroundColor: ['#ff2d55', '#ff2d55', '#ff9f40', '#ff9f40', '#ffcc00', '#00e396', '#00e396'],
                borderRadius: 10
            }]
        },
        options: {
            ...chartOptions,
            plugins: { ...chartOptions.plugins, legend: { display: false } }
        }
    });

    // 3. Poverty Chart
    initChart('povertyChart', {
        type: 'line',
        data: {
            labels: ['1990', '2000', '2010', '2015', '2019', '2022', '2024'],
            datasets: [{
                label: '% Poverty Rate',
                data: [37.8, 29.1, 15.7, 10.1, 8.4, 9.3, 8.9],
                borderColor: '#ffcc00',
                borderWidth: 3,
                pointRadius: 6,
                pointBackgroundColor: '#ffcc00'
            }]
        },
        options: chartOptions
    });

    // 4. Internet Access Chart
    initChart('internetChart', {
        type: 'doughnut',
        data: {
            labels: ['N. America', 'Europe', 'East Asia', 'Latin Am.', 'S. Asia', 'Africa'],
            datasets: [{
                data: [94, 88, 75, 70, 45, 36],
                backgroundColor: ['#00f2ff', '#00b8ff', '#0080ff', '#4b00ff', '#9100ff', '#e100ff'],
                borderWidth: 0
            }]
        },
        options: {
            ...chartOptions,
            cutout: '70%',
            plugins: {
                ...chartOptions.plugins,
                legend: { position: 'right', labels: { color: '#ffffff', padding: 20 } }
            }
        }
    });

    // Reveal animation
    const reveals = document.querySelectorAll('.reveal, .data-section');
    const windowHeight = window.innerHeight;

    function revealSections() {
        reveals.forEach(reveal => {
            const elementTop = reveal.getBoundingClientRect().top;
            if (elementTop < windowHeight - 100) {
                reveal.classList.add('active');
                // Support for old transition style
                reveal.style.opacity = '1';
                reveal.style.transform = 'translateY(0)';
            }
        });
    }

    // Set initial state for data-sections if not already reveal class
    document.querySelectorAll('.data-section').forEach(s => {
        if (!s.classList.contains('reveal')) {
            s.style.opacity = '0';
            s.style.transform = 'translateY(50px)';
            s.style.transition = 'all 1s ease-out';
        }
    });

    window.addEventListener('scroll', revealSections);
    revealSections();
});
