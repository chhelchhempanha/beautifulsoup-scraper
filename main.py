import json
import requests
from bs4 import BeautifulSoup

# Fetch and parse the webpage
url = "https://www.womansday.com/relationships/dating-marriage/a41055149/best-pickup-lines/"
response = requests.get(url)
doc = BeautifulSoup(response.text, "html.parser")

# Extract titles from the specified container
title_container = doc.select_one("div.css-1adm8f3.emt9r7s6 > ul.css-l03nee.emt9r7s4")
title_tags = title_container.find_all("li", class_="css-32630i emt9r7s3")
titles = [title.text for title in title_tags]

# Extract and filter pickup lines
pickup_line_containers = doc.find_all("ul", class_="css-1r2vahp emevuu60")
pickup_lines = []

for container in pickup_line_containers:
    lines = container.find_all("li")
    if lines:
        filtered_lines = [
            line.text.split("RELATED:")[0] if "RELATED:" in line.text else line.text
            for line in lines
        ]
        pickup_lines.append(filtered_lines)

# Combine titles and pickup lines into a dictionary
data = {titles[i]: pickup_lines[i] for i in range(len(titles))}

# Save the data as a JSON file with a new file name
new_file_name = 'pickup_lines_data.json'
with open(new_file_name, 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)

print(f"Data has been saved successfully in file {new_file_name}")
