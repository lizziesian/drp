var socket = io.connect('http://' + document.domain + ':' + location.port);

socket.on("connect", function() {
    socket.emit("parental confirmation", {
        data: "User Connected"
    } )
    var form = $( 'form' ).on( 'submit', function( e ) {
        e.preventDefault()
        let result = $("confirm").val()
    } )
} )