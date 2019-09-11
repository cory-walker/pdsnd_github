import time
import pandas as pd
import numpy as np
""" Dictionary documentations """
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = {'jan' : 1,
          'feb' : 2,
          'mar' : 3,
          'apr' : 4,
          'may' : 5,
          'jun' : 6}

dows = {'sun' : 6,
       'mon' : 0,
       'tue' : 1,
       'wed' : 2,
       'thu' : 3,
       'fri' : 4,
       'sat' : 5,}

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
    cities = ['chicago','washington','new york']
    city = ''
    while city != 'chicago':
        city = input('Please select a city: chicago, new york, or washington: ').lower()
        if city in cities:
            break
            
    # TO DO: get user input for month (all, january, february, ... , june)
    month = ''
    while month != 'all':
        month = input('Please select a month: all, jan, feb, mar, apr, may, jun: ').lower()
        if month in months:
            break
            
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = ''
    while day != 'all':
        day = input('Please select a day of the week: all, sun, mon, tue, wed, thu, fri, sat: ').lower()
        if day in dows:
            break
            
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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    
    if month != 'all':
        mth = months.get(month)
        df = df[df['month'] == mth]
        
    if day != 'all':
        dy = dows.get(day)
        df = df[df['day_of_week'] == dy]
        
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['hour'] = df['Start Time'].dt.hour
    df['station_combination'] = 'Start: ' + df['Start Station'] + ', End: ' + df['End Station']
    df['duration'] = df['End Time'] - df['Start Time']
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    print('\nThe most common month is: ', df['month'].mode()[0]) # TO DO: display the most common month
    print('\nThe most common day of week is: ', df['day_of_week'].mode()[0]) # TO DO: display the most common day of week
    print('\nThe most common hour is: ', df['hour'].mode()[0]) # TO DO: display the most common start hour 
    print('\nThe least common hour is: ', df['hour'].mode()[-1])
    print('\nThe least common day of week is: ', df['day_of_week'].mode()[-1])
    print('\nThe least common day of month is: ', df['month'].mode()[-1])
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    print('\nThe most common Start Station is: ', df['Start Station'].mode()[0]) # TO DO: display most commonly used start station
    print('\nThe most common End Station is: ', df['End Station'].mode()[0]) # TO DO: display most commonly used end station
    print('\nThe most common Station combination is: ', df['station_combination'].mode()[0]) # TO DO: display most frequent combination of start station and end station trip

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    print('\nTotal travel time: ', df['duration'].sum()) # TO DO: display total travel time
    print('\nMean travel time: ', df['duration'].mean()) # TO DO: display mean travel time

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    print('\nuser type count: ', df['User Type'].value_counts()) # TO DO: Display counts of user types
    
    if 'Gender' in df:
        print('\ngender type count: ', df['Gender'].value_counts()) # TO DO: Display counts of gender
    else:
        print('\nGener type is not present in this data')
        
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        print('\nEarliest Birth year: ', int(df['Birth Year'].min())) 
        print('\nMost recent Birth year: ', int(df['Birth Year'].max()))
        print('\nMost common Birth Year: ', df['Birth Year'].mode()[0])
        
    else:
        print('\nBirth Years are not present in this data')
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_stats(stat_name):
    answer = ''
    while answer != 'y':
        answer = input('\nWould you like to see the {} stats? (y/n) '.format(stat_name)).lower()
        if answer == 'n':
            break
            
    return answer

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        if display_stats('time') == 'y':
            time_stats(df)
        
        if display_stats('station') == 'y':
            station_stats(df)
        
        if display_stats('trip duration') == 'y':
            trip_duration_stats(df)
        
        if display_stats('user') == 'y':
            user_stats(df)

        restart = input('\nWould you like to restart? (y/n).\n')
        if restart.lower() != 'y':
            break


if __name__ == "__main__":
	main()
