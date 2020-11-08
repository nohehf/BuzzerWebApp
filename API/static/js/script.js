class Player {
    constructor(name) {
        this.name = name;
    }
}

const namespace = '/test'; //adresse du WebSocket
var socket = io(namespace);

var currentPlayer = new Player(""); //PAS BO de faire comme ça mais bon je suis fatigué


$('#loginButton').on('click',function(){
    var name = $('#name').val();
    currentPlayer.name = name;
    socket.emit('login', {name: name});
    switchPage();
});

// function login(){
//     var name = document.getElementById('name').value
//     currentPlayer.name = name;


//     const url = currentUrl()+':5000/login';
//     const options = {
//         method: 'POST',
//         body: JSON.stringify(currentPlayer)
//     };
    
//     fetch(url,options)
//         .then(response => {console.log(response.status)})
    
//     switchPage();
// }

$('#buzzButton').click(function(){  
    socket.emit('buzz', {name: currentPlayer.name})
});

// function buzz(){

//     const url = currentUrl() +':5000/buzzer'; //A changer quand sur serveur distant
//     const data = {
//         'name': currentPlayer.name
//     };
//     const options = {
//         method: 'POST',
//         body: JSON.stringify(data)
//     };
    
//     fetch(url,options)
//         .then(response => {console.log(response.status)})
//     console.log('BUZZ POST SEND');
// }

socket.on('loginResponse', function(msg,cb){
    var playerName = $('#name').val(); 
    $('#log').append(msg.data + " <br>");
});

socket.on('buzzResponse', function(msg,cb){
    var playerName = $('#name').val(); //Il faudra récuperer current Player.name
    if (msg.data == playerName){
        $('#log').append( "YOU BUZZED! <br>");
    } else{
        $('#log').append('Player: ' + msg.data + "BUZZED! <br>");
    }
    
});


//Fonction qui permet de changer de "mode" entre login et buzzer (fonctionne dans les 2 sens)
function switchPage(){
    var buzzerDiv = document.getElementById('buzzerDiv');
    var loginDiv = document.getElementById('loginDiv');
    if (buzzerDiv.style.display !== "block") {
        // PASSE EN MODE BUZZER
        buzzerDiv.style.display = "block";
        loginDiv.style.display = "none";
        document.title = "BUZZER";
        
    }
    else {
        // PASSE EN MODE LOGIN
        buzzerDiv.style.display = "none";
        loginDiv.style.display = "block";
        document.title = "LOGIN";
    }
}

function msg() {
    var playerName = "test";//AJOUTER LE NOM DE L'objet currentPlayer
    if (playerName == "") {
        alert("Please LOGIN!");
    } else {
        alert("You just buzzed as: "+ playerName);
    }

}


// function httpGet(url) {
//     var xhttp = new XMLHttpRequest();
//     xhttp.onreadystatechange = function() {
//       if (this.readyState == 4 && this.status == 200) {
//         document.getElementById("test").innerHTML = this.responseText;  //A MODIFIER
//         }
//     };
//     xhttp.open("GET", url, false);
//     xhttp.send();
// }

// function httpPost(url,data) {
//     var xhttp = new XMLHttpRequest();
//     xhttp.setRequestHeader('', data); // JE M'en suis arrété ici
//     xhttp.onreadystatechange = function() {
//       if (this.readyState == 4 && this.status == 200) {
//         document.getElementById("test").innerHTML = this.responseText;  //A MODIFIER
//         }
//     };
//     xhttp.open("POST", url, false);
//     xhttp.send();
// }


function currentUrl(){
    var a = window.location.href;
    return (a.substr(0,a.length-1));
}

function test() {
    // var b = "/";
     

    alert(currentUrl());
    
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

