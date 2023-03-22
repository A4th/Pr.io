"use strict";

function inputsFunc() {
    let gradeSys = {}; // Object to store Grade System items
    let inputs = [
        "#subName", "#reqType", "#reqName", "#dueDate"
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
    
    // Display the inputs as an alert message
    alert(`Added Task\n Subject: ${added[0]} \nRequirement Type: ${added[1]} \n Requirement Name:${added[2]} \n Due Date: ${added[3]}`);

    // Clear all inputs after submit
    for (let input of inputs){
        document.querySelector(input).value = '';
    }
}

function populateFeat() {
    let taskFields = document.getElementById("taskFields");

    let subName = document.createElement("select");
    subName.setAttribute("id", "subName");
    subName.setAttribute("type", "text");
    subName.setAttribute("placeholder", "select subject...");

    let sub1 = document.createElement("option");
    sub1.value = "CS 165";
    sub1.text = "CS 165";
    sub1.setAttribute("class","dropdownitem")

    let sub2 = document.createElement("option");
    sub2.value = "CS 138";
    sub2.text = "CS 138";
    sub2.setAttribute("class","dropdownitem")

    let sub3 = document.createElement("option");
    sub3.value = "CS 140";
    sub3.text = "CS 140";
    sub3.setAttribute("class","dropdownitem")



    subName.append(sub1);
    subName.append(sub2);
    subName.append(sub3);


    let subName_label = document.createElement("label");
    subName_label.setAttribute("class", "field_label");
    subName_label.htmlFor = "subName";
    subName_label.innerHTML = "Select Subject: ";

    let reqType = document.createElement("select");
    reqType.setAttribute("id", "reqType");
    reqType.setAttribute("type", "text");
    reqType.setAttribute("placeholder", "select requirement type...");


    let req1 = document.createElement("option");
    req1.value = "Problem Set";
    req1.text = "Problem Set";
    req1.setAttribute("class","dropdownitem")

    let req2 = document.createElement("option");
    req2.value = "Quiz";
    req2.text = "Quiz";
    req2.setAttribute("class","dropdownitem")

    let req3 = document.createElement("option");
    req3.value = "Long Exam";
    req3.text = "Long Exam";
    req3.setAttribute("class","dropdownitem")



    reqType.append(req1);
    reqType.append(req2);
    reqType.append(req3);

    

    let reqType_label = document.createElement("label");
    reqType_label.setAttribute("class", "field_label");
    reqType_label.htmlFor = "reqType";
    reqType_label.innerHTML = "Requirement Type: ";


    let reqName = document.createElement("input");
    reqName.setAttribute("id", "reqName");
    reqName.setAttribute("type", "text");
    reqName.setAttribute("placeholder", "enter requirement name here...");
    

    let reqName_label = document.createElement("label");
    reqName_label.setAttribute("class", "field_label");
    reqName_label.htmlFor = "reqName";
    reqName_label.innerHTML = "Requirement Name: ";


    taskFields.appendChild(subName_label);
    taskFields.appendChild(subName);
    taskFields.appendChild(document.createElement("br"));
    taskFields.appendChild(document.createElement("br"));
    taskFields.appendChild(document.createElement("br"));
    taskFields.appendChild(document.createElement("br"));
    taskFields.appendChild(document.createElement("br"));
    taskFields.appendChild(document.createElement("br"));
    taskFields.appendChild(reqType_label);
    taskFields.appendChild(reqType);
    taskFields.appendChild(document.createElement("br"));
    taskFields.appendChild(document.createElement("br"));
    taskFields.appendChild(document.createElement("br"));
    taskFields.appendChild(document.createElement("br"));
    taskFields.appendChild(document.createElement("br"));
    taskFields.appendChild(document.createElement("br"));
    taskFields.appendChild(reqName_label);
    taskFields.appendChild(reqName);
}
populateFeat();

