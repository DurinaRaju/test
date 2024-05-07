import requests

def track_blue_dart(tracking_id):
    url = "https://www.bluedart.com/tracking?txtTrack=" + tracking_id
    response = requests.get(url)
    
    if response.status_code == 200:
        status = response.json()['track']
        print(f"Tracking ID: {tracking_id} - Status: {status}")
    else:
        print(f"Failed to track {tracking_id}")

# List of Blue Dart Tracking IDs
tracking_ids = ["20599867385"]

for tracking_id in tracking_ids:
    track_blue_dart(tracking_id)