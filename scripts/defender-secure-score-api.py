# defender-secure-score-api.py
import requests, json
from azure.identity import DefaultAzureCredential

def main():
    credential = DefaultAzureCredential()
    token = credential.get_token("https://management.azure.com/.default").token

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    subscription_id = "<YOUR_SUBSCRIPTION_ID>"
    url = f"https://management.azure.com/subscriptions/{subscription_id}/providers/Microsoft.Security/secureScores?api-version=2023-01-01-preview"

    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    data = resp.json()

    with open("secure_score_data.json", "w") as f:
        json.dump(data, f, indent=2)
    print("Saved secure_score_data.json")

if __name__ == "__main__":
    main()
