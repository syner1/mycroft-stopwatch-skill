from mycroft import MycroftSkill, intent_file_handler
from mycroft.util.parse import extract_number
import time 
import humanfriendly


class Stopwatch(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.starttime = 0

    @intent_file_handler('stopwatch_start.intent')
    def handle_stopwatch_start_intent(self, message):
        self.speak_dialog("stopwatch_start")
        self.starttime = time.time() 
        
    @intent_file_handler('stopwatch_stop.intent')
    def handle_stopwatch_stop_intent(self, message):
        if self.starttime == 0:
            self.speak_dialog("stopwatch_nostart")
            pass
        else:
            stoptime = time.time() - self.starttime
            response = {'time': humanfriendly.format_timespan(int(stoptime))}
            self.speak_dialog("stopwatch_stop", data=response)
            self.starttime = 0
            pass
    
    @intent_file_handler('stopwatch_lap.intent')
    def handle_stopwatch_lap_intent(self, message):
        if self.starttime == 0:
            self.speak_dialog("stopwatch_nostart")
            pass
        else:
            laptime = time.time() - self.starttime
            response = {'time': humanfriendly.format_timespan(int(laptime))}
            self.speak_dialog("stopwatch_lap", data=response)
            pass

def create_skill():
    return Stopwatch()

