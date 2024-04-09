import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Feste Parameter
tage_im_jahr = 365
fixkosten_pro_tag = 100  # Beispielwert
variable_kosten_pro_kunde = 2  # Beispielwert

# Temperaturprofil über das Jahr generieren (einfaches Modell)
# Annahme: Hochsommer am 182. Tag (Julimitte), Temperatur variiert sinusförmig mit zufälligen Schwankungen
basis_temperatur = 13  # Durchschnittstemperatur
amplitude = 15  # Temperaturunterschied zwischen Sommer und Winter
zufalls_schwankung = 3  # Maximale zufällige Temperaturschwankung
tage = np.arange(1, tage_im_jahr + 1)
temperaturen = basis_temperatur + amplitude * np.sin(2 * np.pi * (tage - 182) / tage_im_jahr) + np.random.uniform(-zufalls_schwankung, zufalls_schwankung, tage_im_jahr)

# Kundenanzahl und Umsatz pro Kunde modellieren
# Annahme: Mehr Kunden und höherer Umsatz bei höheren Temperaturen
kunden_basis = 50  # Basis-Kundenanzahl bei durchschnittlicher Temperatur
kunden_temperatur_faktor = 5  # Wie stark die Temperatur die Kundenanzahl beeinflusst
umsatz_pro_kunde_basis = 5  # Durchschnittlicher Umsatz pro Kunde bei durchschnittlicher Temperatur
umsatz_temperatur_faktor = 0.5  # Wie stark die Temperatur den Umsatz pro Kunde beeinflusst

# Berechnungen
kundenanzahl = kunden_basis + (temperaturen - basis_temperatur) * kunden_temperatur_faktor
kundenanzahl = np.maximum(kundenanzahl, 0)  # Verhindern negativer Kundenanzahlen
umsatz_pro_kunde = umsatz_pro_kunde_basis + (temperaturen - basis_temperatur) * umsatz_temperatur_faktor
gesamtumsatz = kundenanzahl * umsatz_pro_kunde
gesamtkosten = fixkosten_pro_tag * np.ones(tage_im_jahr) + variable_kosten_pro_kunde * kundenanzahl
profit = gesamtumsatz - gesamtkosten

# Ergebnisse in einem DataFrame speichern
ergebnisse = pd.DataFrame({
    'Tag': tage,
    'Temperatur': temperaturen,
    'Kundenanzahl': kundenanzahl,
    'UmsatzProKunde': umsatz_pro_kunde,
    'Gesamtumsatz': gesamtumsatz,
    'Gesamtkosten': gesamtkosten,
    'Profit': profit
})

# Visualisierung der Temperatur und des Profits über das Jahr
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.plot(tage, temperaturen, label='Temperatur')
plt.xlabel('Tag')
plt.ylabel('Temperatur (°C)')
plt.title('Temperatur über das Jahr')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(tage, profit, label='Profit', color='green')
plt.xlabel('Tag')
plt.ylabel('Profit (€)')
plt.title('Täglicher Profit über das Jahr')
plt.legend()

plt.tight_layout()
plt.show()

# Jahresübersicht
jahr_summary = ergebnisse[['Gesamtumsatz', 'Gesamtkosten', 'Profit']].sum()
jahr_summary
