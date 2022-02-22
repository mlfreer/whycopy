// fixing option 1:
var option1_slider = document.getElementById("option1");
var option1_form = document.getElementById("option1_form");
option1_form.value = option1_slider.value;

// fixing option 2:
var option2_slider = document.getElementById("option2");
var option2_form = document.getElementById("option2_form");
option2_form.value = option2_slider.value;

// fixing option 3:
var option3_slider = document.getElementById("option3");
var option3_form = document.getElementById("option3_form");
option3_form.value = option3_slider.value;

// fixing option 4:
var option4_slider = document.getElementById("option4");
var option4_form = document.getElementById("option4_form");
option4_form.value = option4_slider.value;

// fixing option 5:
var option5_slider = document.getElementById("option5");
var option5_form = document.getElementById("option5_form");
option5_form.value = option5_slider.value;


// fixing tokens:
var tokens_slider = document.getElementById("tokens_slider");
var tokens_form = document.getElementById("tokens_form");
tokens_form.value = tokens_slider.value;


// 
var next_button = document.getElementById("NextButton");

function validate()
{
    if ((tokens_form.value)==0)
    {
        next_button.style.visibility = "visible"
    }
    else
    {
        next_button.style.visibility = "hidden"
    }
}

// round to the next multiple of 5
function round5(x)
{
    return Math.ceil(x/5)*5;
}




// resetting the values
function reset_values() {
    next_button.style.visibility = "hidden";

    option1_form.value = 0
    option2_form.value = 0
    option3_form.value = 0
    option4_form.value = 0
    option5_form.value = 0

    option1_slider.value = 0
    option2_slider.value = 0
    option3_slider.value = 0
    option4_slider.value = 0
    option5_slider.value = 0

    tokens_form.value = 100
    tokens_slider.value = 100
}

