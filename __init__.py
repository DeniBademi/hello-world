# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.

from adapt.intent import IntentBuilder
from os.path import dirname
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger
import requests
import urllib.request
import ssl
__author__ = 'eward'

LOGGER = getLogger(__name__)


class HelloWorldSkill(MycroftSkill):
    def __init__(self):
        super(HelloWorldSkill, self).__init__(name="HelloWorldSkill")

    def initialize(self):
        thank_you_intent = IntentBuilder("ThankYouIntent"). \
            require("ThankYouKeyword").build()
        self.register_intent(thank_you_intent, self.handle_thank_you_intent)

        how_are_you_intent = IntentBuilder("HowAreYouIntent"). \
            require("HowAreYouKeyword").build()
        self.register_intent(how_are_you_intent,
                             self.handle_how_are_you_intent)
        
        hello_world_intent = IntentBuilder("HelloWorldIntent"). \
            require("HowAreYouKeyword").build()
        self.register_intent(hello_world_intent,
                             self.handle_hello_world_intent)
        
        hello_world_intent2 = IntentBuilder("HelloWorldIntent2"). \
            require("HowAreYouKeyword2").build()
        self.register_intent(hello_world_intent2,
                             self.handle_hello_world2_intent)



        
  #  def handle_thank_you_intent(self, message):
  #      self.speak_dialog("welcome")

 #   def handle_how_are_you_intent(self, message):
     #   self.speak_dialog("how.are.you")

 #   def handle_hello_world_intent(self, message):
    #    self.speak_dialog("hello.world")

      #  hello_world_intent = IntentBuilder("HelloWorldIntent"). \
      #      require("HelloWorldKeyword").build()
      #  self.register_intent(hello_world_intent,
      #                       self.handle_hello_world_intent)

    def handle_thank_you_intent(self, message):
        url="https://10.106.0.225/lamp1/0"
        r = urllib.request.urlopen("https://10.106.0.225/lamp1/0", context=ssl.SSLContext()).read()
        self.speak("As you wish") 

    def handle_how_are_you_intent(self, message):
        url="https://10.106.7.2/lamp2/0"
        r = urllib.request.urlopen("https://10.106.7.2/lamp2/0", context=ssl.SSLContext()).read()
        self.speak("As you wish")
        

    def handle_hello_world_intent(self, message):
        url="https://10.106.0.225/lamp1/1"
        r = urllib.request.urlopen("https://10.106.0.225/lamp1/0", context=ssl.SSLContext()).read()
        self.speak("As you wish") 
        
    def handle_hello_world2_intent(self, message):
        url="https://10.106.7.2/lamp2/1"
        r = urllib.request.urlopen("https://10.106.7.2/lamp2/0", context=ssl.SSLContext()).read()
        self.speak("As you wish")

    def stop(self):
        pass


def create_skill():
    return HelloWorldSkill()
