from datetime import datetime, timedelta


def check_frequent_parking(frequent: str):
    if (len(frequent) != 5):
        return False
    sum = 0
    temp = 2
    for i in range(3, -1, -1):
        sum += int(frequent[i]) * temp
        temp += 1
    return 11 - (sum % 11) == int(frequent[4])


def set_zero_hour(day_time: datetime):
    return day_time.replace(minute=0, second=0)


def formula(max_stay_hours_morning: int, price_per_hour_day: float,
            price_per_hours_evening: float, price_per_hour_midnight: float,
            type: int, stay_hours: int, is_valid_frequent_parking: bool
            ):
    if type == 0:  # morning
        discount = 0.9 if is_valid_frequent_parking else 1
        if (stay_hours > max_stay_hours_morning):
            return ((price_per_hour_day * max_stay_hours_morning) + (
                    stay_hours - max_stay_hours_morning) * 2 * price_per_hour_day) * discount
    if type == 1:  # everning
        discount = 0.5 if is_valid_frequent_parking else 1
        return price_per_hours_evening * stay_hours * discount
    if type == 2:  # midnight
        discount = 0.5 if is_valid_frequent_parking else 1
        return price_per_hour_midnight * discount


def formula_by_day_of(max_stay_hours_morning: int, price_per_hour_day: float,
                      price_per_hours_evening: float, price_per_hour_midnight: float,
                      ):
    def formula_by_day(type: int, stay_hours: int, is_valid_frequent_parking: bool):
        return formula(max_stay_hours_morning, price_per_hour_day,
                       price_per_hours_evening, price_per_hour_midnight,
                       type, stay_hours, is_valid_frequent_parking)
    return formula_by_day

def convert_string_to_date(str: str):
    date_format = '%Y-%m-%d %H:%M'
    return datetime.strptime(str, date_format)


try:
    arrival_time_input = input('Input Arrival Time Format (yyyy-mm-dd hh:mm)')
    arrival_time = convert_string_to_date(arrival_time_input)
    arrival_time = set_zero_hour(arrival_time)
    leave_time_input = input('Input Leave Time Format (yyyy-mm-dd hh:mm)')
    leave_time = convert_string_to_date(leave_time_input)
    leave_time = set_zero_hour(leave_time)
    frequent_parking = input('Input Frequent Parking: ')
    is_valid_frequent_parking = check_frequent_parking(frequent_parking)
    temp_day = arrival_time
    is_parking_mid_night = False
    parking_morning_hours = 0
    parking_everning_hours = 0
    sum = 0
    while (arrival_time <= leave_time):
        if 8 <= arrival_time.hour < 17:
            parking_morning_hours += 1
        if 17 <= arrival_time.hour <= 23:
            parking_everning_hours += 1
        if 0 <= arrival_time.hour < 8 and temp_day.day == arrival_time.day :
            is_parking_mid_night = True
        if (temp_day.day != arrival_time.day or arrival_time == leave_time):
            match temp_day.weekday():
                case 0 | 1 | 2 | 3 | 4:  # Monday, Tuesday, Wednesday, Thurday, Friday
                    get_formula = formula_by_day_of(max_stay_hours_morning=2, price_per_hour_day=10,
                                                    price_per_hours_evening=5, price_per_hour_midnight=20)
                case 5:  # Saturday
                    get_formula = formula_by_day_of(max_stay_hours_morning=4, price_per_hour_day=3,
                                                    price_per_hours_evening=5, price_per_hour_midnight=20)
                case 6:  # Sunday
                    get_formula = formula_by_day_of(max_stay_hours_morning=8, price_per_hour_day=2,
                                                    price_per_hours_evening=5, price_per_hour_midnight=20)
                case default:
                    print('default')
                    pass
            if parking_morning_hours > 0:
                sum += get_formula(type=0, stay_hours=parking_morning_hours,
                                      is_valid_frequent_parking=is_valid_frequent_parking)
            if parking_everning_hours > 0:
                sum += get_formula(type=1, stay_hours=parking_everning_hours,
                                       is_valid_frequent_parking=is_valid_frequent_parking)

            if is_parking_mid_night:
                sum += get_formula(type=2, stay_hours=0,
                                        is_valid_frequent_parking=is_valid_frequent_parking)
            temp_day = arrival_time
            is_parking_mid_night = False
            parking_morning_hours = 0
            parking_everning_hours = 0
        arrival_time = arrival_time + timedelta(hours=1)
    print(f'total = {sum}')
except Exception as e:
    print(e)
