"use strict";

// variable for number of grading system "rows"
// TODO: use other mechanisms (e.g. closure) instead of global var
let num_gradeSys = 0;

function inputsFunc() {
    let gradeSys = {};
    let inputs = [
        "#subName", "#unitNum", "#start", "#end"
    ];
    let added = [];

    for (let input of inputs){
        let userInput = document.querySelector(input);
        if(userInput.value.length == 0){
            alert(`Required field: ${input}`);
            return;
        };
        added.push(userInput.value);
    }
    
    for(let i = 1; i < num_gradeSys+1; i++){
        gradeSys[document.querySelector(`#gradeSys-Type-${i}`).value] = document.querySelector(`#gradeSys-Points-${i}`).value;
    }
    
    alert(`Added subject: ${added[0]} \nNo. of Units: ${added[1]} \nstart time: ${added[2]} \nend time: ${added[3]} \nGrading System: ${JSON.stringify(gradeSys)}]`);

    for (let input of inputs){
        document.querySelector(input).value = '';
    }

    for (let each of gradeSys){
        document.querySelector(each).value = '';
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
