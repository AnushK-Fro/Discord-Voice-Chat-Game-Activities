import requests, json

def activities(activity): # Get Activity ID
    switch = {
        1: "755600276941176913",
        2: "755827207812677713",
        3: "773336526917861400",
        4: "814288819477020702"
    }
    return switch.get(activity, "1")

print("--------------------------------") # Heading
print("Fro's Activity Starter")
print("--------------------------------")
print("Please note that to start an activity, you need invite permissions. Your token and any sensitive details are not sent to a third party. You can check the script.")
print("--------------------------------")

channel_id = input("Enter the ID of the voice channel you would like to start the activity in: ") # Channel ID to generate the invite
token = input("Enter your Discord token (used to generate the invite): ") # Discord Token to generate the invite

print("1. Youtube Together") # Activities Heading
print("2. Poker Night")
print("3. Betrayal.io")
print("4. Fishington.io")

activity = int(input("Enter in the ID of the activity you would like to start: ")) # Get Activity

data = json.dumps({ # Data to Send
    "max_age": 86400,
    "max_uses": 0,
    "target_application_id": activities(activity),
    "target_type": 2,
    "temporary": False,
    "validate": None
})

headers = { # Headers
    "Authorization": token,
    "Content-Type": "application/json"
} 

response = requests.post("https://discord.com/api/v8/channels/" + channel_id + "/invites", data=data, headers=headers).json() # Send request to Discord servers

print("Generated Invite Link: https://discord.gg/" + response["code"]) # Print the invite link
print("Post this invite link in a text channel and click the link directly (regardless if it says Activity has Ended), it will launch the activity and make you join the voice channel.") # Explanation
