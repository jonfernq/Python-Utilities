import datetime

# Read in course details from file
with open('course_details.txt', 'r') as f:
    start_date_str = f.readline().strip()
    end_date_str = f.readline().strip()
    midterm_date_str = f.readline().strip()
    class_days_str = f.readline().strip()
    holidays_str = f.readline().strip()
    start_time_str = f.readline().strip()
    end_time_str = f.readline().strip()

# Convert string dates and times to datetime objects
start_date = datetime.datetime.strptime(start_date_str, '%Y-%m-%d')
end_date = datetime.datetime.strptime(end_date_str, '%Y-%m-%d')
midterm_date = datetime.datetime.strptime(midterm_date_str, '%Y-%m-%d')
start_time = datetime.datetime.strptime(start_time_str, '%H:%M').time()
end_time = datetime.datetime.strptime(end_time_str, '%H:%M').time()

# Split string of class days into list of day abbreviations
class_days = class_days_str.split()

# Split string of holidays into list of datetime objects
holidays = []
if holidays_str:
    holidays_str_list = holidays_str.split(',')
    for holiday_str in holidays_str_list:
        holiday = datetime.datetime.strptime(holiday_str.strip(), '%Y-%m-%d')
        holidays.append(holiday)

# Initialize variables for tracking class meetings and weeks
class_meetings = 0
current_week = 1
current_month = start_date.month

# Loop through each day between start and end dates
current_date = start_date
while current_date <= end_date:

    # Check if current date is a holiday, and skip if it is
    if current_date in holidays:
        current_date += datetime.timedelta(days=1)
        continue

    # Check if current day is a class day
    if current_date.strftime('%a') in class_days:

        # Print new week/month heading if necessary
        if current_week != current_date.isocalendar()[1] or current_month != current_date.month:
            print('\nWeek {} - {}'.format(current_date.isocalendar()[1], current_date.strftime('%B %Y')))
            current_week = current_date.isocalendar()[1]
            current_month = current_date.month

        # Print class meeting time for current day
        print('{}, {}, {} - {}'.format(current_date.strftime('%a'), current_date.strftime('%B %d, %Y'), 
                                        start_time.strftime('%I:%M %p'), end_time.strftime('%I:%M %p')))
        class_meetings += 1

    # Increment current date by 1 day
    current_date += datetime.timedelta(days=1)

# Print total number of class meetings
print('\n{} Class Meetings Scheduled'.format(class_meetings))
