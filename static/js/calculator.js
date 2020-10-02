// Pega o input da calculadora
let input = document.querySelector(".input");
// Pega os botões numéricos e de operações
let buttons = document.querySelectorAll('[name="digit"], [name="operation"]');

input.addEventListener("change", () => {}); // Faz com que o input seja atualizado quando o botão for clicado

/* Percorre a lista de botões e adiciona
um eventListener, para que quando qualquer um desses botões - [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, +, -, /, x] - for clicado o seu texto seja concatenado no input da calculadora
*/
buttons.forEach((button) => {
  button.addEventListener("click", (event) => {
    event.preventDefault();
    let clickedButton = event.target.textContent;
    // console.log(clickedButton)
    let operationText = (input.value += clickedButton)
    // console.log(operationText, clickedButton.value);
  });
});

/**
 * Botão que limpa o input da calculadora, essa função define o valor do input para uma 
 * string vazia = ""
 */
let clearButton = document.querySelector('[name="clear"]').addEventListener('click', (event) => {
  event.preventDefault();
  input.value = "";
})


$(function() {
  $('#calculate').click(function(event) {
      event.preventDefault()
      let mathAccount = input.value
      let splited = mathAccount.match(/[^\d()]+|[\d.]+/g)
      console.log(splited)
      
      let data = {
        numberOne: splited[0],
        numberTwo: splited[2],
        operator: splited[1],
      }
      
      $.ajax({
          url: '/calculate',
          data: $('#operation').serialize(),
          type: 'POST',
          success: async function(response) {
              console.log('Resultado calculado com sucesso', response)
          },
          error: function(error) {
           console.log(error)
          }
      }).done(function(arg){
        $('input:text').val(arg.resultado)
      })
  });
});
