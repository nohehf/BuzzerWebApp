class Player {
    constructor(name) {
        this.name = name;
    }
}

var currentPlayer = new Player(""); //PAS BO de faire comme ça mais bon je suis fatigué

function buzz(){
    msg();
}

// Show name when buzz
function login(){
    name = document.getElementById("name").value;
    currentPlayer.name = name;
    alert(currentPlayer.name)
    httpPost("http://127.0.0.1:5000/buzzer",name);
}

function msg() {
    var playerName = "";//AJOUTER LE NOM DE L'objet currentPlayer
    if (playerName == "") {
        alert("Please LOGIN!");
    } else {
        alert("You just buzzed as: "+ playerName);
    }

}


function httpGet(url) {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        document.getElementById("test").innerHTML = this.responseText;  //A MODIFIER
        }
    };
    xhttp.open("GET", url, false);
    xhttp.send();
}

function httpPost(url,data) {
    var xhttp = new XMLHttpRequest();
    xhttp.setRequestHeader('', data); // JE M'en suis arrété ici
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        document.getElementById("test").innerHTML = this.responseText;  //A MODIFIER
        }
    };
    xhttp.open("POST", url, false);
    xhttp.send();
}

function sendName(){

}



function test() {
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
          if (this.readyState == 4 && this.status == 200) {
            document.getElementById("test").innerHTML = this.responseText;
          }
        };
        xhttp.open("GET", "http://127.0.0.1:5000/hello_world", false);
        xhttp.send();
}


//TO USE FETCH: (marche pas encore)

// function test(){
//     fetch('http://127.0.0.1:5000/hello_world')
//     .then(
//       function(response) {
//         if (response.status !== 200) {
//           console.log('Looks like there was a problem. Status Code: ' +
//             response.status);
//           return;
//         }
  
//         // Examine the text in the response
//         response.text().then(function(data) {
//           console.log(data);
//         });
//       }
//     )
//     .catch(function(err) {
//       console.log('Fetch Error :-S', err);
//     });
  
// }

