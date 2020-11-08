const namespace = '/test'; //adresse de l'event
var socket = io(namespace);

// $('#buttonLogin').click(function(){
//     alert('Login?')
//     var playerName = $('#name').val();
//     socket.emit('login', {name: playerName});
// });
function login(){
    alert('Login?')
    var playerName = $('#name').val();
    socket.emit('login', {name: playerName});
};

$('#buttonBuzz').click(function(){
    var playerName = $('#name').val();
    socket.emit('buzz', {name: playerName})
});

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

// $('#button').click(function(){
//     socket.emit('my_event',{data: 'A random message'});
// });
