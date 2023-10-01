import logging

class DataAccessLayer:
  def __init__(self, type):
    logging.info(f"-- Starting data access layer with type {type}")