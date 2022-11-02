#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>

#define MAX_LINE_LEN 200
#define MAX_EVENTS 1000 

typedef struct {
    char description[MAX_LINE_LEN];
    char timezone[MAX_LINE_LEN];
    char location[MAX_LINE_LEN];
    char day[MAX_LINE_LEN];
    char month[MAX_LINE_LEN];
    char year[MAX_LINE_LEN];
    char dweek[MAX_LINE_LEN];
    char start[MAX_LINE_LEN];
    char end[MAX_LINE_LEN];
    char date[MAX_LINE_LEN];
}Event;

typedef struct {
    char day[MAX_LINE_LEN];
    char month[MAX_LINE_LEN];
    char pmonth[MAX_LINE_LEN];
    char year[MAX_LINE_LEN];
    char dweek[MAX_LINE_LEN];
    char line[MAX_LINE_LEN];
    
}Day;

void generate_line(char line[MAX_LINE_LEN]){
    char buffer[MAX_LINE_LEN];
    int count = 0;
    int i = 0;

    while(line[count] != '\0'){
        buffer[count] = '-';
        count++;
    }
    buffer[count - 1] = '\0';
    strcpy(line, buffer);
}

void generate_readable_day(Day* da, char readable[MAX_LINE_LEN]){

    switch(atoi(da->month)){
        
        case 1 :
            strcpy(da->pmonth, "January");
            break; 
        case 2 :
            strcpy(da->pmonth, "February");
            break; 
        case 3 :
            strcpy(da->pmonth, "March");
            break; 
        case 4 :
            strcpy(da->pmonth, "April");
            break; 
        case 5 :
            strcpy(da->pmonth, "May");
            break; 
        case 6 :
            strcpy(da->pmonth, "June");
            break; 
        case 7 :
            strcpy(da->pmonth, "July");
            break; 
        case 8 :
            strcpy(da->pmonth, "August");
            break; 
        case 9 :
            strcpy(da->pmonth, "September");
            break; 
        case 10 :
            strcpy(da->pmonth, "October");
            break; 
        case 11 :
            strcpy(da->pmonth, "November");
            break; 
        case 12 :
            strcpy(da->pmonth, "December");
            break; 
        default :
            strcpy(da->pmonth, "");
    }
    
    snprintf(readable, (MAX_LINE_LEN*10), "%s %s, %s (%s)\n", 
            da->pmonth, da->day, da->year, da->dweek); 
}

void generate_readable_event(Event* eve, char readable[MAX_LINE_LEN]){

     char start_hh[MAX_LINE_LEN]; //buffers used for start time hh, and mm
     char start_mm[MAX_LINE_LEN];
     char end_hh[MAX_LINE_LEN];
     char end_mm[MAX_LINE_LEN];
     char trash[MAX_LINE_LEN];
     char out_put[MAX_LINE_LEN];
     
     sscanf(eve->start, "%2s%1s%2s", start_hh, trash, start_mm);
     sscanf(eve->end, "%2s%1s%2s", end_hh, trash, end_mm);

     //convert start and end time to 12 hour clock

    int s_hh = atoi(start_hh);
    int s_mm = atoi(start_mm);
    int e_hh = atoi(end_hh);
    int e_mm = atoi(end_mm);
    char s_pm_am[5];
    char e_pm_am[5];

    if (s_hh >= 12){
        if (s_hh == 12){
            strcpy(s_pm_am, "PM");
        }else{
            s_hh = s_hh - 12;
            strcpy(s_pm_am, "PM");
        }
    }else{
        if(s_hh == 0){
            s_hh = 12;
            strcpy(s_pm_am, "AM");
        }else{
            strcpy(s_pm_am, "AM");
        }
    }

    if (e_hh >= 12){
        if (e_hh == 12){
            strcpy(e_pm_am, "PM");
        }else{
            e_hh = e_hh - 12;
            strcpy(e_pm_am, "PM");
        }
    }else{
        if(e_hh == 0){
            e_hh = 12;
            strcpy(e_pm_am, "AM");
        }else{
            strcpy(e_pm_am, "AM");
        }
    }

     snprintf(readable, (MAX_LINE_LEN*10), "%02d:%02d %s to %02d:%02d %s: %s {{%s}} | %s\n" 
             ,s_hh, s_mm, s_pm_am,  e_hh, e_mm, e_pm_am, eve->description, eve->location, eve->timezone);
     
}

