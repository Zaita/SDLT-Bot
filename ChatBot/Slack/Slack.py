import sys
import requests
import os
import time
import re
from slack_bolt import App
from dotenv import load_dotenv
import logging

load_dotenv()

app = App (
  token=os.environ.get("SLACK_BOT_TOKEN"),
  signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

class Instance:
  def __init__(self, ticket, dal):
    logging.info("-- Starting Slack Integration")
    app.ticket = ticket
    app.dal = dal
  
  def go(self):
    app.start(31373)


@app.message("test")
def reply_to_test(message, say):
  print(message)
  user = message['user']
  print(app.client.users_info(user=user))
  say(f"Yes, tests are important! {app.ticket.type} - {user}")

@app.message("start")
def reply_to_start(message, say):
  # app.ticket.start(ticketId)
  say("X")

@app.event("message")
def handle_message(body, logger):
  logger.info(body)

# @app.middleware  # or app.use(log_request)
# def log_request(logger, body, next):
#     logger.debug(body)
#     return next()
