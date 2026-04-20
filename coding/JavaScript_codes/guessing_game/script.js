let number  = Math.random() * 100;
number = Math.floor(number);


console.log(number);

let userNumber;
let running = true;
let points = 0;


const result = document.getElementById("h2Id");
const input = document.getElementById("inputId");
const button = document.getElementById("buttonId");


    button.onclick = function(){
        userNumber = input.value;
        if(userNumber == number){
            result.innerText = "Right!";
            number  = Math.random() * 100;
            number = Math.floor(number);
            console.log(number);
        } else{
            result.innerText = "Wrong!";
        }
        running = false;
    }
