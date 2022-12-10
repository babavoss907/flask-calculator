let numbers = [];
let result = 0;
let operator = null;
function calculate(char){
    document.getElementById('display').value += char;
    numbers.push(char);
}
function empty(){
    var value = document.getElementById('display').value = '';
}
function backspace(){
    var value = document.getElementById('display').value;
    document.getElementById('display').value = value.substr(0, value.length - 1);
}
function equal(){
    var result = eval(document.getElementById('display').value);
    document.getElementById('display').value = result;
    let data = {
        'numbers': numbers
        // 'operator': operator
    };
    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function(){
        if(this.readyState == 4 && this.status == 200){
            let response = JSON.parse(this.responseText);
            result = response.result;
            display.innerHTML = result;
        }
    };
    xhttp.open('POST', '/calculate', true);
    xhttp.setRequestHeader('Content-Type', 'application/json')
    xhttp.send(JSON.stringify(data));
}