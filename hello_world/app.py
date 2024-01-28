import json
import os
from slack_sdk import WebClient

# Retrieve the bot token from the environment variables
BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN")
# Create a Slack client using the bot token
client = WebClient(token=BOT_TOKEN)

def lambda_handler(event, context):
    # Parse the incoming event data from Slack
    slack_event = json.loads(event["body"])

    # Check for URL verification during the event subscription process
    if slack_event.get("type") == "url_verification":
        # Respond with the challenge token to verify the endpoint
        return {"statusCode": 200, "body": slack_event.get("challenge")}
    elif slack_event.get("event"):
        # Extract the event data
        data = slack_event.get("event")
        event_type = data.get("type")

        # Check if the event is an app mention
        if event_type == "app_mention":
            # Get the channel ID from the event data
            channel_id = data.get("channel")
            # Post a greeting message in the channel where the app was mentioned
            client.chat_postMessage(channel=channel_id, text="👋 Hello there! I'm Serverless Slack App, here to make your day a little easier. 😊")
            return
    else:
        # Default response for other types of events or unhandled scenarios
        return {
            "statusCode": 200,
            "body": json.dumps(
                {
                    "message": "hello world",
                }
            ),
        }
