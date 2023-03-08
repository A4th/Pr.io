"use strict";

// variable for number of grading system "rows"
// TODO: use other mechanisms (e.g. closure) instead of global var
let num_gradeSys = 0;

function inputsFunc() {
    let gradeSys = {}; // Object to store Grade System items
    let inputs = [
        "#subName", "#unitNum", "#start", "#end"
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

function add_gradeSys() {
    let gradeSysBox = document.getElementById("gradeSysBox");

    // remove add button, to be added to new "row"
    let add_button = document.getElementById("add_gradeSys");
    gradeSysBox.removeChild(add_button);

    let gradeSysType = document.createElement("input");
    gradeSysType.setAttribute("id", `gradeSys-Type-${++num_gradeSys}`);
    gradeSysType.setAttribute("type", "text");
    gradeSysType.setAttribute("class", "gradeSys-Type");
    gradeSysType.setAttribute("placeholder", "e.g. Exam");

    let gradeSysPoints = document.createElement("input");
    gradeSysPoints.setAttribute("id", `gradeSys-Points-${num_gradeSys}`);
    gradeSysPoints.setAttribute("type", "number");
    gradeSysPoints.setAttribute("class", "gradeSys-Points");
    gradeSysPoints.setAttribute("placeholder", "%, e.g. 30");
    gradeSysPoints.setAttribute("min", 0);
    gradeSysPoints.setAttribute("max", 100);

    gradeSysBox.appendChild(gradeSysType);
    gradeSysBox.appendChild(gradeSysPoints);
    gradeSysBox.appendChild(add_button);
    gradeSysBox.appendChild(document.createElement("br"));
}

add_gradeSys();
