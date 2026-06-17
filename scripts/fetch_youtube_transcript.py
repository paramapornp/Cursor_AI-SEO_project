import requests

# 1. Paste Matt Kenyon's YouTube URL inside the quotes below
API_KEY = "sd_0e5774a5377e566edddbfcca130da7b9"
VIDEO_URL = "https://www.youtube.com/watch?v=3q3WBkSoANA"

def fetch_transcript():
    print("🚀 Connecting to Supadata API...")
    url = f"https://api.supadata.ai/v1/youtube/transcript?url={VIDEO_URL}&text=true"
    headers = {"x-api-key": API_KEY}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        with open("raw_transcript.txt", "w", encoding="utf-8") as f:
            f.write(data.get("content", "No transcript found"))
        print("✅ Success! Raw transcript saved to 'raw_transcript.txt'")
    else:
        print(f"❌ Error Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    fetch_transcript()