class Player {
    constructor(name) {
        this.name = name;
    }
}

const namespace = '/test'; //adresse du WebSocket
var socket = io(namespace);

var currentPlayer = new Player(""); //PAS BO de faire comme ça mais bon je suis fatigué




function login(){  //NE MARCHE QUE SUR SAFARI
    alert('Login?')
    var name = $('#name').val();
    currentPlayer.name = name;
    socket.emit('login', {name: name});
    switchPage();
}

function buzz(){
    socket.emit('buzz', {name: currentPlayer.name})
}

// $('#loginButton').click(function(){  //BIZZARE NE MARCHE PAS SUR MOBILE
//     var name = $('#name').val(); 
//     currentPlayer.name = name;
//     socket.emit('login', {name: name});
//     switchPage();
// })

// $('#buzzButton').click(function(){  
//     socket.emit('buzz', {name: currentPlayer.name})
// })


socket.on('loginResponse', function(msg,cb){
    var playerName = $('#name').val(); 
    $('#log').append(msg.data + " <br>");
})

socket.on('buzzResponse', function(msg,cb){
    var playerName = $('#name').val(); //Il faudra récuperer current Player.name
    if (msg.data == playerName){
        $('#log').append( "YOU BUZZED! <br>");
    } else{
        $('#log').append('Player: ' + msg.data + " BUZZED! <br>");
    }
    
})


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

// function currentUrl(){
//     var a = window.location.href;
//     return (a.substr(0,a.length-1));
// }

// function test() {
//     // var b = "/";
     

//     alert(currentUrl());
    
// }

