"use strict";

// variable for number of grading system "rows"
// TODO: use other mechanisms (e.g. closure) instead of global var
let num_gradeSys = 0;
// NOTE: This is a dummy "database" for recording subjects data
let subjects = [];

function inputsFunc() {
    let gradeSys = {}; // Object to store Grade System items
    let inputs = [
        "#subName", "#numUnits", "#start", "#end"
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
    
    // Save to database
    // TODO: Use actual data instead of "dummy" global array
    let subject_data = {
        name: added[0],
        units: added[1],
        sched: [{day: "M", start: added[2], end: added[3]}],
        gradeSys: gradeSys
    };

    hideErrorBar();
    if (subjects.find(subject => subject.name == subject_data.name)) {
        showErrorBar(`Error #1: Subject <b>${subject_data.name}</b> already exists.`);
    } else {
        subjects.push(subject_data);
        // Display the inputs as an alert message
        alert(`Added subject: ${added[0]} \nNo. of Units: ${added[1]} \nstart time: ${added[2]} \nend time: ${added[3]} \nGrading System: ${JSON.stringify(gradeSys)}]`);

        // Clear all inputs after submit
        for (let input of inputs){
            document.querySelector(input).value = '';
        }
    }
}

function showErrorBar(msg) {
    let errorBar = document.getElementById("error-bar");
    // remove animation class sJ that we can initialize new animation later
    errorBar.classList.remove("error-bar-shake");
    errorBar.innerHTML = msg;
    errorBar.classList.add("error-bar-shake");
}

function hideErrorBar() {
    // NOTE: by default, the error bar has display: none
    //  and the animation class overrides this into display: block
    // hence to hide the bar, we simply need to remove the animation class
    let errorBar = document.getElementById("error-bar");
    errorBar.classList.remove("error-bar-shake");
}

// function populateFeat() {
//     let addSub = document.getElementById("addSub");

//     let subName = document.createElement("input");
//     subName.setAttribute("id", "subName");
//     subName.setAttribute("name", "subName");
//     subName.classList.add("input-field");
//     subName.setAttribute("type", "text");
//     subName.setAttribute("placeholder", "...enter subject name");

//     let subName_label = document.createElement("label");
//     subName_label.setAttribute("class", "field_label");
//     subName_label.htmlFor = "subName";
//     subName_label.innerHTML = "Subject Name: ";

//     let numUnits = document.createElement("input");
//     numUnits.setAttribute("id", "numUnits");
//     numUnits.setAttribute("name", "numUnits");
//     numUnits.classList.add("input-field");
//     numUnits.setAttribute("type", "number");
//     numUnits.setAttribute("placeholder", "...enter number of units");
    

//     let numUnits_label = document.createElement("label");
//     numUnits_label.setAttribute("class", "field_label");
//     numUnits_label.htmlFor = "numUnits";
//     numUnits_label.innerHTML = "Number of Units: ";

//     addSub.appendChild(subName_label);
//     addSub.appendChild(subName);
//     addSub.appendChild(document.createElement("br"));
//     addSub.appendChild(document.createElement("br"));
//     addSub.appendChild(numUnits_label);
//     addSub.appendChild(numUnits);
//     addSub.appendChild(document.createElement("br"));
//     addSub.appendChild(document.createElement("br"));

//     let startEnd = document.getElementById("startEnd");

//     let start = document.createElement("input");
//     start.setAttribute("id", "start");
//     start.setAttribute("name", "subStart");

//     start.classList.add("input-field");
//     start.setAttribute("type", "datetime-local");
//     start.setAttribute("placeholder", "mm/dd/yyyy; hh/mm");

//     let start_label = document.createElement("label");
//     start_label.setAttribute("class", "field_label");
//     start_label.htmlFor = "start";
//     start_label.innerHTML = "Start Time: ";

//     let end = document.createElement("input");
//     end.setAttribute("id", "end");
//     end.setAttribute("name", "subEnd");

//     end.classList.add("input-field");   
//     end.setAttribute("type", "datetime-local");
//     end.setAttribute("placeholder", "mm/dd/yyyy; hh/mm");

//     let end_label = document.createElement("label");
//     end_label.setAttribute("class", "field_label");
//     end_label.htmlFor = "end";
//     end_label.innerHTML = "End Time: ";

//     startEnd.appendChild(start_label);
//     startEnd.appendChild(start);
//     startEnd.appendChild(document.createElement("br"));
//     startEnd.appendChild(end_label);
//     startEnd.appendChild(end);
//     startEnd.appendChild(document.createElement("br"));
// }

function add_gradeSys() {
    let gradeSysBox = document.getElementById("gradeSysBox");

    // remove add button, to be added to new "row"
    let add_button = document.getElementById("add_gradeSys");
    gradeSysBox.removeChild(add_button);

    let gradeSysType = document.createElement("input");
    gradeSysType.setAttribute("id", `gradeSys-Type-${++num_gradeSys}`);
    gradeSysType.setAttribute("class", "gradeSys-Type");
    gradeSysType.classList.add("input-field");
    gradeSysType.setAttribute("type", "text");
    gradeSysType.setAttribute("placeholder", "e.g. Exam");

    let gradeSysPoints = document.createElement("input");
    gradeSysPoints.setAttribute("id", `gradeSys-Points-${num_gradeSys}`);
    gradeSysPoints.setAttribute("class", "gradeSys-Points");
    gradeSysPoints.classList.add("input-field");
    gradeSysPoints.setAttribute("type", "number");
    gradeSysPoints.setAttribute("placeholder", "%, e.g. 30");
    gradeSysPoints.setAttribute("min", 0);
    gradeSysPoints.setAttribute("max", 100);

    gradeSysBox.appendChild(gradeSysType);
    gradeSysBox.appendChild(gradeSysPoints);
    gradeSysBox.appendChild(add_button);
    gradeSysBox.appendChild(document.createElement("br"));
}

// populateFeat();
add_gradeSys();
