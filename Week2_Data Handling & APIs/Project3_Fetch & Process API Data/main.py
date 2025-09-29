import requests
import json

# API endpoint (Example: Public API for Cat Facts)
url = "https://catfact.ninja/facts?limit=5"

# Fetch data from API
response = requests.get(url)

# Check if request was successful
if response.status_code == 200:
    data = response.json()
    print("API Data Fetched Successfully!\n")

    # Print fetched data
    print(json.dumps(data, indent=4))

    # Process data (Extract only fact text)
    facts = []
    for fact in data['data']:
        facts.append({
            "fact": fact['fact']
        })

    # Save processed data to JSON
    with open("cat_facts.json", "w") as f:
        json.dump(facts, f, indent=4)

    print("\nProcessed cat facts saved to cat_facts.json")

else:
    print(f"Error: Unable to fetch data (Status Code: {response.status_code})")
