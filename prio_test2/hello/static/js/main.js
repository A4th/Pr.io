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
