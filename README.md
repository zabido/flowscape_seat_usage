# Readme
## What is this script about?
Reads .html files from 'flowscape_data' folder and parses it to identify seat and meeting rooms and their availability (available or occupied). The html file is expected to be saved from the flowscape web application.
The html files are need to be provided, copied manually to the folder.
The script will process all files that haven't been processed/found in the output folder. Results after processing the files are stored in a csv file and placed in the 'processed_data' folder.
The script will identify seats by ID that are always considered to be 4 digit long and stores the availability information. In case a file is already processed it will be skipped.
