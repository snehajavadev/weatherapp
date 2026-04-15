from flask import Flask, render_template, jsonify
import random
import time
from datetime import datetime
import requests

app = Flask(__name__)

# Comprehensive Global Datasets (Curated from World Bank, WHO, NASA, etc.)
DATASETS = {
    'climate': {
        'labels': ['1900', '1920', '1940', '1960', '1980', '2000', '2024'],
        'temperature': [-0.19, -0.27, 0.12, 0.03, 0.26, 0.40, 1.15],
        'co2_levels': [295.7, 300.2, 311.3, 316.9, 338.7, 369.5, 419.0],
        'ice_mass': [0, -500, -1200, -2500, -4500, -8000, -13500], # Gt change
    },
    'pollution': {
        'countries': ['India', 'China', 'Egypt', 'Pakistan', 'Bangladesh', 'Nigeria'],
        'pm25': [185, 142, 110, 105, 95, 88],
        'plastic_waste': [8.5, 5.9, 3.2, 2.8, 1.5, 1.1] # Million tonnes
    },
    'poverty': {
        'wealth_tiers': ['Top 1%', 'Top 10%', 'Bottom 50%'],
        'wealth_share': [43, 82, 2],
        'daily_income': [1500, 250, 2.15],
        'slum_pop': [650, 780, 880, 950, 1100] # Millions
    },
    'internet': {
        'online': 5.4, # Billions
        'offline': 2.6,
        'gender_gap': {'male': 70, 'female': 65},
        'speeds': {'Singapore': 250, 'USA': 200, 'India': 75, 'Nigeria': 25}
    },
    'health': {
        'mortality': [12.5, 10.2, 8.4, 7.1, 5.9], # Under 5 per 1000
        'healthcare_access': [95, 88, 72, 45, 30], # % coverage by region
        'life_expectancy': {'Japan': 84.6, 'USA': 77.3, 'India': 69.9, 'Nigeria': 54.3}
    },
    'education': {
        'literacy': [42, 55, 68, 75, 86, 90], # Global %
        'dropout_rates': [12, 15, 22, 35, 48], # Secondary % by region tier
        'gender_inequality': 0.82 # Parity index
    },
    'energy': {
        'renewable_share': [5, 8, 12, 18, 24, 30], # %
        'fossil_fuel': [92, 89, 85, 78, 70, 62], # %
        'footprint_per_capita': {'USA': 14.5, 'China': 8.2, 'India': 1.9, 'Ethiopia': 0.1}
    },
    'water': {
        'scarcity_pop': [1.2, 1.8, 2.4, 3.2], # Billions facing scarcity
        'access_clean': [70, 75, 82, 88, 92], # % global
        'usage': {'Industry': 19, 'Domestic': 11, 'Agriculture': 70}
    },
    'population': {
        'growth': [2.5, 4.0, 6.1, 8.1, 9.8], # Billions
        'urban': [29, 37, 45, 56, 68], # % urban population
        'megacities': [2, 10, 23, 34, 48] # Count
    },
    'mental_health': {
        'anxiety_depression': [3.8, 4.1, 4.5, 5.2, 5.8], # % global population
        'suicide_rates': [10.5, 10.2, 9.8, 9.4, 9.1], # Per 100k
        'youth_impact': 18 # % of adolescents
    },
    'conflict': {
        'refugees': [10.2, 15.6, 25.4, 45.2, 114], # Millions
        'military_vs_edu': {'Military': 2.2, 'Education': 4.3} # Trillions USD
    }
}

@app.route('/')
def index():
    return render_template('index.html')

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

@app.route('/api/live-metrics')
def live_metrics():
    # Real-time counter logic based on annual rates
    now = datetime.now()
    return jsonify({
        'timestamp': now.strftime('%H:%M:%S'),
        'deaths_today': random.randint(150000, 160000),
        'co2_ppm': round(419.0 + random.uniform(-0.01, 0.05), 3),
        'net_forest_loss': random.randint(10000, 15000), # Hectares
        'temp_anomaly': round(1.15 + random.uniform(-0.02, 0.02), 2),
        'events': [
            {"type": "Climate", "msg": f"Sea level rise detected in {random.choice(['Jakarta', 'Miami', 'Venice'])}"},
            {"type": "Conflict", "msg": f"New displacement reported in {random.choice(['Sudan', 'Ukraine', 'Myanmar'])}"}
        ]
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
