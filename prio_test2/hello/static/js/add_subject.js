"use strict";

function submitForm(form) {
    // reset error bar on each form submission
    hideErrorBar();
    let requiredFields = [ "#subName", "#numUnits" ];

    // If one of the start time, end time, and subject days have value,
    // then ALL other fields in the group must have values
    // NOTE: requirement for subjDays is handled in a different block since it has no single id
    const newStart = document.getElementById("start").value;
    const newEnd = document.getElementById("end").value;
    let newSubDays = [];
    document.getElementsByName("subjDays").forEach((dayCheckbox) => {
        if (dayCheckbox.checked)
            newSubDays.push(dayCheckbox.value);
    });
    // console.log(newSub, newStart, newEnd, newSubDays);
    const schedRequired = newStart != '' || newEnd != '' || newSubDays.length > 0;
    if (schedRequired) {
        requiredFields.push("#start", "#end")
    }
    // console.log(requiredFields);

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

    // If start/end time is set, require at least one day
    if (schedRequired && newSubDays.length == 0) {
        showErrorBar(`Error: Please select the days for the subject schedule.`);
        return;
    }

    // Ensure that start time < end time
    if (schedRequired && newStart >= newEnd) {
        showErrorBar(`Error: Start Time must be before End Time.`);
        return;
    }

    // Check if subject name already exists
    const newSub = document.getElementById("subName").value;
    const subjects = JSON.parse(document.getElementById('subjects-data').textContent);
    const currsubject = document.getElementById("currsubject")?.value;
    // console.log(newSub, Object.keys(subjects));
    if (Object.keys(subjects).find(subject => subject == newSub && subject != currsubject)) {
        showErrorBar(`Error: Subject <b>${newSub}</b> already exists.`);
        return;
    }

    // Check if subject's time schedule conflicts with another subject
    if (newSubDays.length > 0 && newStart != '' && newEnd != '') {
        for (const subject in subjects) {
            // If we are in edit subject page, the newest subject should not conflict with itself
            if (subject == currsubject) continue;
            // console.log(subject, subjects[subject]);

            // If two subjects are not done in same day, then they won't overlap
            const subDays = subjects[subject].subjDays ?? [];
            // TODO: use more efficient intersection algorithm
            const overlapDays = subDays.filter((day) => newSubDays.includes(day))
            // console.log(overlapDays);
            if (overlapDays.length == 0) continue;

            // NOTE: since start and end times are the same for each day, we only compare once
            const subStart = subjects[subject].start;
            const subEnd = subjects[subject].end;

            // overlap range is given by overlapStart = max(start1, start2) and overlapEnd = min(end1, end2))
            // Hence if overlapStart is less than overlapEnd, there is no overlap
            const overlapStart = (subStart > newStart) ? subStart : newStart;       // MAX start
            const overlapEnd = (subEnd < newEnd) ? subEnd : newEnd;                 // MIN endd
            // console.log("Overlap time", overlapStart, overlapEnd);
            if (overlapStart < overlapEnd) {
                // TODO: use AM/PM format for time
                // NOTE: Only prints days with overlap
                showErrorBar(`Error: Schedule conflicts with <b>${subject} (${subStart}-${subEnd} ${overlapDays.join(" ")})</b>.`);
                return;
            }
        }
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
