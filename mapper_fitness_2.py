#!/usr/bin/python

import sys

for line in sys.stdin:
    line = line.strip()
    fields = line.split("\t")  # Split into list

    if len(fields) < 5:
        continue  # Skip lines with insufficient data

    Id, SleepDay, TotalSleepRecords, TotalMinutesAsleep, TotalTimeInBed = fields[:5]
    
    results = [Id, TotalMinutesAsleep]
    print("\t".join(results))