void parse_xml_line(Day* da, Event* ev, char s[MAX_LINE_LEN]){
    if(strncmp(s, "        <description>", 18) == 0){ //if the first n characters are the same then...
        // parse out the desired information from that line.
        char buffer[MAX_LINE_LEN];
        sscanf(s, "        <description>%[^</]", buffer);
        strcpy(ev->description, buffer);
    }
    else if(strncmp(s, "        <timezone>", 18) == 0){ //if the first n characters are the same then...
        // parse out the desired information from that line.
        char buffer[MAX_LINE_LEN];
        sscanf(s, "        <timezone>%[^</]", buffer);
        strcpy(ev->timezone, buffer);
    }
    else if(strncmp(s, "        <location>", 18) == 0){ //if the first n characters are the same then...
        // parse out the desired information from that line.
        char buffer[MAX_LINE_LEN];
        sscanf(s, "        <location>%[^</]", buffer);
        strcpy(ev->location, buffer);
    }
    else if(strncmp(s, "        <day>", 13) == 0){ //if the first n characters are the same then...
        // parse out the desired information from that line.
        char buffer[MAX_LINE_LEN];
        sscanf(s, "        <day>%[^</]", buffer); 
        strcpy(ev->day, buffer); // parse out both to the Event struct and Day struct 
        strcpy(da->day, buffer);
    }
    else if(strncmp(s, "        <month>", 15) == 0){ //if the first n characters are the same then...
        // parse out the desired information from that line.
        char buffer[MAX_LINE_LEN];
        sscanf(s, "        <month>%[^</]", buffer); 
        strcpy(ev->month, buffer); // parse out both to the Event struct and Day struct
        strcpy(da->month, buffer);
         
    }
    else if(strncmp(s, "        <year>", 14) == 0){ //if the first 7 characters are the same then...
        // parse out the desired information from that line.
        char buffer[MAX_LINE_LEN];
        sscanf(s, "        <year>%[^</]", buffer); 
        strcpy(ev->year, buffer); //  parse out both to the Event struct and Day struct
        strcpy(da->year, buffer);          
    }
    else if(strncmp(s, "        <dweek>", 15) == 0){ //if the first 7 characters are the same then...
        // parse out the desired information from that line.
        char buffer[MAX_LINE_LEN];
        sscanf(s, "        <dweek>%[^</]", buffer); 
        strcpy(ev->dweek, buffer); //  parse out both to the Event struct and Day struct
        strcpy(da->dweek, buffer);          
    }
    else if(strncmp(s, "        <start>", 15) == 0){ //if the first 7 characters are the same then...
        // parse out the desired information from that line.
        char buffer[MAX_LINE_LEN];
        sscanf(s, "        <start>%[^</]", buffer); 
        strcpy(ev->start, buffer); //  printf("(in function)buffer = %s\n", buffer);
         
        //printf("(in function)start  = %s\n", ev->start);
    }
    else if(strncmp(s, "        <end>", 13) == 0){ //if the first 7 characters are the same then...
        // parse out the desired information from that line.
        char buffer[MAX_LINE_LEN];
        sscanf(s, "        <end>%[^</]", buffer); 
        strcpy(ev->end, buffer); //  printf("(in function)buffer = %s\n", buffer);
         
    }
}


