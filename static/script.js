document.addEventListener("DOMContentLoaded", function () {

    const form = document.getElementById("predictionForm");

    form.addEventListener("submit", function () {

        const button = form.querySelector("button");

        button.innerHTML = "Predicting...";
        button.disabled = true;

    });

});