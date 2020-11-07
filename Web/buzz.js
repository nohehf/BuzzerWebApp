
// Called by clicking the buzz button
function onClick(){
    msg();
}

// a simple test function
function msg() {
    var playerName = document.getElementById("name").value;
    if (playerName == "") {
        alert("Veuillez entrer un nom !");
    } else {
        alert("You just buzzed as: "+ playerName);
    }

}


function httpGet (url) {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", url, false); // false for synchronous request  ATTENTION CHANGER URL1
    xmlHttp.send();
    // alert(xmlHttp.responseText) //A ENLEVER
    return xmlHttp.response;  
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

