from flask import Flask, render_template, jsonify, request
import random
import time
from datetime import datetime
import requests

app = Flask(__name__)

# Comprehensive Global Datasets
DATASETS = {
    'climate': {
        'labels': ['1900', '1920', '1940', '1960', '1980', '2000', '2024'],
        'temperature': [-0.19, -0.27, 0.12, 0.03, 0.26, 0.40, 1.15],
        'co2_levels': [295.7, 300.2, 311.3, 316.9, 338.7, 369.5, 419.0],
    },
    'pollution': {
        'countries': ['India', 'China', 'Egypt', 'Pakistan', 'Bangladesh', 'Nigeria'],
        'pm25': [185, 142, 110, 105, 95, 88],
    },
    'poverty': {
        'wealth_tiers': ['Top 1%', 'Top 10%', 'Bottom 50%'],
        'wealth_share': [43, 82, 2],
    },
    'internet': {
        'online': 5.4,
        'offline': 2.6,
    },
    'health': {
        'mortality': [12.5, 10.2, 8.4, 7.1, 5.9],
        'life_expectancy': {'Japan': 84.6, 'USA': 77.3, 'India': 69.9, 'Nigeria': 54.3}
    },
    'education': {
        'literacy': [42, 55, 68, 75, 86, 90],
    },
    'energy': {
        'renewable_share': [5, 8, 12, 18, 24, 30],
    },
    'water': {
        'scarcity_pop': [1.2, 1.8, 2.4, 3.2],
    },
    'population': {
        'growth': [2.5, 4.0, 6.1, 8.1, 9.8],
    },
    'mental_health': {
        'anxiety_depression': [3.8, 4.1, 4.5, 5.2, 5.8],
    },
    'conflict': {
        'refugees': [10.2, 15.6, 25.4, 45.2, 114],
        'military_vs_edu': {'Military': 2.2, 'Education': 4.3}
    }
}

@app.route('/')
def index(): return render_template('index.html')

@app.route('/climate')
def climate(): return render_template('climate.html', data=DATASETS['climate'])

@app.route('/pollution')
def pollution(): return render_template('pollution.html', data=DATASETS['pollution'])

@app.route('/poverty')
def poverty(): return render_template('poverty.html', data=DATASETS['poverty'])

@app.route('/internet')
def internet(): return render_template('internet.html', data=DATASETS['internet'])

@app.route('/health')
def health(): return render_template('health.html', data=DATASETS['health'])

@app.route('/education')
def education(): return render_template('education.html', data=DATASETS['education'])

@app.route('/energy')
def energy(): return render_template('energy.html', data=DATASETS['energy'])

@app.route('/water')
def water(): return render_template('water.html', data=DATASETS['water'])

@app.route('/population')
def population(): return render_template('population.html', data=DATASETS['population'])

@app.route('/mental-health')
def mental_health(): return render_template('mental_health.html', data=DATASETS['mental_health'])

@app.route('/conflict')
def conflict(): return render_template('conflict.html', data=DATASETS['conflict'])

@app.route('/analytics')
def analytics(): return render_template('analytics.html')

@app.route('/stories')
def stories(): return render_template('stories.html')

@app.route('/simulator')
def simulator():
    countries = {
        'India': {'income': 2500, 'life': 69.9, 'internet': 45, 'edu': 74, 'pollution': 'High'},
        'USA': {'income': 76000, 'life': 77.3, 'internet': 92, 'edu': 99, 'pollution': 'Moderate'},
        'Japan': {'income': 35000, 'life': 84.6, 'internet': 94, 'edu': 100, 'pollution': 'Low'},
        'Nigeria': {'income': 2100, 'life': 54.3, 'internet': 36, 'edu': 62, 'pollution': 'Very High'}
    }
    return render_template('simulator.html', countries=countries)

@app.route('/compare')
def compare(): return render_template('compare.html', data=DATASETS)

@app.route('/impact')
def impact(): return render_template('impact.html')

@app.route('/rankings')
def rankings():
    rankings = {
        'Happiness': ['Finland', 'Denmark', 'Iceland', 'Israel', 'Netherlands'],
        'Healthcare': ['South Korea', 'Taiwan', 'Denmark', 'Austria', 'Japan'],
        'Green Energy': ['Iceland', 'Norway', 'Sweden', 'Brazil', 'Canada'],
        'Most Improved': 'Vietnam (Connectivity)',
        'Declining Region': 'Sahel (Food Security)'
    }
    return render_template('rankings.html', rankings=rankings)

@app.route('/solutions')
def solutions(): return render_template('solutions.html')

@app.route('/learn')
def learn(): return render_template('learn.html')

@app.route('/api/live-metrics')
def live_metrics():
    now = datetime.now()
    return jsonify({
        'timestamp': now.strftime('%H:%M:%S'),
        'deaths_today': random.randint(150000, 160000),
        'co2_ppm': round(419.0 + random.uniform(-0.01, 0.05), 3),
        'net_forest_loss': random.randint(10000, 15000),
        'temp_anomaly': round(1.15 + random.uniform(-0.02, 0.02), 2),
    })

@app.route('/api/predict')
def predict():
    year = int(request.args.get('year', 2024))
    emissions_rate = 1.05
    return jsonify({
        'prediction_year': year,
        'co2_est': round(419 * (emissions_rate ** ((year-2024)/10)), 1),
        'temp_est': round(1.15 + (0.15 * ((year-2024)/10)), 2),
        'sea_level_rise_cm': round((year-2024) * 0.4, 1)
    })

@app.route('/api/reality-shock')
def reality_shock():
    return jsonify({
        'plastic_to_ocean_kg': 250,
        'hunger_deaths_per_min': 11,
        'forest_loss_sqm': 27000
    })

@app.route('/api/weather')
def get_weather():
    locations = {'Tokyo': (35.6, 139.6), 'London': (51.5, -0.1), 'New York': (40.7, -74.0), 'Delhi': (28.6, 77.2)}
    weather_data = []
    try:
        for city, (lat, lon) in locations.items():
            url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
            res = requests.get(url, timeout=5).json()
            weather_data.append({'city': city, 'temp': res['current_weather']['temperature']})
        return jsonify(weather_data)
    except: return jsonify([])

if __name__ == '__main__':
    app.run(debug=True)
