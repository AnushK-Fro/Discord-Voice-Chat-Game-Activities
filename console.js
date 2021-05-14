fetch("https://discord.com/api/v8/channels/Channel ID Here/invites", {
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
