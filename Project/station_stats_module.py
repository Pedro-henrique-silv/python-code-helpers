def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    import time
    import pandas as pd
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
