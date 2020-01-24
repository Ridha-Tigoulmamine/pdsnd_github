import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
def print_detail():
    print('Project title : Explore US Bikeshare Data')
    print('Project description : This project makes use of Python to exploring data related to bike share systems; provided by Motivate; for three major cities in the United States "Chicago", "New York City", and "Washington". The implemented code allows answering interesting questions about it by computing descriptive statistics. The script also takes raw input to create an interactive experience in the terminal to present these statistics.')
    print('Dataset used : chicago.csv, new_york_city.csv, washington.csv')

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
    while True:
      city = input("\nWhich city would you like to filter by? New York City, Chicago or Washington?\n")
      if city.lower() not in CITY_DATA.keys():
        print("Sorry, I didn't find this city. Try again.")
        continue
      else:
        break

    # get user input for month (all, january, february, ... , june)
    while True:
      month = input("\nWhich month would you like to filter by? January, February, March, April, May, June or all months?\n")
      if month.lower() not in ['all', 'january', 'february', 'march','april', 'may', 'june']:
        print("Sorry, I didn't find this month. Try again.")
        continue
      else:
        break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
      day = input("\nWhich day would you like to filter by?? Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or all dayse.\n")
      if day.lower() not in ['all', 'monday', 'tuesday', 'wednesday', 'thursday','friday', 'saturday', 'sunday']:
        print("Sorry, I didn't find this day. Try again.")
        continue
      else:
        break

    print('-'*40)
    return city.lower(), month.lower(), day.lower()


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
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode()[0]
    print('the most Common Month:', popular_month)

    # display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('the most Common day:', popular_day)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Common Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    Start_Station = df['Start Station'].value_counts().idxmax()
    print('Most Commonly used start station:', Start_Station)

    # display most commonly used end station
    End_Station = df['End Station'].value_counts().idxmax()
    print('\nthe most Commonly used end station:', End_Station)

    # display most frequent combination of start station and end station trip
    print('\nMost Frequency Start & Stop Combination')
    print(df.groupby(['Start Station', 'End Station']).size().nlargest(1))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    Total_Travel_Time = sum(df['Trip Duration'])
    print('Total travel time:', Total_Travel_Time/86400, " Days")

    # display mean travel time
    Mean_Travel_Time = df['Trip Duration'].mean()
    print('Mean travel time:', Mean_Travel_Time/60, " Minutes")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()

    # Display counts of gender
    print('\nCounts of Genders:')
    try:
        print(df['Gender'].value_counts())
    except:
        print('Data does not include genders')

    # Display earliest, most recent, and most common year of birth
    try:
      Earliest_Year = df['Birth Year'].min()
      print('\nEarliest Year:', Earliest_Year)
    except KeyError:
      print("\nEarliest Year:\nNo data available for this month.")

    try:
      Most_Recent_Year = df['Birth Year'].max()
      print('\nMost Recent Year:', Most_Recent_Year)
    except KeyError:
      print("\nMost Recent Year:\nNo data available for this month.")

    try:
      Most_Common_Year = df['Birth Year'].value_counts().idxmax()
      print('\nMost Common Year:', Most_Common_Year)
    except KeyError:
      print("\nMost Common Year:\nNo data available for this month.")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    show_more = 'yes'
    while show_more == 'yes':
        for i in df.iterrows():
            count = 0
            while count < 5:
                print(i)
                count += 1
            response = input('\nView 5 more data entries? Yes or No?\n')
            if response.lower() == 'no':
                show_more = 'no'
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
