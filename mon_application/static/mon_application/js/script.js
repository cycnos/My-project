// mon_application/static/mon_application/js/script.js
document.getElementById("person-form").addEventListener("submit", function(event) {
    // Validation simple avant l'envoi du formulaire
    const firstName = document.getElementById("first_name").value;
    const lastName = document.getElementById("last_name").value;
    const age = document.getElementById("age").value;

    if (!firstName || !lastName || !age) {
        alert("Tous les champs sont requis !");
        event.preventDefault();  // Empêche l'envoi du formulaire si les champs sont vides
    }
});
