import logging
import Ticket.Ticket as Ticket
import ChatBot.ChatBot as ChatBot
import DataAccessLayer.DataAccessLayer as DAL

logging.basicConfig(level=logging.DEBUG)

ticket = Ticket.Interface(type="jira")
dal = DAL.DataAccessLayer(type="rest-api")

chatBot = ChatBot.Interface()
chatBot.go(type="slack", ticket=ticket, dal=dal)  