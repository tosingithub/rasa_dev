# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
#
#
class ActionHelloWorld(Action):
#
    def name(self): # -> Text:
        return "action_hello_world"

    def run(self, dispatcher, tracker, domain): #: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        #scoreval = tracker.get_slot("scoreval")
        dispatcher.utter_message(text="Här är vårt råd: Ni bör få mer expertvägledning")

        return []
