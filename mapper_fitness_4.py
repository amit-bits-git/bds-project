#!/usr/bin/python

import sys

for line in sys.stdin:
    line = line.strip()
    fields = line.split("\t")  # Split into list

    if len(fields) < 5:
        continue  # Skip lines with insufficient data

    Id, SleepDay, TotalSleepRecords, TotalMinutesAsleep, TotalTimeInBed, ActivityDate, TotalSteps, TotalDistance, TrackerDistance, LoggedActivitiesDistance, VeryActiveDistance, ModeratelyActiveDistance, LightActiveDistance, SedentaryActiveDistance, VeryActiveMinutes, FairlyActiveMinutes, LightlyActiveMinutes, SedentaryMinutes, Calories = fields[:19]
        
    results = [Id, TotalDistance]
    print("\t".join(results))