int main(int argc, char *argv[]) {
    char line[MAX_LINE_LEN];
    int from_y = 0, from_m = 0, from_d = 0;
    int to_y = 0, to_m = 0, to_d = 0;
    char *filename = NULL;
    int i;
    

    for (i = 0; i < argc; i++) {
        if (strncmp(argv[i], "--start=", 8) == 0) {
            sscanf(argv[i], "--start=%d/%d/%d", &from_y, &from_m, &from_d);
        } else if (strncmp(argv[i], "--end=", 6) == 0) {
            sscanf(argv[i], "--end=%d/%d/%d", &to_y, &to_m, &to_d);
        } else if (strncmp(argv[i], "--file=", 7) == 0) {
            filename = argv[i]+7;
        }
    }

    if (from_y == 0 || to_y == 0 || filename == NULL) {
        fprintf(stderr,
            "usage: %s --start=yyyy/mm/dd --end=yyyy/mm/dd --file=icsfile\n",
            argv[0]);
        exit(1);
    }

    /* Starting calling your own code from this point. */

    FILE* input_file = fopen(filename, "r");
    Event event[MAX_EVENTS];
    Day day[MAX_EVENTS];
    Event temp;
    Day temp1;
    Day temp2;
    char re[MAX_LINE_LEN];
    char re1[MAX_LINE_LEN];
    int k = 0;
    int event_count = 0;


    if(input_file == NULL){
        printf("Unable to open input file\n");
        return 1;
    }

    while (fgets(line, MAX_LINE_LEN, input_file) != NULL){
        if (strncmp(line, "    </event>", 12) == 0){
            Event* this_event = &event[k];
            char this_formatted[MAX_LINE_LEN];

            k++;
        }
        parse_xml_line(&day[k], &event[k], line);
    }


    /*
    This sorts by month and day vvvvvvvvvv 
     
      */

    for(int i = 0; i < k; ++i){
        for(int j = i+1; j<k; ++j){
            if(atoi(day[i].day) > atoi(day[j].day)){
                temp1 = day[i];
                day[i] = day[j];  
                day[j] = temp1;
            }if (atoi(day[i].month) > atoi(day[j].month)){
                temp1 = day[i];
                day[i] = day[j];  
                day[j] = temp1;
            }
        }
    }

    int alldays = k;

    /*
    This sorts by event (starting time)  vvvvvvvvvv 
     
      */

    for(int i = 0; i < k; ++i){
        for(int j = i+1; j<k; ++j){
            if (atoi(event[i].start) > atoi(event[j].start)){
                temp = event[i];
                event[i] = event[j];  
                event[j] = temp;
            }
        }
    }

    /*
    This removes duplicate days (only want unique days) vvvvvvvvvv 
     
      */

    for(int x = 0; x < alldays; x++){
        for(int y = x+1; y < alldays; y++){
            if(strncmp(day[x].day, day[y].day, 2) == 0){ 
                for(int z = y; z < alldays; z++){
                    day[z] = day[z+1];
                }
                y--;
                alldays--; 
            }
        }
    }
    
    int numspaces = alldays - 1;
    int counter = 0;
    int newdays = 0;

    /*
    This compares the day and event structs to know which event(s)
    belong on what day vvvvvvvvvv 
      */

    for(int i = 0; i < alldays; i++){
                /*
                   -case 1: if month = start month 
                   -then look at the range 
                   -from from_d <= day[i].day <= 31
                   -if there are any dates that fall under that range then
                   print them out.
                */
                if(atoi(day[i].month) == from_m){
                    if(atoi(day[i].day) >= from_d && atoi(day[i].day) <= 31){
                    generate_readable_day(&day[i], re1);
                    printf("%s", re1);
                    generate_line(re1);
                    printf("%s\n", re1);
                    /*
                    This compares the day and event structs attributes to know which event(s)
                    belong on what day vvvvvvvvvv 
                      */
                    for(int j = 0; j < k; j++){
                        if(strncmp(day[i].day, event[j].day, 2) == 0 &&
                            strncmp(day[i].month, event[j].month, 2) == 0 && 
                            strncmp(day[i].year, event[j].year, 4) == 0){
                                generate_readable_event(&event[j], re);
                                printf("%s", re);
                        }
                    }
                    if(counter < numspaces){
                        printf("\n");
                        counter++;
                    }

                    }else{
                        continue;
                    }

                /*
                   -case 2: if month = end month 
                   -then look at the range 
                   -from 1 <= day[i].day <= to_d 
                   -if there are any dates that fall under that range then
                   print them out.
                */
                }else if(atoi(day[i].month) == to_m){
                    if(atoi(day[i].day) >= 1 && atoi(day[i].day) <= to_d){

                        generate_readable_day(&day[i], re1);
                        printf("%s", re1);
                        generate_line(re1);
                        printf("%s\n", re1);
                        for(int j = 0; j < k; j++){
                            if(strncmp(day[i].day, event[j].day, 2) == 0 &&
                                strncmp(day[i].month, event[j].month, 2) == 0 && 
                                strncmp(day[i].year, event[j].year, 4) == 0){
                                    generate_readable_event(&event[j], re);
                                    printf("%s", re);
                            }
                        }
                        if(counter < numspaces){
                            printf("\n");
                            counter++;
                        }
                    }else{
                        continue;
                    }

                /*
                   -else: if from_y <= day[i].year <= to_y and
                            if from_m <=day[i].month <= to_m
                   -if there are any dates that fall under that range then
                   print them out.
                */
            }else if((atoi(day[i].year) >= from_y && atoi(day[i].year) <= to_y) && 
                (atoi(day[i].month) >= from_m && atoi(day[i].month) <= to_m)){

                generate_readable_day(&day[i], re1);
                printf("%s", re1);
                generate_line(re1);
                printf("%s\n", re1);
                for(int j = 0; j < k; j++){
                    if(strncmp(day[i].day, event[j].day, 2) == 0 &&
                        strncmp(day[i].month, event[j].month, 2) == 0 && 
                        strncmp(day[i].year, event[j].year, 4) == 0){
                            generate_readable_event(&event[j], re);
                            printf("%s", re);
                    }
                }
                if(counter < numspaces){
                    printf("\n");
                    counter++;
                }

            }
    }
    fclose(input_file);
    exit(0);
}
