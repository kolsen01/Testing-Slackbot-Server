from flask import Flask, request, make_response, Response
import os
import json

from slackclient import SlackClient

# Your app's Slack bot user token
SLACK_BOT_TOKEN = "xoxb-266477967974-sQp2XpVg8T3jf2fssDIhsD82"

# Flask webserver for incoming traffic from Slack
app = Flask(__name__)

# Post a message to a channel, asking users if they want to play a game

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