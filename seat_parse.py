import re

input_file = "input.html"
output_file = "output.txt"

with open(input_file, "r", encoding="utf-8") as f:
    html_code = f.read()

matches = re.findall(r"<p class=\"sc-pcJja hDGzhX\"><span>(\d+)<\/span><span>(.*?)<\/span>", html_code)

# seat_status = {f"Seat {int(id):04d}": status.strip() for id, status in matches if status.strip()}

# with open(output_file, "w") as f:
    # for seat, status in seat_status.items():
        # f.write(f"{seat} is {status}\n")

# Convert matches to a list of strings
matches = [(m[0], re.sub(r"<div.*?>|<\/div>", "", m[1])) for m in matches]

seat_status = {f"Seat {int(id):04d}": status.strip() if status.strip() != "Occupied" else "Occupied" for id, status in matches}

with open(output_file, "w") as f:
    for seat, status in seat_status.items():
        f.write(f"{seat} is {status}\n")