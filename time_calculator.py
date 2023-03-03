def add_time(start, duration, day_of_week=None):

  days = ["sunday","monday","tuesday","wednesday","thursday","friday","saturday"]
  
  start_time_12format = start.split()
  start_time = start_time_12format[0]
  am_or_pm = start_time_12format[1]
  start_time_sep = start_time.split(":")
  start_time_hour = int(start_time_sep[0])
  start_time_min = int(start_time_sep[1])

  duration_sep = duration.split(":")
  duration_hour = int(duration_sep[0])
  duration_min = int(duration_sep[1])
  
  if am_or_pm == "PM":
    if start_time_hour == 12:
      start_time_hour = start_time_hour
    else:
      start_time_hour += 12
  else:
    if start_time_hour == 12:
      start_time_hour = 24

  new_time_hour = start_time_hour + duration_hour
  new_time_min = start_time_min + duration_min

  if new_time_min >= 60:
    adding_hour = int(new_time_min/60)
    new_time_hour = new_time_hour + adding_hour
    new_time_min = new_time_min%60

  if new_time_hour > 24:
    days_later = int(new_time_hour/24)
    new_time_hour = new_time_hour%24
    if new_time_hour == 0:
      new_time_hour = 24
    else:
      pass
    if days_later == 1:
      day_count = "(next day)"
    elif days_later >1:
      day_count = "("+ str(days_later)+" days later)"
    else:
      day_count = ""
  else:
    days_later = 0
    day_count = ""

  if(day_of_week is not None):
    start_day = day_of_week.lower()
    day_index = days.index(start_day)
    new_day_index = int(day_index) + int(days_later)
    if new_day_index >= 7:
      new_day_index = new_day_index%7
      final_day = days[new_day_index].capitalize()
    else:
      new_day_index = new_day_index
      final_day = days[new_day_index].capitalize()
  else:
    final_day = ""
    
  start_time_min = "{:02d}".format(start_time_min)
  duration_min = "{:02d}".format(duration_min)
  new_time_min = "{:02d}".format(new_time_min)
  
  if new_time_hour <= 11:
    am_or_pm_final = "AM"
  elif new_time_hour >= 13 and new_time_hour <= 23:
    am_or_pm_final = "PM"
    new_time_hour = new_time_hour - 12
  elif new_time_hour == 12:
    am_or_pm_final = "PM"
  elif new_time_hour == 24:
    new_time_hour = 12
    am_or_pm_final = "AM"
  else:
    pass

  new_time_array = [str(new_time_hour),":",str(new_time_min)," ",str(am_or_pm_final)]

  if final_day != "":
    new_time_array.append(", ")
    new_time_array.append(final_day)
  if day_count != "":
    new_time_array.append(" ")
    new_time_array.append(day_count)

  new_time = "".join(new_time_array)
  return new_time
