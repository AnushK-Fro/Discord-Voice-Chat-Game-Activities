# Discord Game Activities in Voice Chat Script
Start YouTube Together, Poker Night, Betrayal.io, or Fishington.io in a Discord voice channel without paying.

All you need to do is run the Python script, fill in the fields, and it will give you an invite link.
Post the invite link in a text channel and then click the link directly. It should launch the activity.

The options are:
1. Youtube Together
2. Poker Night
3. Betrayal.io
4. Fishington.io

These games built into Discord are the only ones that are known to exist.
You do not need to pay for any of them.
No data is sent to third parties, the data is only sent to Discord. You can verify this by checking the script yourself.

# Alternative
### As a Member
Alternatively, instead of running this Python script, you can just run this in your developer console:
fetch(https://discord.com/api/v8/channels/Channel ID Here/invites, {
                    method: "POST",
                    body: JSON.stringify({
                        max_age: 86400,
                        max_uses: 0,
                        target_application_id: "755827207812677713",  // Youtube Together: 755600276941176913 | Poker Night: 755827207812677713 | Betrayal.io: 773336526917861400 | Fishington.io: 814288819477020702 
                        target_type: 2,
                        temporary: false,
                        validate: null
                    }),
                    headers: {
                        "Authorization": "Discord Token Here",
                        "Content-Type": "application/json"
                    }
                })
                
Replace "Discord Token Here" with your actual Discord token. Replace "Channel ID Here" with the channel ID of the voice channel you want to start the activity in. You can also replace the target_application_id with a different application ID depending on what activity you want to do. If you look at the response of the request, it will contain the ID for the invite to start the activity.
### As an Administrator
You can download a bot such as https://github.com/advaith1/activities to automatically create invites for you without using your token.
