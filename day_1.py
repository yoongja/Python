
# \/\/\/\/\/\/\  DO NOT TOUCH AREA  \/\/\/\/\/\/\ #
def is_on_list(days,day):
    return(day in days)

def get_x(days,num):
    return(days[num])

def add_x(days,day):
    days.append(day)

def remove_x(days,day):
    days.remove(day)

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

print("Is Wed on 'days' list?", is_on_list(days, "Wed"))

print("The fourth item in 'days' is:", get_x(days, 3))

add_x(days, "Sat")
print(days)

remove_x(days, "Mon")
print(days)


# /\/\/\/\/\/\/\ END DO NOT TOUCH AREA /\/\/\/\/\/\/\ #

