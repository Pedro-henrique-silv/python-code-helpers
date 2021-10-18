import time
import pandas as pd
import numpy as np
import calendar
from pprint import pprint #function was found on link below
#https://stackoverflow.com/questions/10279712/how-to-print-dict-in-separate-line

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def filter_aux(filter_selected, filter_options):
    """
    Show options to filter considering if it was select day or month

    Input:
        (str) filter_selected - city, date time, day or month
        (str) filter_options - list of options

    Returns:
        (str) option_selected - result of the filter input
    """
    print("\nPlease select one of the options bellow to filter by a {}\n".
    format(filter_selected))
    for i in range((len(filter_options))):
        print("    {}".format(filter_options[i].title()))

    #Checks if it's a valid value
    input_erro = True
    while input_erro:

        input_aux = input("    ")
        try:
            if input_aux.lower() in filter_options:
                input_erro = False
            else:
                print("    '{}' is not a valid option, please try again".format(input_aux))

        except:
            print("    '{}' is not a valid option, please try again".format(str(input_aux)))

    #check the filter select and show the options to this filter
    return input_aux.lower()
all

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no
        month filter
        (str) day - name of the day of week to filter by, or "all" to apply no
        day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    #Create time options lists
    city_filter_options = ['chicago', 'new york city', 'washington']
    date_filter_options = ['month', 'day', 'both', 'no date filter']
    month_filter_options = ['january', 'february', 'march', 'april', 'may', 'june']
    day_filter_options = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday',
    'friday', 'saturday']


    #uses filter_aux to check input errors
    city = filter_aux('city',city_filter_options)
    date_filter_selected = filter_aux('date time',date_filter_options)
    if date_filter_selected == 'no date filter':
        date_filter_selected = 'all'

    if date_filter_selected == 'all':
        month = 'all'
        day = 'all'
    elif date_filter_selected == 'month':
        month = filter_aux('month',month_filter_options)
        day = 'all'
    elif date_filter_selected == 'day':
        month = 'all'
        day = filter_aux('day',day_filter_options)
    else:
        month = filter_aux('month',month_filter_options)
        day = filter_aux('day',day_filter_options)

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no
        month filter
        (str) day - name of the day of week to filter by, or "all" to apply no
        day filter
    Returns:
        df - pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])


    # extract month and day of week from Start Time to create new columns
    df['month'] = pd.to_datetime(df['Start Time']).dt.month
    #df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['day of week'] = pd.to_datetime(df['Start Time']).dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day of week'] == day.title()]

    return df



def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    #calendar is used to simplify the month display

    start_time = time.time()

    # extract hour from the Start Time column to create an hour column
    df['hour'] = pd.to_datetime(df['Start Time']).dt.hour

    list_time_options = ['month', 'day of week', 'hour']
    filter_option = [month, day, 'all']

    #use for loop to avoid repetions on filter and display
    for i in range(len(list_time_options)):
        aux = list_time_options[i]
        # If there is a filter by month, it would be reduntant display this data
        if filter_option[i] == 'all':

            # uses mode module to find the most popular option
            popular_aux = df[aux].mode()[0]
            #select filter rows off the most popular option then uses
            #filter function to select only the option column
            count_popular_aux = df[df[aux] == popular_aux].filter(
            items=[aux]).count()[0]

            if aux == 'month':
                #uses month_name function to get month name
                print("    The most popular {} is {}, with a count of {} travels".
                format(aux,calendar.month_name[popular_aux],"{:,}".
                format(count_popular_aux)))
            else:
                print("    The most popular {} is {}, with a count of {} travels".
                format(aux,str(popular_aux),"{:,}".format(count_popular_aux)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')

    start_time = time.time()

    df['Trip'] = df['Start Station'] + ' to ' + df['End Station']

    list_station_options = ['Start Station', 'End Station', 'Trip']

    #use for loop to avoid repetions on filter and display
    for aux in list_station_options:

        # uses mode module to find the most popular option
        popular_aux = df[aux].mode()[0]
        #select filter rows off the most popular option then uses
        #filter function to select only the option column
        count_popular_aux = df[df[aux] == popular_aux].filter(
        items=[aux]).count()[0]

        print("    The most popular {} is {}, with a count of {} travels".
        format(aux,popular_aux,"{:,}".format(count_popular_aux)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



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
            #df[aux_stats_var].fillna('Not informed', inplace=True)

            #create an aux frame to help to print results
            aux_count = df[aux_stats_var].fillna('Not informed').value_counts()

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
                filt_user_data = df[df[aux_stats_var].fillna('Not informed') == ind_txt]

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
        print("\n    The selected city has no data about Birth Year stats")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def main():
    while True:
        city, month, day = get_filters()
        print("Filters:\n   city = {}\n   month = {}\n   day = {}\n".format(city, month, day))
        print('-'*40)
        df = load_data(city, month, day)
        df_orig = df

        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        i = 0;
        print_data = ''
        while print_data != 'no':
            print_data = input('\nWould you like to view individual trip data? Enter yes or no.\n    ').lower()
            if print_data not in ('yes' 'no'):
                print("    '{}' is not a valid option".format(print_data))
            elif print_data == 'yes':
                aux = i
                while i < aux+5:
                    print('\n')
                    pprint(df.iloc[i,0:-4].to_dict())
                    #print('\n')
                    i += 1
            
        
        restart = input('\nWould you like to restart? Enter yes or no.\n    ').lower()
        while restart not in ('yes' 'no'):
            print("    '{}' is not a valid option".format(restart))
            restart = input('\nWould you like to restart? Enter yes or no.\n    ').lower()
            
        if restart == 'no':
            break

if __name__ == "__main__":
	main()
