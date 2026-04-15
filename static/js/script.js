document.addEventListener('DOMContentLoaded', () => {
    // Shared Chart Options
    const chartOptions = {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
            legend: { labels: { color: '#ffffff', font: { family: 'Outfit', size: 12 } } }
        },
        scales: {
            x: { grid: { color: 'rgba(255, 255, 255, 0.05)' }, ticks: { color: '#a0a0a0' } },
            y: { grid: { color: 'rgba(255, 255, 255, 0.05)' }, ticks: { color: '#a0a0a0' } }
        }
    };

    // Helper to init charts only if element exists
    const safeChart = (id, type, labels, dataArr, label, color) => {
        const el = document.getElementById(id);
        if (!el) return;
        new Chart(el.getContext('2d'), {
            type: type,
            data: {
                labels: labels,
                datasets: [{
                    label: label,
                    data: dataArr,
                    borderColor: color,
                    backgroundColor: color.replace('1)', '0.1)'),
                    fill: type === 'line',
                    tension: 0.4
                }]
            },
            options: chartOptions
        });
    };

    // Global Reveal Logic
    const initReveal = () => {
        const reveals = document.querySelectorAll('.reveal');
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('active');
                }
            });
        }, { threshold: 0.1 });

        reveals.forEach(el => observer.observe(el));
        
        // Immediate check for visible elements
        reveals.forEach(el => {
            const rect = el.getBoundingClientRect();
            if (rect.top < window.innerHeight) el.classList.add('active');
        });
    };

    initReveal();

    // Specific Page Initializations
    // Climate
    if (document.getElementById('tempChart')) {
        // These are handled in the template scripts currently to use backend data
    }
});
