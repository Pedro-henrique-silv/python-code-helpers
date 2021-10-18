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
            message += " {} {}s,".format(str(aux_trip_value[i]).zfill(2),
            aux_trip_str[i] )
        #in case the time is singular
        elif aux_trip_value[i] > 0:
            message += " {} {},".format(str(aux_trip_value[i]).zfill(2),
            aux_trip_str[i] )

    ind_last_comma = message[0:-1].rfind(',')

    message = message[0:ind_last_comma] + ' and' + message[ind_last_comma+1:-1]

    print(message)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    import time
    import pandas as pd
    import numpy as np

    start_time = time.time()

    stats_var = ['User Type', 'Gender']

    for aux_stats_var in stats_var:
        try:
            #change NaN to 'Not informed' to help print Output
            df[aux_stats_var].fillna('Not informed', inplace=True)

            #create an aux frame to help to print results
            aux_count = df[aux_stats_var].value_counts()

            print("\n    {} stats:\n".format(aux_stats_var))
            #Quantity
            print("        Quantity of trips by {}:\n".format(aux_stats_var))


            for i in range(len(aux_count)):
                print('            {}: {}'.
                format(aux_count.index[i],"{:,}".format(aux_count[i])))

            #trip duration by user
            print("\n        Trip duration by {}:".format(aux_stats_var))

            for ind_txt in aux_count.index:
                print('\n            {}:'.format(ind_txt))

                #create a filter aux frame
                filt_user_data = df[df[aux_stats_var] == ind_txt]

                #uses convert_seconds fucntion to get an array with time spent
                aux_total_trip_filt = convert_seconds(
                int(filt_user_data['Trip Duration'].sum()))
                #initate print total message
                message_user_tot = "            The total trip time is"
                #uses aux function print_trip_stats to print total stats'
                print_trip_stats(message_user_tot, aux_total_trip_filt)

                #uses convert_seconds fucntion to get an array with time spent
                aux_total_trip_filt = convert_seconds(
                int(filt_user_data['Trip Duration'].mean()))
                #initate print mean message
                message_user_mean = "            The mean trip time is"
                #uses aux function print_trip_stats to print total stats'
                print_trip_stats(message_user_mean, aux_total_trip_filt)

        except:
            print("\n    The selected city has no data about {} stats:".
            format(aux_stats_var))

    # Display earliest, most recent, and most common year of birth

    try:
        earliest_by = int(df['Birth Year'].min())
        most_recent_by = int(df['Birth Year'].max())
        most_common_by = int(df['Birth Year'].mode()[0])
        most_common_by_count = df[df['Birth Year'] == most_common_by].filter(
        items=['Birth Year']).count()[0]
        nan_values = df['Birth Year'].isnull().sum()

        print("\n    Birth Year stats:\n")

        print("        Earliest Birth Year: {}".format(earliest_by))
        print("        Most recent Birth Year: {}".format(most_recent_by))
        print("        Most common Birth Year is {}, with {} people".
        format(most_common_by,"{:,}".format(most_common_by_count)))
        print("        The selected data has {} not registers with non informed Birth Year".
        format("{:,}".format(nan_values)))


    except:
        print("\n    The selected city has no data about birth year stats")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
