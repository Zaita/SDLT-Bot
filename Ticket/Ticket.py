import logging

class Interface:
  def __init__(self, type):
    logging.info("-- Starting ticket system integration")
    self.type = type