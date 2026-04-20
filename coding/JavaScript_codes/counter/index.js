const countNumber = document.getElementById("countLabel");
countNumberValue = Number(countNumber);


document.getElementById("decreaseBtn").onclick = function(){
    countNumberValue --;
    document.getElementById("countLabel").textContent = countNumberValue;
}
document.getElementById("increaseBtn").onclick = function(){
    countNumberValue ++;
    document.getElementById("countLabel").textContent = countNumberValue;
}
document.getElementById("resetBtn").onclick = function(){
    countNumberValue = 0;
    document.getElementById("countLabel").textContent = countNumberValue;
}