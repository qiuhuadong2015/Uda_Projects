import time
import pandas as pd

CITY_DATA = {'chicago': 'chicago.csv',
             'new york': 'new_york_city.csv',
             'washington': 'washington.csv'}
MONTH_DATA = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october',
              'november', 'december', 'all']
DAY_DATA = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    从命令行获取用户的筛选条件：选择城市、选择月份、选择星期几

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    # 获取城市
    print('''
You can choose one city to analyze from the list:
1. chicago
2. new york
3. washington
Please enter the name of one city(for example, new york):''')
    city_invalid = True
    while city_invalid:
        city = input().lower().strip()
        city_invalid = city not in CITY_DATA.keys()
        if city_invalid:
            print("Your input is not a valid city: " + city)
            print("Please enter the name of one city again:")
        else:
            print("Your input is OK : " + city)

    # TO DO: get user input for month (all, january, february, ... , june)
    # 获取月份
    print('''
You can choose one month to analyze from the list:
1. january
2. february
...
12. december
13. all
Please enter the name of one city(for example, all):''')
    month_invalid = True
    while month_invalid:
        month = input().lower().strip()
        month_invalid = month not in MONTH_DATA
        if month_invalid:
            print("Your input is not a valid month: " + month)
            print("Please enter the name of one month again:")
        else:
            print("Your input is OK : " + month)

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    # 获取星期几
    print('''
You can choose one day to analyze from the list:
1. monday
2. tuesday
...
7. sunday
8. all
Please enter one day of week(for example, monday):''')
    day_invalid = True
    while day_invalid:
        day = input().lower().strip()
        day_invalid = day not in DAY_DATA
        if day_invalid:
            print("Your input is not a valid day: " + day)
            print("Please enter one day of week again:")
        else:
            print("Your input is OK : " + day)

    print('-' * 40)
    return city, month, day


def parse_time_section(structure_time):
    """
    提取时间的小时数，用于将时间分段
    :param structure_time: 时间对象
    :return: 小时数
    """
    return structure_time.tm_hour


def parse_time_info(time_str):
    """
    预先解析时间字符串为需要的信息
    :param time_str: 时间字符串
    :return: 字符串，包含月份、星期几、时间段，用 | 分割
    """
    structure_time = time.strptime(time_str, "%Y-%m-%d %H:%M:%S")
    month = structure_time.tm_mon  # range[1,12]
    month = MONTH_DATA[month - 1]
    day = structure_time.tm_wday   # range[0,6], 0 是星期一
    day = DAY_DATA[day]
    time_section = str(parse_time_section(structure_time))
    return month + "|" + day + "|" + time_section


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    从 csv 文件中加载数据为 pandas DataFrame，并基于条件（城市、月份、星期几）过滤，以及预处理数据（增加需要的列）

    [STEP 1]: 加载 csv 文件转为 DataFrame 对象并根据条件进行筛选
    [STEP 2]: 解析开始时间，新增月份列、星期列、时间段列
    [STEP 3]: 合并起始车站列和结束车站列，新增路线的列
    [STEP 4]: 根据请求进行筛选

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # [STEP 1]
    df = pd.read_csv(CITY_DATA[city])
    # [STEP 2]
    df['time_info'] = df['Start Time'].map(parse_time_info)
    df['month'] = df['time_info'].map(lambda s: s.split("|")[0])
    df['day'] = df['time_info'].map(lambda s: s.split("|")[1])
    df['time_section'] = df['time_info'].map(lambda s: int(s.split("|")[2]))
    # [STEP 3]
    df['trip'] = df['Start Station'] + " -> " + df['End Station']
    # [STEP 4]
    # print(df.head())
    if month != 'all':
        df = df.where(df['month'] == month)
    if day != 'all':
        df = df.where(df['day'] == day)
    df = df.dropna(axis=0, how="all")
    return df


def time_stats(df):
    """
    Displays statistics on the most frequent times of travel.
    统计并显示出行最频繁的时间段
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    s_month = df.groupby("month").size()
    print(s_month[s_month == max(s_month)])
    print()
    # TO DO: display the most common day of week
    s_day = df.groupby("day").size()
    print(s_day[s_day == max(s_day)])
    print()
    # TO DO: display the most common start hour
    s_time_section = df.groupby("time_section").size()
    print(s_time_section[s_time_section == max(s_time_section)])
    print()
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """
    Displays statistics on the most popular stations and trip.
    统计并显示人气最高的站点和路线
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    s_start_station = df.groupby("Start Station").size()
    print(s_start_station[s_start_station == max(s_start_station)])
    print()
    # TO DO: display most commonly used end station
    s_end_station = df.groupby("End Station").size()
    print(s_end_station[s_end_station == max(s_end_station)])
    print()
    # TO DO: display most frequent combination of start station and end station trip
    s_path = df.groupby("trip").size()
    print(s_path[s_path == max(s_path)])
    print()
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """
    Displays statistics on the total and average trip duration.
    统计并显示路线用时的总时长和平均时长
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("total travel time of every trip:")
    print(df.groupby("trip")['Trip Duration'].sum())
    print()
    # TO DO: display mean travel time
    print("mean travel time of every trip:")
    print(df.groupby("trip")['Trip Duration'].mean())
    print()
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df, has_all_colums):
    """
    Displays statistics on bikeshare users.
    统计并显示共享单车用户的统计数据
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df.groupby("User Type").size())
    print()
    # TO DO: Display counts of gender
    if has_all_colums:
        print(df.groupby("Gender").size())
        print()
    # TO DO: Display earliest, most recent, and most common year of birth
    if has_all_colums:
        print("earliest year of birth:")
        print(df['Birth Year'].min())
        print("most recent year of birth:")
        print(df['Birth Year'].max())
        print("most common year of birth")
        s_common_birth_year = df.groupby("Birth Year")["Birth Year"].count()
        print(s_common_birth_year[s_common_birth_year == max(s_common_birth_year)])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city not in ['washington'])

        restart = input('\nWould you like to restart? Enter yes or no.(or other to exit)\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
