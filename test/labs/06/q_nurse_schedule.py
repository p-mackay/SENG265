#!/usr/bin/env python3

import datetime
from datetime import timedelta

def main():
    """
    Florence is a nurse in a clinic. She is caring for 4 patients on
    different medication schedules

    * Mark needs medication every 5 hours
    * Susan needs medication every 3 hours
    * Chloe needs medication every 8 hours
    * Alexander needs medication every 10 hours

    Starting with your current day and time, make a care schedule
    for the next 14 days that Florence can use to schedule
    who needs medication at what time.

    HINT: Create datetime objects for all times. Convert to ical
    and then sort. Now convert back to datetime objects to print out
    the final schedule.

    Follow the steps provided.

    STEP 1: Use function patient_schedule to get a list of
    medication times for every patient
    medication times in the list are in ical format

    mark_schedule = <...........COMPLETE..................>
    susan_schedule = <...........COMPLETE..................>
    chloe_schedule = <...........COMPLETE..................>
    alexander_schedule = <...........COMPLETE..................>


    STEP 2: Combine all the lists and then form a master list of
    when medication is required by which patient.

    Print the medication schedule sorted by time in the format below:

      Friday, 25 03 2021, 09:24:27 Time to give medication to Alexander
      Friday, 25 03 2021, 10:24:27 Time to give medication to Chloe

    Refer to florence_sched.txt to see what the final output
    should look like. You are not required to write this information
    to a file. Simply output to console is enough.

    HINT: You will need to keep track of who needs medication when.
    One way of doing this is with a dictionary. You may choose to
    use other ways.
    """

    # COMPLETE YOUR IMPLEMENTATION
    this_list = []
    dates = []
    merged = {}
    m_list = patient_schedule('Mark', 5)
    s_list = patient_schedule('Susan', 3)
    c_list = patient_schedule('Chloe', 8)
    a_list = patient_schedule('Alexander', 10)


    '''
    for time in m_list['times']:
        print(time.strftime('%A, %d %m %Y, %X'), m_list['name'])
    for time in s_list['times']:
        print(time.strftime('%A, %d %m %Y, %X'), s_list['name'])
    for time in c_list['times']:
        print(time.strftime('%A, %d %m %Y, %X'), c_list['name'])
    for time in a_list['times']:
        print(time.strftime('%A, %d %m %Y, %X'), a_list['name'])
    '''
    this_list.append(m_list)
    this_list.append(s_list)
    this_list.append(c_list)
    this_list.append(a_list)

    m_list = []

    for ele in this_list:
        for date in ele['times']:
            dates.append(date)

    dates.sort()
    for date in dates:
        

def patient_schedule(name, med_interval):
    """
    This function will take a patient name and corresponding
    medication interval and return a list of times when the patient needs
    medication, in ical format.  The function should use datetime_to_ical
    function.
    * Mark needs medication every 5 hours
    * Susan needs medication every 3 hours
    * Chloe needs medication every 8 hours
    * Alexander needs medication every 10 hours
    """
    patient = {'name' : name, 'times' : []} 
    end_date = datetime.datetime(2022, 3, 22)
    todays_date = datetime.datetime.today()
    tm = todays_date

    while tm < end_date:
        tm += timedelta(hours=med_interval)  
        patient['times'].append(tm)

    return patient



def generate_dates():
    date_list = []

    end_date = datetime.datetime(2022, 3, 22)
    todays_date = datetime.datetime.today()
    date = todays_date

    while date < end_date:
        date += timedelta(days=1)
        date_list.append(date) 

    return date_list


if __name__ == "__main__":
    main()
