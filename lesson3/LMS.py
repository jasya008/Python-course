# import datetime as dt
# days = int(input())
# day_brth = dt.datetime.today()

# a = day_brth + dt.timedelta(days=days)

# print(a.day, a.month)


# def days_left(data):
#     d, m, y = [int(e) for e in data.split(".")]
#     my_d = dt.datetime(y, m, d) - dt.datetime.today()
#     print(my_d.days())


# price = int(input())
# discount = int(input())
# del_day = int(input())


# reg_day = input()
# d, m, y = [int(e) for e in reg_day.pslit(".")]
# reg_day = dt.date(y, m, d)

# reg_time = input()
# min, sec = [int(e) for e in reg_time.split(":")]
# reg_time = dt.datetime(0, min, sec)


# if dt.time(0, 12, 30) > reg_time > dt.time(0, 6, 0):
#     total = price - price * (discount / 100)
#     if reg_day.weekday() == 0:
#         date = reg_day + dt.timedelta(days=del_day)
#     else:
#         date = reg_day + dt.timedelta(days=del_day - 1)
# else:
#     total = price
#     date = reg_day + dt.timedelta(days=del_day)

# print(date.strftime("%D-%m-%Y"), int(total))


# def alarm(data, delta=10):
#     d, m, y = [int(e) for e in data.split("-")]
#     start_date = dt.date(2021, 1, 4)  
#     current_date = dt.date(y, m, d)
#     days_diff = (current_date - start_date).days
#     week_number = (days_diff // 7) + 1

#     if week_number % 2 != 0: 
#         if current_date.weekday() in [0, 1, 2, 4]: 
#             alarm_time = dt.time(8, 30)
#         elif current_date.weekday() == 3:  
#             alarm_time = dt.time(7, 45)
#         else:  
#             alarm_time = dt.time(10, 0)
#     else: 
#         if current_date.weekday() in [0, 1, 4]:  
#             alarm_time = dt.time(9, 0)
#         elif current_date.weekday() in [2, 3]:  
#             alarm_time = dt.time(9, 30)
#         else:  
#             alarm_time = dt.time(11, 0)

#     alarm_datetime = dt.datetime.combine(current_date, alarm_time)
#     alarm_times = [alarm_datetime.strftime("%d-%m-%Y %H:%M")]

#     if current_date.weekday() < 5: 
#         repeat_alarm = alarm_datetime + dt.timedelta(minutes=delta)
#         alarm_times.append(repeat_alarm.strftime("%d-%m-%Y %H:%M"))

#     return tuple(alarm_times)



# import datetime as dt

# def alarm(input_date, delta = 10):
#     time1 = None
#     time2 = None

#     day1 = dt.date(2021, 1, 4)
#     print(*[int(a) for a in input_date.split("-")])
#     day2 = dt.date([int(a) for a in input_date.split("-")])
#     days = day2 - day1
#     print(days,day%7)
#     return time1, time2
