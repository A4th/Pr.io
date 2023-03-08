"use strict";

function inputsFunc() {
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

    alert(`Added subject: ${added[0]} \nNo. of Units: ${added[1]} \nstart time: ${added[2]} \nend time: ${added[3]}`);

    for (let input of inputs){
        document.querySelector(input).value = '';
    }                        

}