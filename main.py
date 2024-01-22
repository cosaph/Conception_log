# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ensai <ensai@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/01/22 13:31:23 by ensai             #+#    #+#              #
#    Updated: 2024/01/22 16:00:18 by ensai            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import datetime
import pytz
import logging

logging.basicConfig(filename=None, encoding='utf-8', level=logging.DEBUG)

def get_current_time():
    timezone = pytz.timezone('Indian/Reunion')
    logging.info(f"Lancement du traitement")
    if timezone is None:
        logging.error("aucune timezone n'a été renseignée")
        raise ValueError("aucune timezone n'a été renseignée")
    current_time = datetime.datetime.now(timezone)
    logging.debug(f"Demande d'heure sur le timezone : {timezone}")
    return current_time

if __name__ == '__main__':
    current_time = get_current_time()
    print("Heure à La Réunion :", current_time)