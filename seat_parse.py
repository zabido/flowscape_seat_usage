import os
import re
from datetime import datetime

flowscape_folder = "flowscape_data"
processed_folder = "processed_data"

processed_files = os.listdir(processed_folder)
processed_files = [f for f in processed_files if f.endswith(".csv")]

for filename in os.listdir(flowscape_folder):
    if not filename.endswith(".html"):
        continue

    input_file = os.path.join(flowscape_folder, filename)

    # Check if file has already been processed
    processed_file = None
    for f in processed_files:
        if f.startswith(filename[:-5]):
            processed_file = os.path.join(processed_folder, f)
            print(f"File {filename} has already been processed")
            break

    # If file has been processed, skip to next file
    if processed_file is not None:
        continue

    # Process file
    with open(input_file, "r", encoding="utf-8") as f:
        html_code = f.read()

    matches = re.findall(r"<p class=\"sc-pcJja hDGzhX\"><span>(\d+)<\/span><span>(.*?)<\/span>", html_code)

    # Convert matches to a list of strings
    matches = [(m[0], re.sub(r"<div.*?>|<\/div>", "", m[1])) for m in matches]

    seat_status = {f"Seat {int(id):04d}": status.strip() if status.strip() != "Occupied" else "Occupied" for id, status in matches}

    # Get creation time of input file
    timestamp = os.path.getctime(input_file)
    timestamp_dt = datetime.fromtimestamp(timestamp)
    timestamp_str = timestamp_dt.strftime("%Y%m%d%H%M%S")

    output_file = os.path.join(processed_folder, f"{filename[:-5]}_processed_{timestamp_str}.csv")

    with open(output_file, "w") as f:
        for seat, status in seat_status.items():
            f.write(f"{seat} is {status}\n")
        print(f"File {filename} has been processed and saved as {output_file}.")
