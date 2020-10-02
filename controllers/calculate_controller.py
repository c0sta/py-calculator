
from controllers.history_controller import HistoryController
import datetime
import math
import re
from flask import jsonify



class CalculateController():
    history_controller = HistoryController()

    def calculate(operation, username):
        
        potenciacao = re.split('\s', operation)
       
        if potenciacao[1] == "^":
            num1 = int(potenciacao[0])
            num2 = int(potenciacao[2])
            resultado = pow(num1, num2)
            
            # Cria a mensagem e adiciona ao histórico
            HistoryController.create_history_message(username= username, operation=operation, result=resultado)
            
            return jsonify({'resultado': resultado})

        elif potenciacao[1] == u"\u221A":

            # Realiza o cálculo de radiação
            resultado = math.sqrt(int(potenciacao[2]))

            # Cria a mensagem e adiciona ao histórico
            HistoryController.create_history_message(username=username,  operation=operation, result=resultado)


            return jsonify({'resultado': resultado})
        elif potenciacao[1] == "/":

            # Realiza o cálculo de radiação
            if potenciacao[2] != 0 and potenciacao[0] != 0:
                resultado = eval(operation)
                # Cria a mensagem e adiciona ao histórico
                HistoryController.create_history_message(username=username,  operation=operation, result=resultado)
                return jsonify({'resultado': resultado})
            return jsonify({'resultado': 'Inválido'})

        else:
            
            # Realiza o cálculo de Soma, subtração, multiplicação e divisão
            resultado = eval(operation)
            
            # Cria a mensagem e adiciona ao histórico
            HistoryController.create_history_message(username=username,  operation=operation, result=resultado)

            return jsonify({'resultado': resultado})

    