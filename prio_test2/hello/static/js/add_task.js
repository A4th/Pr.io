"use strict";

// NOTE: Taken from add_subject.js
function submitForm(form) {
    // reset error bar on each form submission
    hideErrorBar();
    let requiredFields = [ "#reqField", "#taskName", "#dueDate" ];

    // Identify required inputs and their label names
    let requiredInputs = {};
    for (let fieldID of requiredFields) {
        requiredInputs[fieldID] = document.querySelector(fieldID).labels[0].textContent;
    }

    // Input validation
    // Check required fields
    for (let input in requiredInputs) {
        let userInput = document.querySelector(input);
        if(userInput.value.length == 0) {
            showErrorBar(`Error: The <b>${requiredInputs[input]}</b> field is required.`);
            return;
        };
    }

    // Ensure that appropriate subject is chosen
    const subject_id = document.getElementById("subject_id").value;
    if (subject_id === null || subject_id == -1) {
        showErrorBar(`Error: Please choose a <b>Subject</b>.`);
        return;
    }

    // No validation errors, submit form
    form.submit();
}
