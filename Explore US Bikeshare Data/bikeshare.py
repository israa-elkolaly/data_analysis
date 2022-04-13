import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']
DAYS = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ''
    month = ''
    day=''
    while city not in CITY_DATA:
        print("please enter correct name of the city you want (chicago, new york city, washington) ")
        city=input().lower()
    
        
    # TO DO: get user input for month (all, january, february, ... , june)
    while month not in MONTHS and month != "all":
        print("please select all or  correct name of month you want ('january', 'february', 'march', 'april', 'may', 'june') ")
        month=input().lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while day not in DAYS and day != "all":
        print("please select all or correct name of day you want ('sunday','monday','tuesday','wednesday','thursday','friday','saturday') ")
        day=input().lower()

    print('-'*40)
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
    df = pd.read_csv(r'{}'.format(CITY_DATA[city]))

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name.str.lower()


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]
    

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    commn_month_index = df['month'].mode()[0]-1
    print('the most common month is {}'.format(MONTHS[commn_month_index]))

    # TO DO: display the most common day of week
    print('the most common day of week is {}'.format(df['day_of_week'].mode()[0]))


    # TO DO: display the most common start hour
    df['hour']=df['Start Time'].dt.hour
    print('the most common start hour is {}'.format(df['hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('the most commonly used start station is {}'.format(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station

    print('the most commonly used end station is {}'.format(df['End Station'].mode()[0]))
    
    # TO DO: display most frequent combination of start station and end station trip
    print('the most frequent combination of start station and end station trip is {}'.format(df[['Start Station','End Station']].mode().loc[0]))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time 
    print('the total travel time is {}'.format(df['Trip Duration'].sum()))


    # TO DO: display mean travel time
    print('the mean travel time is {}'.format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('the counts of user types is {}'.format(df['User Type'].value_counts()))



    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
         print('the counts of user types is {}'.format(df['Gender'].value_counts()))


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('the earliest year of birth is {}'.format(df['Birth Year'].min()))
        print('the most recent year of birth is {}'.format(df['Birth Year'].max()))
        print('the most common year of birth is {}'.format(df['Birth Year'].mode()[0]))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        print("Dataset Description \n",df.describe())
        print("Do you want to explore the dataset? yes to explore \n")
        x=input().lower()
        c=10
        while x == 'yes':
            print(df.head(c))
            print("Do you want to explore more? yes to explore \n")
            x=input().lower()
            c = c+5

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
