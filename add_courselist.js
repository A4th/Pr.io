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
            return;
        }

        // TODO:  add error checking for request
        const course_filename = univ + "_" + college + "_" + courseSelect.value + ".json";
        fetch("https://raw.githubusercontent.com/A4th/Pr.io/main/Courselist/" + course_filename)
            .then((response) => response.json())
            .then((data) => console.log(data));
    };
}


// populate course selection with options
populateDegProgOptions();
