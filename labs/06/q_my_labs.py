#!/usr/bin/env python3

import datetime
from datetime import timedelta

def main():
    """
    Create a datetime object for today's date
    """

    # COMPLETE IMPLEMENTATION
    todays_date = datetime.datetime(2022, 3, 4) 

    date_list = every_lab(todays_date)

    for date in date_list:
        print(date.strftime("%a, %d %b %y"))

    """ 
    variable date_list should contain datetime objects 
    for all the days when you have a lab
    print these dates in the format "Mon, 15 Jan 21"
    """

    # COMPLETE IMPLEMENTATION

    


def every_lab(todays_date):
    end_date = datetime.datetime(2022, 4, 8)
    labs = []
    this_lab = todays_date
    labs.append(this_lab)

    while this_lab < end_date:
       this_lab += timedelta(weeks=1) 
       labs.append(this_lab)
    
    return labs

    """
    Assume that you have a lab every week till the end of classes. 
    (Only your lab, in this instance.)

    This function will create datetimes objects for those labs, 
    add them to a list and then return this list
    """

    # COMPLETE IMPLEMENTATION


if __name__ == "__main__":
    main()
