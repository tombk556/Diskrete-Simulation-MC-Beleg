function getInputs() {
    var anzahl = document.getElementById('anzahlInput').value;
    var fixkosten = document.getElementById('fixkostenInput').value;
    var variableKosten = document.getElementById('variableKostenInput').value;
    var temperatur = document.getElementById('temperaturInput').value;

    console.log('Anzahl an durchläufen:', anzahl);
    console.log('Fixkosten pro Tag (€):', fixkosten);
    console.log('Variable Kosten pro Kunden (€):', variableKosten);
    console.log('Basis Temperatur (°C):', temperatur);
}


const handleSubmit = async (e) => {
    e.preventDefault();
    getInputs();
}