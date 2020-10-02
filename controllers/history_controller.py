

import datetime


history_array = [] 

class HistoryController():

    # Método que cria a mensagem que será adicionado ao histórico
    def create_history_message(username, operation, result):

        if username and operation and result:
            today = datetime.datetime.now()
            hour = "{}:{}".format(today.hour, today.minute)
            print(hour)
            
            history_message = '{} - {} : {} = {}'.format(username, hour, operation, result)
            
            history_array.append(history_message)
            print(history_array)
            return 'Adicionado ao histórico!'
        else:
            return "Erro ao adicionar ao histórico, algum valor está faltando"

    def get_history():
            return history_array

