# Discussion

## Objective  
This script is made to extract logs from a big log file for a specific date. Instead of going through the whole file normally, it uses memory mapping to make it faster.

## How it works  
1. The user gives a date when running the script.  
2. The script opens the log file and uses memory mapping to read it.  
3. It checks each line and if the line starts with the given date, it saves that line.  
4. All the matching logs are saved in a new file inside an "output" folder.

## Challenges  
- Figuring out how to read large files without slowing down was tricky.  
- Handling file errors like when the log file is missing.  
- Making sure the script only picks lines starting with the exact date.

## Conclusion  
The script works well for big log files and quickly pulls out logs for any given date. It also handles common errors and keeps the output organized.
