from flask import Flask, render_template, request, jsonify
from src.models import run_modell

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def handle_data():
    # get the data from the post request and tranform them
    data = request.get_json()
    n = int(data["anzahl"])
    basis_temperatur = [int(temp) for temp in data["temperatur"].split("-")]
    fixkosten_pro_tag = float(data["fixkosten"])
    variable_kosten_pro_kunde = float(data["variableKosten"])
    umsatz_pro_kunde = [int(temp) for temp in data["umsatzProKunde"].split("-")]
    kunden_basis = [int(temp) for temp in data["kundenBasis"].split("-")]
    temp_schw = int(data["tempSchwankugenInput"])
    
    if str(data["warmheissesJahr"]) == "Ja":
        warm_heiss_jahr = True
    elif str(data["warmheissesJahr"]) == "Nein":
        warm_heiss_jahr = False
    else:
        warm_heiss_jahr = False
    
    total_profit, total_revenue, mean_revenue, mean_profit, mean_temperaturen, days, total_customers = run_modell(
        n=n, 
        fixkosten_pro_tag=fixkosten_pro_tag, 
        variable_kosten_pro_kunde=variable_kosten_pro_kunde, 
        basis_temperatur=basis_temperatur,
        umsatz_pro_kunde=umsatz_pro_kunde,
        kunden_basis=kunden_basis,
        warm_heiss_jahr=warm_heiss_jahr,
        temp_schw=temp_schw)
    
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
    app.run(host="0.0.0.0", port=3000)
