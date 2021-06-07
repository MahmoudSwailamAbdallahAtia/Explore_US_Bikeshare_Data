#importing time, pandas, and numpy
import time
import pandas as pd
import numpy as np
#dictinary of 3 csv files.
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
#get user input about his\her choices to specify a city, month, and day to analyze. 
#function to handle user choices.
def get_filters():
    city = input('which city you want ? ').lower()
    month = input('choose all for all our months or which month you want ? ').title()
    day = input('choose all for all our days or which day you want ? ').title()
    #lists of user choices we want to get from.
    cities = ['chicago','new york city','washington']
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'All']
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'All']
    #just read pyhton as words!.
    if city in cities and(month in months and day in days):
        #.format puts city, month and day the user inputed above in {} to make user see like city: the city and so on.
        print('Great You Choose>>> city: {}  month: {}  day:{}'.format(city, month, day))
    while city not in cities or(month not in months or day not in days):
        #print() will print to the output and because of \n the user will see the dialoge in 2 lines.                                       
        print('Please Choose From This Cities >>>\n    chicago, new york city, washington')
        print('And From This Months >>>\n    January, February, March, April, May, June, All')
        print('And From This days >>>\n    Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, All')
        #.lower() makes all inputs the user do uppercase or lowercase in lowercase.
        city = input('which city you want ? ').lower()
        month = input('which month you want ? ').title()
        day = input('which day you want ? ').title()
        if city in cities and(month in months and day in days):
            print('Great You Choose>>> city: {}  month: {}  day:{}'.format(city, month, day))
    print('-'*40)
    return city, month, day 
        
#if you remember def get_filters(city, month, day):above this order will excute the function.             
def load_data(city, month, day):
    """
        Loads data for the specified city and filters by month and day if applicable.
        df = pd.read_csv(CITY_DATA[city])
        Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
        Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #load data from csv file
    df = pd.read_csv(CITY_DATA[city])
    #convert column start time to date to extract any date we want
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #make column month from date 
    df['month'] = df['Start Time'].dt.month_name()
    # the same with day and hour
    df['day'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    if month != 'All':
        #input month now will appear only on column month
        df = df[df['month'] == month]
    if day != 'All':  
        # and the day too
        df = df[df['day'] == day]
    print('-'*40)
    return df        
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()        
    # TO DO: display the most common month
    #the mode from month, day and hour columns 
    print('the common_month : \n', df['month'].mode()[0])
    # TO DO: display the most common day
    print('the common day : \n', df['day'].mode()[0])
    # TO DO: display the most common start hour
    print('the common hour : \n', df['hour'].mode()[0])
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # TO DO: display most commonly used start station
    print('common_start_station\n', df['Start Station'].mode()[0])
    # TO DO: display most commonly used end station
    print('common_end_station\n', df['End Station'].mode()[0])
    # TO DO: display most frequent combination of start station and end station trip
    df['frequent'] = df['Start Station'] + ' AND ' + df['End Station']
    print('common_frequent_station\n', df['frequent'].mode()[0])
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # TO DO: display total travel time
    print('Total travel time in seconds\n', df['Trip Duration'].sum())
    print('Total travel time in hours\n', (df['Trip Duration'].sum())/3600)
    # TO DO: display mean travel time
    print('Average Time in seconds\n', df['Trip Duration'].mean())
    print('Average Time in hours\n', (df['Trip Duration'].mean())/3600)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    #desplay counts of user tupe
    print('User Types\n', df['User Type'].value_counts())
    #and gender
    if 'Gender' in df:
        print('gender counts:\n', df['Gender'].value_counts())
    #all description of birth year like max, min, 25%, 50%, 75%
    if 'Birth Year' in df:
        print("description of birth year\n", df['Birth Year'].describe())
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def explore(df):
    #determine rows the user want to read 
    read = input("How many rows you want to read?")
    read_0 = int(read)
    print (df[0:read_0])
    again = input("Do you want to explore more rows? Type>>>\n      yes or no : \n      ").lower()
    y = 0
    while True:
        if again != 'yes':
            break
        x = read_0 + y
        read = input("How many rows you want to read?\n      ")
        read_1 = int(read)
        y += read_1
        repeated = read_0 + y
        print(df[x:repeated])
        again = input("Do you want to explore more rows? Type>>> yes or no : ").lower()
    print("Thank You for exploring our DATA")
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        explore(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break  
if __name__ == "__main__":
	main()
