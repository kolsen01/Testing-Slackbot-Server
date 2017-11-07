from flask import Flask, request, make_response, Response
import os
import json

from slackclient import SlackClient

# Your app's Slack bot user token
SLACK_BOT_TOKEN = "xoxb-266477967974-sQp2XpVg8T3jf2fssDIhsD82"
# SLACK_VERIFICATION_TOKEN = "SLACK_VERIFICATION_TOKEN"

# Slack client for Web API requests
#slack_client = SlackClient(SLACK_BOT_TOKEN)

# Flask webserver for incoming traffic from Slack
app = Flask(__name__)

# Post a message to a channel, asking users if they want to play a game

"""attachments_json = [
    {
        "fallback": "Upgrade your Slack client to use messages like these.",
        "color": "#3AA3E3",
        "attachment_type": "default",
        "callback_id": "menu_options_2319",
        "actions": [
            {
                "name": "games_list",
                "text": "Pick a game...",
                "type": "select",
                "data_source": "external"
            }
        ]
    }
]
"""
#
#@app.route("/slack/message_options", methods=["POST"])
#def message_options():
#    print(request.form, "message_options")
#    # Parse the request payload
#    form_json = json.loads(request.form["payload"])

#    menu_options = {
"""
        "options": [
            {
                "text": "Chess",
                "value": "chess"
            },
            {
                "text": "Global Thermonuclear War",
                "value": "war"
            }
        ]
    }

    return Response(json.dumps(menu_options), mimetype='application/json')
"""

@app.route("/slack/message_actions", methods=["POST"])
def message_actions():
    print(request.form, "message_actions")
    # Parse the request payload
    form_json = json.loads(request.form["payload"])
    print(form_json)

    # Check to see what the user's selection was and update the message
    selection = form_json["actions"][0]["value"]

    if selection == "yes":
        message_text = "The only winning move is not to play.\nHow about a nice game of chess?"
    else:
        message_text = ":horse:"

"""
    response = slack_client.api_call(
      "chat.update",
      channel=form_json["channel"]["id"],
      ts=form_json["message_ts"],
      text=message_text,
      attachments=[]
    )
"""
    return Response(json.dumps(message_text), mimetype='application/json')

#test
@app.route("/slack/healthy", methods=["GET"])
def healthy():
    
    return make_response("healthy", 200)

#test
@app.route("/slack/command", methods=["POST"])
def command():
    print(request.form, "command")
    message = {
            "text": "This is your first interactive message",
            "attachments": [
                {
                    "text": "Building buttons is easy right?",
                    "fallback": "Shame... buttons aren't supported in this land",
                    "callback_id": "button_tutorial",
                    "color": "#3AA3E3",
                    "attachment_type": "default",
                    "actions": [
                        {
                            "name": "yes",
                            "text": "yes",
                            "type": "button",
                            "value": "yes"
                        },
                        {
                            "name": "no",
                            "text": "no",
                            "type": "button",
                            "value": "no"
                        },
                        {
                            "name": "maybe",
                            "text": "maybe",
                            "type": "button",
                            "value": "maybe",
                            "style": "danger"
                        }
                    ]
                }
            ]
        }

   # return make_response(message, 200) 
    return Response(json.dumps(message), mimetype='application/json')   

if __name__ == "__main__":
    app.run()