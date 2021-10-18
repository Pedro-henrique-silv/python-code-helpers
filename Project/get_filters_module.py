def filter_aux(filter_selected, filter_options):
    """
    Show options to filter considering if it was select day or month

    Input:
        (str) filter_selected - city, date time, day or month
        (str) filter_options - list of options

    Returns:
        (str) option_selected - result of the filter input
    """
    print("\nPlease select one of the options bellow to filter a {}\n".
    format(filter_selected))
    for i in range((len(filter_options))):
        print("    To select {}, type {}".format(filter_options[i],
        str(int(i+1))))

    #Checks if it's a valid value
    input_erro = True
    while input_erro:

        input_aux = input("    ")
        try:
            input_aux = int(input_aux)
            if 0 < input_aux < len(filter_options) + 1:
                input_erro = False
            else:
                print("    '{}' is not an option, please select a number between 1 and {}".
                format(str(input_aux),str(len(filter_options))))

        except:
            print("    '{}' is not an option, please select a number between 1 and {}".
            format(input_aux,str(len(filter_options))))

    #check the filter select and show the options to this filter
    return filter_options[input_aux-1].lower()


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
    date_filter_options = ['month', 'day', 'both', 'all']
    month_filter_options = ['January', 'February', 'March', 'April', 'May', 'June']
    day_filter_options = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday',
    'Friday', 'Saturday']

    #I choose to do by this way to make easyer to the final user to select
    #option 'all', because it cold be a lot off ways to select this by text

    #uses filter_aux to check input errors
    city = filter_aux('city',city_filter_options)
    date_filter_selected = filter_aux('date time',date_filter_options)

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
