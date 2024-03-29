"use strict";

// NOTE: Taken from add_subject.js
function submitForm(form) {
    // reset error bar on each form submission
    hideErrorBar();
    let requiredFields = [ "#reqType", "#taskName", "#dueDate" ];

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

    // TODO: replace with actual popup/message toast/bar/etc.
    // NOTE: Technically message should be AFTER form submission, but that needs more work
    alert("Task Added Successfully.");
    // No validation errors, submit form
    form.submit();
}

function subjectChanged(form) {
    // add previous reqType, taskName, dueDate values
    let fieldIDs = [ "reqType", "taskName", "dueDate", "taskNotes"];
    for (const id of fieldIDs) {
        // HACK: Add to form by appending hidden input elements
        let addInput = document.createElement("input");
        addInput.setAttribute("type", "hidden");
        addInput.setAttribute("name", id);
        addInput.setAttribute("value", document.getElementById(id)?.value);
        form.appendChild(addInput);
    }

    form.submit();
}
