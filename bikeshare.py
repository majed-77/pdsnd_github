import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

#CITY_DATA = {'chicago': 'chicago.csv',
#             'new york city': 'new_york_city.csv',
#             'washington': 'washington.csv'}



def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Enter the city: chicago, new york city, or washington: ').lower()
    while city not in ['chicago', 'new york city', 'washington']:
        city = input("Sorry your input should be>> chicago, new york city or washington: ").lower()

    # get user input for month (all, january, february, ... , june)
    month = input('Enter the month: january, february, march, april, may, june or all: ').lower()
    while month not in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
        month = input('Sorry your input should be>> january, february, march, april, may, june or all').lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Enter the day : sunday, ... friday, saturday or all: ').lower()
    while day not in ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']:
        day = input('Sorry your input should be>> sunday, ... friday, saturday or all').lower()
    print('-' * 40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # extract day from Start Time into new column called month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Common Month:', popular_month)
    print('Most Common Month:', popular_month)
    # display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most Common day:', popular_day)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Common Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Commonly Start Station:', start_station)
    print('Most Commonly Popular Start Station:', popular_start_station)

    # display most commonly used end station
    end_station = df['End Station'].mode()[0]
    popular_end_station = df['End Station'].mode()[0]
    print('Most Commonly End Station:', end_station)
    print('Most Commonly Popular End Station:', popular_end_station)

    # display most frequent combination of start station and end station trip
    print("The most frequent combination of start station and end station trip")
    most_common_start_and_end_stations = df.groupby(['Start Station', 'End Station']).size().nlargest(1)
    print(most_common_start_and_end_stations)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("total travel time is: ", total_travel_time)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('mean travel time is:', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # Display counts of gender
    try:
        counts_of_gender = df['Gender'].value_counts()
        print(counts_of_gender)
    except KeyError:
        print("\ncounts_of_gender:\nNo data available for gender in this city.")

    # Display earliest, most recent, and most common year of birth
    try:
        most_common_year = df['Birth Year'].mode()[0]

        most_recent_year = df['Birth Year'].max()

        earliest_year = df['Birth Year'].min()

        print('\nMost common year is:', int(most_common_year),
              '\nMost recent year is:', int(most_recent_year),
              '\nEarliest year is:', int(earliest_year))
    except KeyError:
        print("\nmost recent, and most common year of birth:\nNo data available for brith year in this city.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def display_data(df):
    x=0
    i=0
    #Display 5 rows of individual trip data
    user_input=input('Would you like to view 5 rows of individual trip data? Enter yes or no? ').lower()
    if user_input not in ['yes', 'no']:
        print('invalid choice, pleas enter yes or no ')
        user_input=input('Would you like to view 5 rows of individual trip data? Enter yes or no? ').lower()
    elif user_input != 'yes':
        print('Thanks')
    else:
        while x+5 < df.shape[0]:
            print(df.iloc[x:i+5])
            i += 5
            user_input = input('if Would you like to view more 5 rows of raw data? enter yes or no ').lower()
            if user_input != 'yes':
                print('Thanks')
                break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
