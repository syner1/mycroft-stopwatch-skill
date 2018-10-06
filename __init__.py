from mycroft import MycroftSkill, intent_file_handler
from mycroft.util.parse import extract_number
import time, humanfriendly


class StopwatchAndTimer(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('stopwatch_start.intent')
    def handle_stopwatch_start_intent(self, message):
        self.speak_dialog("stopwatch_start",expect_response=True)
        self.starttime = time.time() 
        
    @intent_file_handler('stopwatch_stop.intent')
    def handle_stopwatch_stop_intent(self, message):
        stoptime = time.time() - self.starttime
        response = {'time': humanfriendly.format_timespan(int(stoptime))}
        self.speak_dialog("stopwatch_stop", data=response)
        
def create_skill():
    return StopwatchAndTimer()

