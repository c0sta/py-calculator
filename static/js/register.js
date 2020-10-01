/**
 * Pego os campos de username e password
 */
var fields = document.getElementsByTagName('input');
// Pego o botão de submit do formulário
var submitButton = document.getElementById('submit')

var url = "/register"
//Pega os valores inseridos nos inputs e salva em váriaveis para enviar para o Backend



$(function() {
    $('#submit').click(function(event) {
        event.preventDefault()
        $.ajax({
            url: '/register',
            data: $('#form').serialize(),
            type: 'POST',
            success: function(response) {
                console.log(response);
            },
            error: function(error) {
             console.log(error)
            }
        })
    });
});


