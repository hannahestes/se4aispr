#!/usr/bin/env python3
"""
monitor_hw5.py
Live-monitoring for hw5.py: shows which CSVs are currently opened.
"""
import subprocess
import time

PID = 89146          # Replace with your actual hw5.py PID
SLEEP = 10           # Seconds between checks

while True:
    print("\nChecking open CSV files for PID", PID)
    try:
        # Run lsof to list files opened by the process
        result = subprocess.run(
            ["lsof", "-p", str(PID)],
            capture_output=True,
            text=True
        )
        lines = result.stdout.splitlines()
        # Filter for CSV files
        csv_files = [line for line in lines if ".csv" in line]
        print(f"CSV files currently open ({len(csv_files)}):")
        for f in csv_files:
            print(" ", " ".join(f.split()[8:]))  # print the filename only
    except Exception as e:
        print("Error:", e)

    time.sleep(SLEEP)
