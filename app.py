from flask import Flask, render_template, jsonify
import random
import time
from datetime import datetime

app = Flask(__name__)

# Global Datasets
DATASETS = {
    'climate': {
        'labels': ['1960', '1970', '1980', '1990', '2000', '2010', '2020', '2024'],
        'temperature': [0.03, 0.02, 0.26, 0.45, 0.40, 0.72, 1.02, 1.15],
        'co2_levels': [316.9, 325.7, 338.7, 354.4, 369.5, 389.9, 414.2, 419.0]
    },
    'pollution': {
        'countries': ['India', 'China', 'Egypt', 'Mexico', 'Indonesia', 'UK', 'USA'],
        'pm25': [185, 142, 110, 95, 88, 35, 28],
        'waste_sources': ['Industrial', 'Municipal', 'Agricultural', 'Construction'],
        'waste_values': [45, 25, 20, 10]
    },
    'poverty': {
        'years': ['1990', '2000', '2010', '2015', '2019', '2022', '2024'],
        'rate': [37.8, 29.1, 15.7, 10.1, 8.4, 9.3, 8.9],
        'regions': ['Africa', 'South Asia', 'East Asia', 'Latin Am.'],
        'regional_poverty': [41, 12, 1, 4]
    },
    'internet': {
        'regions': ['N. America', 'Europe', 'East Asia', 'Latin Am.', 'S. Asia', 'Africa'],
        'penetration': [94, 88, 75, 70, 45, 36],
        'mobile_users': [320, 580, 1200, 450, 800, 500] # In millions
    }
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/climate')
def climate():
    return render_template('climate.html', data=DATASETS['climate'])

@app.route('/pollution')
def pollution():
    return render_template('pollution.html', data=DATASETS['pollution'])

@app.route('/poverty')
def poverty():
    return render_template('poverty.html', data=DATASETS['poverty'])

@app.route('/internet')
def internet():
    return render_template('internet.html', data=DATASETS['internet'])

@app.route('/analytics')
def analytics():
    return render_template('analytics.html')

@app.route('/api/live-metrics')
def live_metrics():
    # Simulate real-time metrics
    return jsonify({
        'timestamp': datetime.now().strftime('%H:%M:%S'),
        'co2': round(419.0 + random.uniform(-0.01, 0.05), 3),
        'temp_anomaly': round(1.15 + random.uniform(-0.02, 0.02), 2),
        'active_sensors': random.randint(12400, 12500),
        'events': [
            {"type": "Climate", "msg": f"Temperature surge detected in {random.choice(['Arctic', 'Amazon', 'Sahara'])}"},
            {"type": "Pollution", "msg": f"Air quality advisory in {random.choice(['Delhi', 'Beijing', 'Cairo'])}"},
            {"type": "Connectivity", "msg": f"New satellite link established in {random.choice(['Nigeria', 'Bolivia', 'Vietnam'])}"}
        ]
    })

if __name__ == '__main__':
    app.run(debug=True)
