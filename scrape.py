import requests
from bs4 import BeautifulSoup
import json
import os

def fetch_and_save():
    # Replace with the actual T2BLive or Sacnilk URL
    url = "https://www.sacnilk.com/quick_boxoffice_updates"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # This logic depends on the site's table structure
        table = soup.find('table')
        rows = table.find_all('tr')[1:11] # Get top 10
        
        data = []
        for row in rows:
            cols = row.find_all('td')
            if len(cols) >= 3:
                data.append({
                    "title": cols[0].text.strip(),
                    "collection": cols[1].text.strip(),
                    "verdict": cols[2].text.strip()
                })
        
        # Save to JSON
        with open('live_data.json', 'w') as f:
            json.dump(data, f, indent=4)
            
    except Exception as e:
        print(f"Update failed: {e}")

if __name__ == "__main__":
    fetch_and_save()