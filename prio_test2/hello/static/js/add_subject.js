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

function showErrorBar(msg) {
    // NOTE: one-shot timer used to ensure that animation is always shown
    //       e.g. when errorBar is visible and both hideErrorBar()
    //       and showErrorBar() are called within a few ms of each other
    setTimeout(() => {
        let errorBar = document.getElementById("error-bar");
        // remove animation class so that we can initialize new animation later
        errorBar.classList.remove("error-bar-shake");
        errorBar.innerHTML = msg;
        errorBar.classList.add("error-bar-shake");

        errorBar.scrollIntoView();
    }, 100);
}

function hideErrorBar() {
    // NOTE: by default, the error bar has display: none
    //  and the animation class overrides this into display: block
    // hence to hide the bar, we simply need to remove the animation class
    let errorBar = document.getElementById("error-bar");
    errorBar.classList.remove("error-bar-shake");
}

// function add_gradeSys() {
//     let gradeSysBox = document.getElementById("gradeSysBox");
//
//     // remove add button, to be added to new "row"
//     let add_button = document.getElementById("add_gradeSys");
//     gradeSysBox.removeChild(add_button);
//
//     let gradeSysType = document.createElement("input");
//     gradeSysType.setAttribute("id", `gradeSys-Type-${++num_gradeSys}`);
//     gradeSysType.setAttribute("class", "gradeSys-Type");
//     gradeSysType.classList.add("input-field");
//     gradeSysType.setAttribute("type", "text");
//     gradeSysType.setAttribute("placeholder", "e.g. Exam");
//
//     let gradeSysPoints = document.createElement("input");
//     gradeSysPoints.setAttribute("id", `gradeSys-Points-${num_gradeSys}`);
//     gradeSysPoints.setAttribute("class", "gradeSys-Points");
//     gradeSysPoints.classList.add("input-field");
//     gradeSysPoints.setAttribute("type", "number");
//     gradeSysPoints.setAttribute("placeholder", "%, e.g. 30");
//     gradeSysPoints.setAttribute("min", 0);
//     gradeSysPoints.setAttribute("max", 100);
//
//     gradeSysBox.appendChild(gradeSysType);
//     gradeSysBox.appendChild(gradeSysPoints);
//     gradeSysBox.appendChild(add_button);
//     gradeSysBox.appendChild(document.createElement("br"));
// }

// add_gradeSys();
