def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    #calendar is used to simplify the month display
    import calendar
    import time
    import pandas as pd

    start_time = time.time()

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

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
