"use strict";

// variable for number of grading system "rows"
// TODO: use other mechanisms (e.g. closure) instead of global var
let num_gradeSys = 0;

function inputsFunc() {
    let gradeSys = {}; // Object to store Grade System items
    let inputs = [
        "#subName", "#reqType", "#start", "#end"
    ];
    let added = [];

    // Test will inputs are filled (except for grading system entries)
    for (let input of inputs){
        let userInput = document.querySelector(input);
        if(userInput.value.length == 0){
            alert(`Required field: ${input}`);
            return;
        };
        added.push(userInput.value);
    }
    
    // Fill the gradeSys object and push the Grading System entries ids for easy clearing
    for(let i = 1; i < num_gradeSys+1; i++){
        if(document.querySelector(`#gradeSys-Type-${i}`).value.length === 0){
            alert(`Required field: ${`#gradeSys-Type-${i}`}`);
            return;
        }
        if(document.querySelector(`#gradeSys-Points-${i}`).value.length === 0){
            alert(`Required field: ${`#gradeSys-Points-${i}`}`);
            return;
        }
        gradeSys[document.querySelector(`#gradeSys-Type-${i}`).value] = document.querySelector(`#gradeSys-Points-${i}`).value;
        inputs.push(`#gradeSys-Type-${i}`);
        inputs.push(`#gradeSys-Points-${i}`);
    }
    
    // Display the inputs as an alert message
    alert(`Added subject: ${added[0]} \nNo. of Units: ${added[1]} \nstart time: ${added[2]} \nend time: ${added[3]} \nGrading System: ${JSON.stringify(gradeSys)}]`);

    // Clear all inputs after submit
    for (let input of inputs){
        document.querySelector(input).value = '';
    }
}

function populateFeat() {
    let addSub = document.getElementById("addSub");

    let subName = document.createElement("input");
    subName.setAttribute("id", "subName");
    subName.setAttribute("type", "text");
    subName.setAttribute("placeholder", "select subject...");

    let subName_label = document.createElement("label");
    subName_label.setAttribute("class", "addSub_label");
    subName_label.htmlFor = "subName";
    subName_label.innerHTML = "Select Subject: ";

    let reqType = document.createElement("input");
    reqType.setAttribute("id", "reqType");
    reqType.setAttribute("type", "text");
    reqType.setAttribute("placeholder", "select requirement type...");
    

    let reqType_label = document.createElement("label");
    reqType_label.setAttribute("class", "addSub_label");
    reqType_label.htmlFor = "reqType";
    reqType_label.innerHTML = "Requirement Type: ";


    let reqName = document.createElement("input");
    reqName.setAttribute("id", "reqName");
    reqName.setAttribute("type", "text");
    reqName.setAttribute("placeholder", "enter requirement name here...");
    

    let reqName_label = document.createElement("label");
    reqName_label.setAttribute("class", "addSub_label");
    reqName_label.htmlFor = "reqType";
    reqName_label.innerHTML = "Requirement Name: ";


    

    addSub.appendChild(subName_label);
    addSub.appendChild(subName);
    addSub.appendChild(document.createElement("br"));
    addSub.appendChild(document.createElement("br"));
    addSub.appendChild(reqType_label);
    addSub.appendChild(reqType);
    addSub.appendChild(document.createElement("br"));
    addSub.appendChild(document.createElement("br"));
    addSub.appendChild(document.createElement("br"));
    addSub.appendChild(reqName_label);
    addSub.appendChild(reqName);

    let startEnd = document.getElementById("startEnd");

    let start = document.createElement("input");
    start.setAttribute("id", "start");
    start.setAttribute("type", "datetime-local");
    start.setAttribute("placeholder", "mm/dd/yyyy; hh/mm");

    let start_label = document.createElement("label");
    start_label.setAttribute("class", "startEnd_label");
    start_label.htmlFor = "start";
    start_label.innerHTML = "Due Date: ";

    let end = document.createElement("input");
    end.setAttribute("id", "end");
    end.setAttribute("type", "time");
    end.setAttribute("placeholder", "mm/dd/yyyy; hh/mm");

    let end_label = document.createElement("label");
    end_label.setAttribute("class", "startEnd_label");
    end_label.htmlFor = "end";
    end_label.innerHTML = "Time Due: ";

    startEnd.appendChild(start_label);
    startEnd.appendChild(start);
    startEnd.appendChild(document.createElement("br"));
    startEnd.appendChild(end_label);
    startEnd.appendChild(end);
}
populateFeat();

