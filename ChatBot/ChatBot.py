import logging
import ChatBot.Slack.Slack as Slack

class Interface:
  def __init__(self):
    logging.info("-- Starting chatbot subsystem")
    
  def go(self, type, ticket, dal):
    logging.info(f"-- Spawning ChatBot instance with type {type}")
    if type == "slack":
      s = Slack.Instance(ticket, dal)
      s.go()
  