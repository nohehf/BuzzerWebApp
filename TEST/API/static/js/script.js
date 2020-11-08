const namespace = '/test'; //adresse de l'event
var socket = io(namespace);

$('#buttonLogin').click(function(){
    var playerName = $('#name').val();
    socket.emit('login', {name: playerName});
});

$('#buttonBuzz').click(function(){
    var playerName = $('#name').val();
    socket.emit('buzz', {name: playerName})
});

socket.on('response', function(msg,cb){
    $('#log').append(msg.data + " <br>");
});

// $('#button').click(function(){
//     socket.emit('my_event',{data: 'A random message'});
// });
