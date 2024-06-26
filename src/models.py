"""Tom Bischopink © - HTWD 2024"""
import numpy as np


class Temperature:

    days = 365

    def __init__(self, hot_year: bool = False, temp_var: int = 2) -> None:
        self.hot_year = hot_year
        self.temp_var = temp_var

    def calculate_temperature(self) -> np.ndarray:
        offset = 15 if self.hot_year else 11
        days = np.arange(1, 366)
        temps = 1 + 15 * np.sin(2 * np.pi * (days - 92) / 365) + \
            np.random.uniform(-self.temp_var, self.temp_var, 365) + offset
        return temps


class EisdielenGeschäft:

    def __init__(self, temperaturen: np.ndarray, fixkosten_pro_tag: int = 100, umsatz_temperatur_faktor: float = 0.05,
                 variable_kosten_pro_kunde: float = 0.5, kunden_temperatur_faktor: int = 5,
                 basis_temperatur: list = [10, 15], kunden_basis: list = [50, 60], umsatz_pro_kunde: list = [3, 5]) -> None:

        self.temperaturen = temperaturen
        self.fixkosten_pro_tag = fixkosten_pro_tag
        self.umsatz_temperatur_faktor = umsatz_temperatur_faktor
        self.variable_kosten_pro_kunde = variable_kosten_pro_kunde
        self.kunden_temperatur_faktor = kunden_temperatur_faktor
        self.basis_temperatur = basis_temperatur
        self.kunden_basis = kunden_basis
        self.umsatz_pro_kunde = umsatz_pro_kunde

    def run_modell(self):
        # zufällige Werte für die Parameter für das Modell zum Start der Simulation
        basis_temperatur = np.random.randint(
            self.basis_temperatur[0], self.basis_temperatur[1])
        kunden_basis = np.random.randint(
            self.kunden_basis[0], self.kunden_basis[1])
        umsatz_pro_kunde = np.random.uniform(
            self.umsatz_pro_kunde[0], self.umsatz_pro_kunde[1])

        tage_im_jahr = len(self.temperaturen)
        kunden_temperatur_faktor = self.kunden_temperatur_faktor
        fixkosten_pro_tag = self.fixkosten_pro_tag
        umsatz_temperatur_faktor = self.umsatz_temperatur_faktor
        variable_kosten_pro_kunde = self.variable_kosten_pro_kunde

        # berechnungen
        kundenanzahl = kunden_basis + \
            (self.temperaturen - basis_temperatur) * kunden_temperatur_faktor
        # negative werte auf 0 setzen
        kundenanzahl = np.maximum(kundenanzahl, 0)
        umsatz_pro_kunde = umsatz_pro_kunde + \
            (self.temperaturen - basis_temperatur) * umsatz_temperatur_faktor
        gesamt_umsatz = kundenanzahl * umsatz_pro_kunde
        gesamt_kosten = fixkosten_pro_tag * \
            np.ones(tage_im_jahr) + variable_kosten_pro_kunde * kundenanzahl

        profit = gesamt_umsatz - gesamt_kosten

        return profit, gesamt_umsatz, self.temperaturen, kundenanzahl


def run_modell(n: int,
               fixkosten_pro_tag: int = 200,
               basis_temperatur: list = [10, 15],
               variable_kosten_pro_kunde: float = 0.6,
               umsatz_pro_kunde: list = [3, 5],
               kunden_basis: list = [50, 60],
               temp_schw: int = 2,
               warm_heiss_jahr: bool = False
               ):
    total_revenue = []
    total_profit = []
    mean_revenue = []
    mean_profit = []
    temperaturen = []
    customers = []
    for _ in range(n):
        temp = Temperature(hot_year=warm_heiss_jahr, temp_var=temp_schw).calculate_temperature()
        profit, revenue, temperature, customer = EisdielenGeschäft(
            temperaturen=temp,
            fixkosten_pro_tag=fixkosten_pro_tag,
            variable_kosten_pro_kunde=variable_kosten_pro_kunde,
            basis_temperatur=basis_temperatur,
            umsatz_pro_kunde=umsatz_pro_kunde,
            kunden_basis=kunden_basis
        ).run_modell()

        total_profit.append(sum(profit))
        total_revenue.append(sum(revenue))
        mean_revenue.append(revenue)
        mean_profit.append(profit)
        temperaturen.append(temperature)
        customers.append(sum(customer))

    days = np.arange(1, 366)
    mean_revenue = np.mean(mean_revenue, axis=0)
    mean_profit = np.mean(mean_profit, axis=0)
    mean_temperaturen = np.mean(temperaturen, axis=0)
    total_profit = np.mean(total_profit).round(2)
    total_profit_str = f"{total_profit:,.2f} Euro"
    total_revenue = np.mean(total_revenue).round(2)
    total_revenue_str = f"{total_revenue:,.2f} Euro"
    total_customers = np.mean(customers).round()
    
    costs_per_customer = (total_revenue - total_profit) / total_customers
    revenue_per_customer = total_revenue / total_customers
    profit_per_customer = total_profit / total_customers
    print(f"Costs per customer: {costs_per_customer:.2f} Euro")
    print(f"Revenue per customer: {revenue_per_customer:.2f} Euro")
    print(f"Profit per customer: {profit_per_customer:.2f} Euro")

    return total_profit_str, total_revenue_str, mean_revenue, mean_profit, mean_temperaturen, days, total_customers
