import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
            'new york city': 'new_york_city.csv',
          'washington': 'washington.csv' }

def get_filters():
   print('Hello! Let\'s explore some US bikeshare data!')
    
   city = input("Please select which city you would like to study: ").lower()

   while city not in ['chicago', 'new york city', 'washington']:
        city = input("Sorry that city name is not recognised, please try again. \nThe selections available are Chicago, New York City or Washington: ").lower()
        print ("You have selected", city)

   
   month = input("Please select a month between January and June or use 'all' to gather date from all months available: ").lower()

   while month not in ['all', 'january', 'february','march','april','may','june']:
        month = input("Sorry that month is not recognised, please try again:").lower()
    
   print ("You have selected", month)
    
   day = input("Please select a day or use 'all' to gather date from all days available: ").lower()

   while day not in ['all', 'monday', 'tuesday','wednesday','thursday','friday','saturday','sunday']:
        days = input("Sorry that day name is not recognised, please try again: ")
    
   print ("You have selected", day)

   print('-'*60)
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
    # convert the Start Time column to datetime
   df["Start Time"] = pd.to_datetime(df["Start Time"])
    # extract month and day of week from Start Time to create new columns
   df['month'] = df['Start Time'].dt.month
   df['day_of_week'] = df['Start Time'].dt.strftime("%A")
# filter by month if applicable
   if month != 'all':
      months = ['january','february','march','april','june']
      month = months.index(month) + 1

      df = df[df['month'] == month]
 # filter by day of week if applicable
   if day != 'all':
      df = df[df['day_of_week'] == day.title()]

   return df

def time_stats(df):
  ##"""Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    #TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print ("Most common month:" ,common_month)

    #TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print ("Most common month:",common_day)


    #TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print("Most common hour:",most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*60)


def station_stats(df):
 ##   """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print ("Most common start station:",most_common_start_station)
    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print ("Most common end station:",most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df ['combination'] = df ['Start Station'] +" and "+ df['End Station']
    most_commmon_start_station = df ['combination'].mode()[0]
    print("Most frequent start and end stations:",most_commmon_start_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*60)


def trip_duration_stats(df):
 ##   """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    # TO DO: display total travel time
    total_travel_time = sum(df ['Trip Duration'])
    print ("Combined total travel time:",total_travel_time)

    # TO DO: display mean travel time
    average_travel_time = df['Trip Duration'].mean()
    print ("Average trip duration:",average_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*60)


def user_stats(df):
  ##  """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print ("User Types are:\n",user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df:
      print("User gender statistics:\n",df['Gender'].value_counts())
    else:
      print ("User gender statistics: Sorry! no data available")
    
   

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
      earliest_year = int(df['Birth Year'].min())
      most_recent_year =int(df['Birth Year'].max())
      most_common_year = int(df['Birth Year'].mode())
      print("The earliest birth year: {} \nThe most recent year: {} \n The most common year: {}".format(earliest_year,most_recent_year,most_common_year))
    else:
      print ("User birth year statistics: Sorry! no data available")
      
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*60)

def raw_data(df):
    raw = input ("Would you like to see some of the raw data for the selected criteria? Please answer yes or no: ")
    start_position = 0
    while raw not in ['yes']:
      raw = input("Sorry that answer is not recognised, please try again: ").lower()
    while (raw) == 'yes':
      print(df.iloc[start_position:start_position+5])
      start_position += 5
      raw = input("Do you wish to continue with the next 5 rows? please answer yes or no: ").lower()
    

def main():
   while True:
      city, month, day = get_filters()
      df = load_data(city, month, day)

      time_stats(df)
      station_stats(df)
      trip_duration_stats(df)
      user_stats(df)
      raw_data(df)

      restart = input('\nDo you want to restart? Enter yes or no.\n')
      if restart.lower() != 'yes':
         break


if __name__ == "__main__":
	main()