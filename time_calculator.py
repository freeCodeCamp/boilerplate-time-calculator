


def add_time(start_time, duration, start_day=None):
    # Parse start time
    start_time, am_pm = start_time.split()
    start_hour, start_minute = map(int, start_time.split(':'))
    
   
    duration_hour, duration_minute = map(int, duration.split(':'))
    
    
    if am_pm == "PM":
        start_hour += 12
    
    
    total_minutes = start_hour * 60 + start_minute + duration_hour * 60 + duration_minute
    
   
    days = total_minutes // (24 * 60)
    remaining_minutes = total_minutes % (24 * 60)
    
    
    result_hour = remaining_minutes // 60
    result_minute = remaining_minutes % 60
    result_am_pm = "AM" if result_hour < 12 else "PM"
    result_hour %= 12
    
    
    if result_hour == 0:
        result_hour = 12
    
   
    if start_day:
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        start_day_index = days_of_week.index(start_day.capitalize())
        result_day_index = (start_day_index + days) % 7
        result_day = days_of_week[result_day_index]

    
    result_str = f"{result_hour}:{result_minute:02d} {result_am_pm}"
    if start_day:
        result_str += f", {result_day}"
    if days == 1:
        result_str += " (next day)"
    elif days > 1:
        result_str += f" ({days} days later)"
    
    return result_str


print(add_time("3:00 PM", "3:10"))
print(add_time("11:30 AM", "2:32", "Monday"))
print(add_time("11:43 AM", "00:20"))
print(add_time("10:10 PM", "3:30"))
print(add_time("11:43 PM", "24:20", "tueSday"))
print(add_time("6:30 PM", "205:12"))

    

