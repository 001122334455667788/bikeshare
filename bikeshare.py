import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }
months=['january', 'february', 'march', 'april', 'may', 'june'] #list for months
Days=['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday' ] #list for days
cities =['Chicago', 'New York', 'Washington']
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # ask user to input a specific city
    city = input("\nWhich city would you like to see data about?: chicago, new york, washington \n").lower()
    # if user entered a wrong choice, program ask him to choose a valid choice
    while (city not in CITY_DATA):
        print("enter a valid choice")
        city = input("Which city would you like to see data about?: chicago, new york, washington \n").lower()

    # ask user to input a specific month
    month = input('\nWhich month would you like to see data about?: all, january, february, ... , june \n').lower()
    # if user entered a wrong choice, program ask him to choose a valid choice
    while (month != 'all' and month not in months):
        print('please enter a valid choice')
        month = input('Which month would you like to see data about?: all, january, february, ... , june \n').lower()

    # ask user to input a specific month
    day = input('\nWhich day would you like to see data about?: all, monday, tuesday, ... sunday \n').lower()
    # if user entered a wrong choice, program ask him to choose a valid choice
    while (day != 'all' and day not in Days):
        print('please enter a valid choice')
        day = input('Which day would you like to see data about?: all, monday, tuesday, ... sunday \n').lower()

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

    # extract month and day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()#1
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        month =months.index(month) + 1
        df = df[ df['month'] == month ]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[ df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df.month.value_counts().idxmax()
    print(popular_month)
    # TO DO: display the most common day of week
    popular_day_of_week = df.day_of_week.value_counts().idxmax()#2
    print(popular_day_of_week)
    # TO DO: display the most common start hour
    popular_start_hour = df.hour.value_counts().idxmax()
    print(popular_start_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_commonly_start_station=df['Start Station'].value_counts().idxmax()
    print(most_commonly_start_station)
    # TO DO: display most commonly used end station
    most_commonly_end_station=df['End Station'].value_counts().idxmax()
    print(most_commonly_end_station)
    # TO DO: display most frequent combination of start station and end station trip
    combination=df.groupby(['Start Station'])['End Station'].value_counts().mode
    print(combination)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print(total_travel)
    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print(mean_travel)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('User Type Stats:')
    print(df['User Type'].value_counts())
    if city != 'washington':
        # Display counts of gender
        print('Gender Stats:')
        print(df['Gender'].value_counts())
        # Display earliest, most recent, and most common year of birth
        print('Birth Year Stats:')
        most_common_year = df['Birth Year'].mode()[0]
        print('Most Common Year:',most_common_year)
        most_recent_year = df['Birth Year'].max()
        print('Most Recent Year:',most_recent_year)
        earliest_year = df['Birth Year'].min()
        print('Earliest Year:',earliest_year)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def display(df):

    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    while (view_data=="yes"):
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower()
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__=='__main__':
    main()