"use strict";

function submitForm(form) {
    // reset error bar on each form submission
    hideErrorBar();
    // Identify required inputs and their label names
    let requiredInputs = {};
    for (let fieldID of [ "#subName", "#numUnits" ]) {
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

    // Check if subject name already exists
    const newSub = document.getElementById("subName").value;
    const subjects = JSON.parse(document.getElementById('subjects-data').textContent);
    console.log(newSub, Object.keys(subjects));
    if (Object.keys(subjects).find(subject => subject == newSub)) {
        showErrorBar(`Error: Subject <b>${newSub}</b> already exists.`);
        return;
    }

    // No validation errors, submit form
    form.submit();
}

function addGradeSys() {
    let gradeSysBox = document.getElementById("gradeSysBox");
    let del_button = document.getElementById("del_gradeSys");
    let add_button = document.getElementById("add_gradeSys");

    const reqNameFmt = "reqName";
    const gradeNumFmt = "gradeNum";
    const maxGradeNum = 5;

    // NOTE: assumes that the add gradeSys button is added right after an id=gradeNumX element
    const currGradeSysNum = parseInt(add_button.previousElementSibling.name.substring(gradeNumFmt.length));
    const newGradeSysNum = currGradeSysNum + 1;

    if (newGradeSysNum >= maxGradeNum) {
        add_button.setAttribute("hidden", "true");
    } else {
        add_button.removeAttribute("hidden");
    }

    if (newGradeSysNum > 1) {
        del_button.removeAttribute("hidden");
    }

    // remove add and delete buttons, to be added to new "row"
    gradeSysBox.removeChild(add_button);
    gradeSysBox.removeChild(del_button);

    // Show next row of gradeSys inputs
    let gradeSysElement = null;
    for (let fmt of [ reqNameFmt, gradeNumFmt ]) {
        gradeSysElement = document.getElementsByName(`${fmt}${newGradeSysNum}`)[0];
        gradeSysElement.removeAttribute("hidden");
    }

    // NOTE: at this point, gradeSysElement should hold gradeNum{X+1}
    // re-add buttons, right beside gradeNum{X+1}
    gradeSysElement.after(add_button, del_button);
}

function delGradeSys() {
    let gradeSysBox = document.getElementById("gradeSysBox");
    let del_button = document.getElementById("del_gradeSys");
    let add_button = document.getElementById("add_gradeSys");

    const reqNameFmt = "reqName";
    const gradeNumFmt = "gradeNum";
    const maxGradeNum = 5;

    // NOTE: assumes that the add gradeSys button is added right after an id=gradeNumX element
    const currGradeSysNum = parseInt(add_button.previousElementSibling.name.substring(gradeNumFmt.length));
    const newGradeSysNum = currGradeSysNum - 1;

    if (newGradeSysNum <= 1) {
        del_button.setAttribute("hidden", "true");
    } else {
        del_button.removeAttribute("hidden");
    }

    if (newGradeSysNum < maxGradeNum) {
        add_button.removeAttribute("hidden");
    }

    // remove add and delete buttons, to be added to new "row"
    gradeSysBox.removeChild(add_button);
    gradeSysBox.removeChild(del_button);

    // hide current row of gradeSys inputs and clear contents
    for (let fmt of [ reqNameFmt, gradeNumFmt ]) {
        let gradeSysElement = document.getElementsByName(`${fmt}${currGradeSysNum}`)[0];
        gradeSysElement.value = "";
        gradeSysElement.setAttribute("hidden", "true");
    }

    // re-add buttons, right beside gradeNum{X-1}
    document.getElementsByName(`${gradeNumFmt}${newGradeSysNum}`)[0].after(add_button, del_button);
}
