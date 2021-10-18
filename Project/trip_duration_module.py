def convert_seconds(time_secods):
    """convert seconds to day, hour, month and seconds

        Input - time in secons
        Output - array with converted time

    """
    int_year, mod_year = time_secods//(12*30*24*60*60), time_secods%(12*30*24*60*60)
    int_month, mod_month = mod_year//(30*24*60*60), mod_year%(30*24*60*60)
    int_day, mod_day = mod_month//(24*60*60), mod_month%(24*60*60)
    int_hour, mod_hour = mod_day//(60*60), mod_day%(60*60)
    int_minute, int_second = mod_hour//60, int(mod_hour%60)

    #create an auxiliar array to print the total time travel converted
    return [int_year, int_month, int_day, int_hour, int_minute, int_second]

def print_trip_stats(message,aux_trip_value):
    """convert seconds to day, hour, month and seconds

        Input:
            message - initial message
            aux_trip_value - array with years, months, days, hours, minutes
            and seconds

    """
    aux_trip_str = ['year', 'month', 'day', 'hour', 'minute', 'second']

    for i in range(len(aux_trip_value)):

        #adjust message to plural
        if aux_trip_value[i] > 1:
            message += " {} {}s,".format(str(aux_trip_value[i]).
            zfill(2),aux_trip_str[i] )
        #in case the time is singular
        elif aux_trip_value[i] > 0:
            message += " {} {},".format(str(aux_trip_value[i]).
            zfill(2),aux_trip_str[i] )

    ind_last_comma = message[0:-1].rfind(',')

    message = message[0:ind_last_comma] + ' and' + message[ind_last_comma+1:-1]

    print(message)

def trip_duration_stats(df):
    import time
    import pandas as pd
    import numpy as np
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    aux_total_trip_value = convert_seconds(int(df['Trip Duration'].sum()))
    aux_mean_trip_value = convert_seconds(int(df['Trip Duration'].mean()))


    #initate print total message
    total_message = "    The total trip time is"
    #uses aux function print_trip_stats to print total stats'
    print_trip_stats(total_message, aux_total_trip_value)

    #initate print mean message
    mean_message = "    The mean trip time is"
    #uses aux function print_trip_stats to print mean stats'
    print_trip_stats(mean_message, aux_mean_trip_value)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
