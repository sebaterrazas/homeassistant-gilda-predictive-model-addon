from flask import Flask, jsonify
import random
from datetime import datetime, timedelta

app = Flask(__name__)

def generate_predictions():
    # Start time: now
    start_time = datetime.now()
    # End time: 2 days from now
    end_time = start_time + timedelta(days=2)
    # List to hold the predictions
    predictions = []
    
    # Generate timestamps at 1-hour intervals
    current_time = start_time
    while current_time <= end_time:
        # Generate a random consumption value between 0 and 1.5
        consumption = random.uniform(0, 1.5)
        # Append the time and consumption as a dictionary
        predictions.append({
            'time': current_time.isoformat(),  # Format as ISO 8601 string
            'consumption': consumption
        })
        # Increment the time by 1 hour
        current_time += timedelta(hours=1)
    
    return { 'predictions': predictions }

@app.route('/predict', methods=['GET'])
def get_prediction():
    # Get the list of predictions (time and consumption)
    predictions = generate_predictions()
    return jsonify(predictions)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

