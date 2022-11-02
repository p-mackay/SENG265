#!/usr/bin/env python3
'''
Paul MacKay - V00967869 - SENG265 - Assignment 2 - 14/03/22

Strategy explained:
    - Read in each of the files from stdin (races.xml, circuits.xml, broadcasters.xml)
    - Create a list of dicts representing all information contained in each of the 
    input files. So we have 3 lists each list contains multiple dicts.
    - Then match up tags to get the corrects information for each date, write
    that information to output.yaml
    
'''

import re
import sys
import datetime


'''
Code supplied with a2. Returns a list of dicts (dicts are of size 9 in order to 
contain each key ie broadcasters, id, description, location, etc)   
'''
def race_to_dict(file_name):
    # define the collections to be used
    this_list = []
    filtered_lines = []
    # read the file line by line
    with open(file_name) as file:
        for line in file:
            # use regular expressions to collect relevant data
            line = re.findall(r'<(.*?)>(.*?)</\1>', line)
    #         # only include tags with information
            if len(line) > 0:
                filtered_lines.append(line[0])
    this_dic = {}
    # create the dictionaries
    for i in range(len(filtered_lines)):
        tup = filtered_lines[i]
        this_dic[tup[0]] = tup[1]
        # separate the information for each broadcaster
        if (i+1)%9 == 0 and i>0:
            this_list.append(this_dic)
            this_dic = {}
    # print the list of dictionaries
    return this_list 

'''
Code supplied with a2. Returns a list of dicts (dicts are of size 5 in order to 
contain each key ie id, name, location, timezone, etc)   
'''
def circuit_to_dict(file_name):
    # define the collections to be used
    this_list = []
    filtered_lines = []
    # read the file line by line
    with open(file_name) as file:
        for line in file:
            # use regular expressions to collect relevant data
            line = re.findall(r'<(.*?)>(.*?)</\1>', line)
    #         # only include tags with information
            if len(line) > 0:
                filtered_lines.append(line[0])
    this_dic = {}
    # create the dictionaries
    for i in range(len(filtered_lines)):
        tup = filtered_lines[i]
        this_dic[tup[0]] = tup[1]
        # separate the information for each broadcaster
        if (i+1)%5 == 0 and i>0:
            this_list.append(this_dic)
            this_dic = {}
    # print the list of dictionaries
    return this_list 

'''
Code supplied with a2. Returns a list of dicts (dicts are of size 3 in order to 
contain each key ie id, name, cost)   
'''
def broadcaster_to_dict(file_name):
    # define the collections to be used
    this_list = []
    filtered_lines = []
    # read the file line by line
    with open(file_name) as file:
        for line in file:
            # use regular expressions to collect relevant data
            line = re.findall(r'<(.*?)>(.*?)</\1>', line)
    #         # only include tags with information
            if len(line) > 0:
                filtered_lines.append(line[0])
    this_dic = {}
    # create the dictionaries
    for i in range(len(filtered_lines)):
        tup = filtered_lines[i]
        this_dic[tup[0]] = tup[1]
        # separate the information for each broadcaster
        if (i+1)%3 == 0 and i>0:
            this_list.append(this_dic)
            this_dic = {}
    # print the list of dictionaries
    return this_list 

'''
Accepts:
    events_list - a list containing unique datetime objects
    race_list - a list containing all races (each race represented as a dict)
    cir_list - a list containing all circuits (each circuit represented as a dict)
    br_list - a list containing all broadcasters (each broadcaster represented as a dict)
Writes a file called output.yaml
'''
def make_file(events_list, race_list, cir_list, br_list):
    i = 0

    f = open("output.yaml", "w")
    f = open("output.yaml", "a")
    

    f.write("events:\n")
    while i < len(events_list):
        f.write(events_list[i].strftime('  - %d-%m-%Y:\n'))
        for race in race_list:
            ts= datetime.datetime(int(race.get('year')), int(race.get('month')), int(race.get('day')))
            if ts == events_list[i]:
                f.write(f"    - id: {race.get('id')}\n")
                f.write(f"      description: {race.get('description')}\n")
                for cir in cir_list:
                    if race.get('location') == cir.get('id'):
                        f.write(f"      circuit: {cir.get('name')} ({cir.get('direction')})\n")
                        f.write(f"      location: {cir.get('location')}\n")
                        tz = cir.get('timezone')
                x = datetime.datetime(int(race.get('year')), int(race.get('month')), int(race.get('day')), hour=int(race.get('start')[:2]), minute=int(race.get('start')[3:5]))
                y = datetime.datetime(int(race.get('year')), int(race.get('month')), int(race.get('day')), hour=int(race.get('end')[:2]), minute=int(race.get('end')[3:5]))
                f.write(f"      when: {x.strftime('%I:%M %p')} - {y.strftime('%I:%M %p')} {x.strftime('%A, %B %d, %Y')} ({tz})\n")
                f.write("      broadcasters:\n")
                for br in br_list:
                    if br.get('id') in race.get('broadcaster').split(','):
                        f.write(f"        - {br.get('name')}\n")
        i += 1

    f.close()

'''
accepts a date in the form yyyy/mm/dd
returns a datetime object of datetime(yyyy,mm,dd)
'''
def cmdline_date_to_datetime(dt):
    d = dt.split('/')
    date = datetime.datetime(int(d[0]), int(d[1]), int(d[2])) 

    return date

def main():
    s = sys.argv[1][8:]
    e = sys.argv[2][6:]
    input_race = sys.argv[3][9:]
    input_circuits = sys.argv[4][11:]
    input_broadcasters = sys.argv[5][15:]
    race_list = race_to_dict(input_race) 
    cir_list = circuit_to_dict(input_circuits) 
    br_list = broadcaster_to_dict(input_broadcasters)
    events_list = []

    s_dt = cmdline_date_to_datetime(s)
    e_dt = cmdline_date_to_datetime(e)
    
    for race in race_list:
        date_buff = datetime.datetime(int(race.get("year")), int(race.get("month")), int(race.get("day")))
        if s_dt <= date_buff <= e_dt:
            events_list.append(date_buff)
        continue

    events_list = list(set(events_list))
    events_list.sort()
    race_list = (sorted(race_list, key = lambda item: item['start']))

    make_file(events_list, race_list, cir_list, br_list)



if __name__ == '__main__':
   main()


