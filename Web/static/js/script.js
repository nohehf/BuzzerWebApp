class Player {
    constructor(name) {
        this.name = name;
    }
}


var currentPlayer = new Player(""); //PAS BO de faire comme ça mais bon je suis fatigué


function login(){
    var name = document.getElementById('name').value
    currentPlayer.name = name;


    const url = 'http://192.168.1.167:5000/login';
    const options = {
        method: 'POST',
        body: JSON.stringify(currentPlayer)
    };
    
    fetch(url,options)
        .then(response => {console.log(response.status)})
    
    switchPage();
}

function buzz(){

    const url = 'http://192.168.1.167:5000/buzzer';
    const data = {
        'name': currentPlayer.name
    };
    const options = {
        method: 'POST',
        body: JSON.stringify(data)
    };
    
    fetch(url,options)
        .then(response => {console.log(response.status)})
    console.log('BUZZ POST SEND');
}

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




function test() {
    document.getElementById('buzzerDiv').style.display = 'block';
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

