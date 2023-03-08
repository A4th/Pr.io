"use strict";

// Course/Degree program information
// NOTE: For now, we are limited to UPD CoE
//       and the list of BS courses are hardcoded
//       since we need server side scripting if we
//       want to dynamically fetch .json course files
let univ = "UPD";
let college = "College Of Engineering"
let degprogs = [
    "BS Chemical Engineering",
    "BS Civil Engineering",
    "BS Computer Engineering",
    "BS Computer Science",
    "BS Electrical Engineering",
    "BS Electronics Engineering",
    "BS Geodetic Engineering",
    "BS Industrial Engineering",
    "BS Material Science and Engineering",
    "BS Mechanical Engineering",
    "BS Metallurgical Engineering",
    "BS Mining Engineering"
];

function populateDegProgOptions() {
    let courseSelect = document.getElementById("course-select");
    let courseSubjects = document.getElementById("course-subjects");
    let controls = document.getElementById("control-buttons");

    // Ensure first that course selection is empty
    while (courseSelect.length > 0) {
        courseSelect.remove(0);
    }

    // First option tells user to select their course/degree program
    let numCourses = 0;
    courseSelect.options[numCourses++] = new Option("--Choose your Course--", "NONE");

    for (let prog of degprogs) {
        courseSelect.options[numCourses++] = new Option(prog, prog);
    }

    // When a valid course is selected, display subjects
    courseSelect.onchange = function() {
        if (courseSelect.value == "NONE") {
            clearNode(courseSubjects);
            clearNode(controls);
            return;
        }

        // TODO:  add error checking for request
        const course_filename = univ + "_" + college + "_" + courseSelect.value + ".json";
        fetch("https://raw.githubusercontent.com/A4th/Pr.io/main/Courselist/" + course_filename)
            .then((response) => response.json())
            .then((data) => populateSubjectOptions(courseSelect.value, data));
    };
}

function clearNode(node) {
    while (node.hasChildNodes()) {
        node.removeChild(node.lastChild);
    }
}

function populateSubjectOptions(course, subjects_json) {
    // First, clear current list of subjects
    let courseSubjects = document.getElementById("course-subjects");
    let controls = document.getElementById("control-buttons");
    clearNode(courseSubjects);
    clearNode(controls);

    let label = document.createElement('h3');
    label.textContent = `${course} Subjects:`;
    // separate scrollable box for actual subjects
    let subjects_box = document.createElement('div');
    subjects_box.setAttribute("id", "subjects-box");
    subjects_box.setAttribute("class", "scroll");

    courseSubjects.appendChild(label);
    courseSubjects.appendChild(subjects_box);

    // sort subjects so that user can more easily find their choices
    let subjects = Object.keys(subjects_json);
    subjects.sort((s1, s2) => s1.localeCompare(s2));
    let num_subs = 0;
    for (let s of subjects) {
        let id = "subject" + (++num_subs);

        let chk = document.createElement("input");
        chk.setAttribute("type", "checkbox");
        chk.setAttribute("id", id);
        chk.setAttribute("value", s);
        chk.setAttribute("data-subject", s);
        chk.setAttribute("data-units", subjects_json[s]);

        let lbl = document.createElement('label');
        lbl.setAttribute("for", id)
        lbl.textContent = s + ` (${subjects_json[s]} units)`;

        // wrap each entry in span element so that
        // we can easily loop over each element later
        let entry = document.createElement("span");
        entry.appendChild(chk);
        entry.appendChild(lbl);
        entry.appendChild(document.createElement("br"));

        subjects_box.appendChild(entry);
    }

    let add = document.createElement("button");
    add.setAttribute("id", "add-course-subjects-button");
    add.textContent = "Add Subjects"
    add.onclick = function() {
        let subject_chks = document.getElementById("subjects-box");
        // if subjects-box could not be found, probably no course chosen yet
        if (!subject_chks) {
            console.log("Null");
            return;
        }

        let subjects_taken = {};
        for (let i = 1; i <= num_subs; ++i) {
            let id = "subject" + i;
            let chk = document.getElementById(id);

            if (chk?.checked) {
                // TODO: add error cheking in case subjects_json has non-float as value
                subjects_taken[chk.getAttribute("data-subject")] = parseFloat(chk.getAttribute("data-units"));
            }
        }

        // TODO: save subjects to persistent storage
        console.log(subjects_taken);
        if (Object.keys(subjects_taken).length > 0) {
            alert("Subjects taken:\n" + JSON.stringify(subjects_taken));
        }
    };

    controls.appendChild(add);
}


// populate course selection with options
populateDegProgOptions();
