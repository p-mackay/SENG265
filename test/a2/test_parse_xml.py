#!/usr/bin/env python3
"""
Created on Mon Feb 28 10:16:43 2022
@author: rivera
#!/usr/bin/env python3
"""

import re
import sys
import datetime

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


def main():
    s = sys.argv[1][9:]
    e = sys.argv[2][7:]
    input_race = sys.argv[3][9:]
    input_circuits = sys.argv[4][11:]
    input_broadcasters = sys.argv[5][15:]
    race_list = race_to_dict(input_race) 
    cir_list = circuit_to_dict(input_circuits) 
    br_list = broadcaster_to_dict(input_broadcasters)
    events_list = []
    '''
    x = datetime.datetime(int(race.get('year')), int(race.get('month')), 
            int(race.get('day')), hour=int(race.get('start')[:2]), 
            minute=int(race.get('start')[3:5]))
    '''
    s = s.split('/')
    e = e.split('/')
    print(s)
   
    s_dt = datetime.datetime(int(s[0]), int(s[1]), int(s[2]))
    e_dt = datetime.datetime(int(e[0]), int(e[1]), int(e[2]))
    
    print(s_dt)

    for race in race_list:
        date_buff = datetime.datetime(int(race.get("year")), int(race.get("month")), int(race.get("day")))
        if s_dt <= date_buff <= e_dt:
            events_list.append(date_buff)
        continue

    events_list = list(set(events_list))
    events_list.sort()
    race_list = (sorted(race_list, key = lambda item: item['start']))

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
    '''
    while i < len(events_list):
        print(events_list[i].strftime('  - %d-%m-%Y'))
        for race in race_list:
            ts= datetime.datetime(int(race.get('year')), int(race.get('month')), int(race.get('day')))
            if ts == events_list[i]:
                print(f"    - id: {race.get('id')}")
                print(f"      description: {race.get('description')}")
                for cir in cir_list:
                    if race.get('location') == cir.get('id'):
                        print(f"      circuit: {cir.get('name')} ({cir.get('direction')})")
                        print(f"      location: {cir.get('location')}")
                x = datetime.datetime(int(race.get('year')), int(race.get('month')), int(race.get('day')), hour=int(race.get('start')[:2]), minute=int(race.get('start')[3:5]))
                y = datetime.datetime(int(race.get('year')), int(race.get('month')), int(race.get('day')), hour=int(race.get('end')[:2]), minute=int(race.get('end')[3:5]))
                print(f"      when: {x.strftime('%I:%M %p')} - {y.strftime('%I:%M %p')} {x.strftime('%A, %B %d, %Y')} ({cir.get('timezone')}) ")
                print("      broadcasters:")
                for br in br_list:
                    if br.get('id') in race.get('broadcaster').split(','):
                        print(f"        - {br.get('name')}")
        i += 1
    '''
    

    
    '''
    for dic in race_list:
        print(dic['year'])
        events_list.append(dic["year"], dic["month"], dic["day"])

    print(events_list)
    '''
    
    '''
    dicts = []
    dicts.append(a_list)
    dicts.append(c_list)
    dicts.append(b_list)
    

    for i in dicts:
        for f in i:
            merged.update(f)

    
    print(merged)
    '''
    f.close()

if __name__ == '__main__':
   main()


