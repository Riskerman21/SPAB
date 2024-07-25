import re
#pip install spacy 
#python -m spacy download en_core_web_sm
import spacy
import en_core_web_sm
import pandas as pd
from long_perdict import predict_flood_risk
from dateutil import parser
from datetime import datetime

month_number_to_name = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
}

class process_text():

    def __init__(self):
        self.message = "Hello! I am the Thailand Flood Safety Chat Bot. I am here to provide assistance!\r\n" + \
            "Please note that I can only currently work in English, including location names.\r\n" + \
            "'You can ask me questions like where can I go?'\r\n" + \
            "'Will I be affected during a certain date in a certain district name?'\r\n"
        
        # Set up member variables to track user input
        self.province = None 
        self.amphoe = None
        self.date = None
        self.general = None

        #Set up other variables to use NER to collect required information 
        self.nlp_model = spacy.load("en_core_web_sm")
        self.nlp_model = en_core_web_sm.load()
        df = pd.read_csv('ChatBotData/province_list.csv', header=None)
        self.PROVINCES = df[0].tolist()

        df = pd.read_csv('ChatBotData/amphoe_list.csv', header=None)
        self.AMPHOES = df[0].tolist()

    def __str__(self):
        return self.message
    
    def question_asked(self,text):
        if 'advice' in text.lower() or 'event' in text.lower() or 'do' in text.lower():
            return f"Gather supplies, including non-perishable foods, cleaning supplies, and water for several days, in case you must leave immediately or if services are cut off in your area. Keep important documents in a waterproof container."

        doc = self.nlp_model(text)
        
        provence_changed = False
        amphoe_changed = False
        date_changed = False


        for ent in doc.ents:
            print(ent)
            text = ent.text.replace(',', '').replace('.', '')

            if text in self.PROVINCES:
                provence_changed = True
                self.province = text
            
            elif f"{text} District" in self.AMPHOES:
                amphoe_changed = True
                self.amphoe = f"{text} District"

            elif ent.label_ == 'DATE':
                date_changed = True
                try:
                    date_obj = parser.parse(ent.text)
                    self.date = date_obj.month
                except:
                    self.date = datetime.now().month

        print(self.province, self.amphoe)
        if provence_changed and amphoe_changed:
            addition = ""
            if self.date is None:
                self.date = datetime.now().month
                addition = "To enquire about a specific month please enter a date."

            prediction = predict_flood_risk(self.date, self.amphoe, self.province)
            return f"Great, Ill find that prediction for you using {self.amphoe}, {self.province} and {month_number_to_name[self.date]}.\r\n {addition}\r\n" + \
            f"The probability is {prediction}!" 
        
        elif provence_changed or amphoe_changed:
            return f"Please enter both the provence and amphoe you would like to check was well as a date."

        else:
            return f"I'm not quite sure what you have asked of me. To get general advice ask about general advice.\r\n" + \
            "To find about your area ask about your amphoe, provence and a date you would like to enquire about."
        

chatbot = process_text()
print(chatbot.question_asked("I am located at Chiang Mai, Mueang Chiang Mai, Bangkok what are the chances of flooding"))
print(chatbot.question_asked("What is the current advice"))


