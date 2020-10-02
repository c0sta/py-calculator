

import datetime
from models.userModel import User

from sqlalchemy.sql.functions import current_user
from sqlalchemy import update

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
            
            user = User.query.filter_by(username=username).first()
            users = User.users_table
            
            users.update().where(users.c.id == user.id).values(history=history_array)

            return 'Adicionado ao histórico!'
        else:
            return "Erro ao adicionar ao histórico, algum valor está faltando"

    def get_history():
            return history_array

