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

function showTaskDetails(taskEvent) {
    // Ensure that details pane is visible
    let detailsPane = document.getElementById("details-pane");
    detailsPane.style = "display: inline";

    document.getElementById("taskName").value = taskEvent.extendedProps.taskName;
    document.getElementById("taskSubject").value = taskEvent.extendedProps.subject;
    // TODO: provide option to change reqType (requires data from task.taskModel)
    document.getElementById("taskReqType").value = taskEvent.extendedProps.reqType;

    // TODO: Simplify date outputs (contains too much information)
    document.getElementById("taskStart").value = taskEvent.extendedProps.startDate;
    document.getElementById("taskEnd").value = taskEvent.extendedProps.endDate;

    document.getElementById("taskDueDate").value = taskEvent.extendedProps.dueDate;
}
