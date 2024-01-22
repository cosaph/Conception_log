# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    tp1.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ensai <ensai@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/01/22 13:31:23 by ensai             #+#    #+#              #
#    Updated: 2024/01/22 13:35:12 by ensai            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import datetime
import pytz

def get_current_time():
    tz = pytz.timezone('Indian/Reunion')
    current_time = datetime.datetime.now(tz)
    return current_time

if __name__ == '__main__':
    current_time = get_current_time()
    print("Heure à La Réunion :", current_time)