def add_time(start, duration,day=None):
    # 1. Declare Variables
    start_hours = int(start.split(":")[0])
    start_minutes = int(start.split(":")[1][:2])

    start_meridiem = start.split(":")[1][3:]

    duration_hours = int(duration.split(":")[0])
    duration_minutes = int(duration.split(":")[1])

    #2. Convert to 24 hrs Format
    if start_meridiem == "PM" and start_hours != 12:
        start_hours += 12
    elif start_meridiem == "AM" and start_hours == 12:
        start_hours = 0

    #3. Add Duration Hours and minutes
    total_hours = start_hours + duration_hours
    total_minutes = start_minutes + duration_minutes

    #4. Handle overflow of minutes
    if total_minutes >= 60:
        total_hours += 1
        total_minutes %= 60

    #5. Calculate days later and hours later
    days_later = total_hours // 24
    hours_later = total_hours % 24

    #6. Convert back to 12 hrs Format
    if hours_later == 0:
        hours_later = 12
        meridiem = "AM"
    elif hours_later < 12 :
        meridiem = "AM"
    elif hours_later == 12:
        meridiem = "PM"
    else:
        hours_later -= 12
        meridiem = "PM"

    #7. Handle the optional days of the week
    if day:
        days_in_the_week = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
        day_index = days_in_the_week.index(day.capitalize())
        end_day_index = (day_index + days_later) % 7
        end_day = days_in_the_week[end_day_index]
    else:
        end_day = None

    #8. Format the final time
    formatted_time = f"{hours_later}:{total_minutes:02d} {meridiem}"

    if end_day:
        formatted_time += f", {end_day}"

    #9. Handle next day or days later message
    if days_later == 1:
        formatted_time += f" (next day)"
    elif days_later > 1:
        formatted_time += f" ({days_later} days later)"

    #10. Return the fully formatted time
    return formatted_time

add_time('11:43 PM', '24:20', 'tueSday')