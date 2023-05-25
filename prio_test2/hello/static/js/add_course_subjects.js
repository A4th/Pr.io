"use strict";

function submitAddCourseSubjectsForm(form) {
    // reset error bar on each form submission
    hideErrorBar();

    // Get selected subjects
    let selectedSubjects = [];
    document.getElementsByName("chosenSubs").forEach((subjChkbox) => {
        if (subjChkbox.checked)
            selectedSubjects.push(subjChkbox.value);
    });

    // Input validation
    // Required at least one subject to be added
    if (selectedSubjects.length == 0) {
        showErrorBar(`Error: Please select at least one subject to add.`);
        return;
    }

    // No validation errors, submit form
    form.submit();
}
