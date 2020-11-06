
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