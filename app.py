from flask import Flask, render_template, request, jsonify
import numpy as np
from src.models import run_modell
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def handle_data():
    data = request.get_json()
    total_profit, total_revenue, mean_revenue, mean_profit, mean_temperaturen, days, total_customers = run_modell(
        int(data["anzahl"]))
    
    mean_revenue = mean_revenue.tolist()
    mean_profit = mean_profit.tolist()
    mean_temperaturen = mean_temperaturen.tolist()
    days = days.tolist()
    return jsonify({"total_customers": total_customers,
                    "total_profit": total_profit, 
                    "total_revenue": total_revenue,
                    "mean_revenue": mean_revenue,
                    "mean_profit": mean_profit,
                    "mean_temperature": mean_temperaturen,
                    "days": days}), 200




if __name__ == '__main__':
    app.run(debug=True)
