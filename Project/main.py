import time
import pandas as pd
import numpy as np

import get_filters_module as gfm
import load_module as lm
import time_stats_module as tsm
import station_stats_module as ssm
import trip_duration_module as tdm
import user_stats_module as usm

while True:

    city, month, day = gfm.get_filters()
    print("Filters:\n   city = {}\n   month = {}\n   day = {}\n".format(city, month, day))
    df = lm.load_data(city, month, day)
    tsm.time_stats(df,month,day)
    ssm.station_stats(df)
    tdm.trip_duration_stats(df)
    usm.user_stats(df)

    restart = ''
    while restart not in ('yes' 'no'):
        restart = input('\nWould you like to restart? Enter yes or no.').lower()
        if restart not in ('yes' 'no'):
            print("    '{}' is not a valid option".format(restart))

    if restart == 'no':
        break
