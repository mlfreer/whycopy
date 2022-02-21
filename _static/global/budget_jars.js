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



// resetting the values
function reset() {
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

// updating value from x to y:
function update_value(x,y) {
    a = parseFloat(tokens_form.value)
    b = parseFloat(x.value)
    c = parseFloat(y.value)

    if ((x.id=="tokens_form") || (x.id=="tokens_slider"))
    {
        diff = (b-c)/5

        option1 = parseFloat(option1_form.value)
        option2 = parseFloat(option2_form.value)
        option3 = parseFloat(option3_form.value)
        option4 = parseFloat(option4_form.value)
        option5 = parseFloat(option5_form.value)
//        window.alert(option1-diff)
        if ((b<=c) && (option1-diff <=100) && (option2-diff <=100) && (option3-diff <=100) && (option4-diff <=100) && (option5-diff <=100))
        {
            temp = parseFloat(x.value)
            y.value = temp.toFixed(2);
            option1_form.value = (option1 - diff).toFixed(2);
            option2_form.value = (option2 - diff).toFixed(2);
            option3_form.value = (option3 - diff).toFixed(2);
            option4_form.value = (option4 - diff).toFixed(2);
            option5_form.value = (option5 - diff).toFixed(2);

            option1_slider.value = (option1 - diff).toFixed(2);
            option2_slider.value = (option2 - diff).toFixed(2);
            option3_slider.value = (option3 - diff).toFixed(2);
            option4_slider.value = (option4 - diff).toFixed(2);
            option5_slider.value = (option5 - diff).toFixed(2);
        }
        else
        {
            if ((b>c) && (option1-diff >=0) && (option2-diff  >=0) && (option3-diff  >=0) && (option4-diff  >=0) && (option5-diff  >=0))
            {
                temp = parseFloat(x.value)
                y.value = temp.toFixed(2);
                option1_form.value = (option1 - diff).toFixed(2);
                option2_form.value = (option2 - diff).toFixed(2);
                option3_form.value = (option3 - diff).toFixed(2);
                option4_form.value = (option4 - diff).toFixed(2);
                option5_form.value = (option5 - diff).toFixed(2);

                option1_slider.value = (option1 - diff).toFixed(2);
                option2_slider.value = (option2 - diff).toFixed(2);
                option3_slider.value = (option3 - diff).toFixed(2);
                option4_slider.value = (option4 - diff).toFixed(2);
                option5_slider.value = (option5 - diff).toFixed(2);
            }
            else
            {
                temp = parseFloat(y.value)
                x.value = temp.toFixed(2);

            }
        }
    }
    else
    {
        if (a-b+c >= 0) {
            temp =a-b+c;
//            if ((b-c<=1) && (b-c>=-1)) {window.alert(b-c)}
            tokens_form.value=temp.toFixed(2);
//            window.alert(tokens_form.value)
            tokens_slider.value = tokens_form.value
            temp = parseFloat(x.value)
            y.value = temp.toFixed(2);
        }
        else
        {   
            temp = parseFloat(y.value)
            x.value=temp.toFixed(2)
        }
    }

    if ((tokens_form.value>100) || (tokens_slider.valu>100) )    
    {
        reset()
    }
}


// to operationlize the buttons
function dec(form,slider) {
    a = parseFloat(form.value)
    if (a >= 1) {       
        temp = parseFloat(form.value)
        temp = temp-1
        form.value=temp.toFixed(2)
//        window.alert(slider.value)
        update_value(form,slider)
    };
}

function inc(form,slider) {
    a = parseFloat(form.value)
    if (a <= 99) {       
        temp = parseFloat(form.value)
        temp = temp+1
        form.value=temp.toFixed(2)
        update_value(form,slider)
    };
}

