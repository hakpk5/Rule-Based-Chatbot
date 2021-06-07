from os import name
from scrollable_frame import ScrollableFrame
# # importing regex and random libraries
import re
import random
import tkinter as tk


class ChatWindow(tk.Toplevel):
    # potential negative responses
    negative_responses = ("no", "nope", "nah", "naw", "not a chance", "sorry")
    # keywords for exiting the conversation
    exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later")
    # random starter questions
    random_questions = (
        "Why are you here? ",
        "Are there many humans like you? ",
        "What do you consume for sustenance? ",
        "Is there intelligent life on this planet? ",
        "Does Earth have a leader? ",
        "What planets have you visited? ",
        "What technology do you have on this planet? "
    )

    def __init__(self, master):
        super().__init__(master)

        self.protocol('WM_DELETE_WINDOW', master.destroy)

        self.alienbabble = {'describe_planet_intent': r'.*\s*your planet.*',
                            'answer_why_intent': r'why\sare.*',
                            'cubed_intent': r'.*cube.*(\d+)'
                            }

        self.resizable(False, False)
        self.geometry('300x400')
        self.transient(master)

        self.rowconfigure(0, weight=1)

        self.convo = ScrollableFrame(self, width=400)
        self.convo.grid(row=0, column=0, sticky='nsew')

        self.bar = tk.Frame(self)

        self.btnpressed = tk.BooleanVar(self, name='btn')
        self.msg = tk.Entry(self.bar, width=24, font=(None, 12))

        self.btn = tk.Button(self.bar, text="SEND",
                             width=4, command=self.send_msg)

        self.msg.pack(side=tk.LEFT)
        self.btn.pack(side=tk.LEFT)
        self.bar.grid(row=1, column=0, sticky='ew')

        self.greeted = False
        self.greet()

    def send_msg(self):
        message = self.msg.get()
        tk.Message(self.convo.window, text=message, bg="#eee",
                   width=256).grid(sticky='e', pady=5)
        self.btnpressed.set(True)
        self.chat(message)

    def greet(self):
        tk.Message(self.convo.window, width=256,
                   text="Hello there, what's your name?", bg="#eee").grid(sticky='w')

        self.wait_variable('btn')

        will_help = "Hi {}, I'm Etcetera. I'm not from this planet. Will you help me learn about your planet? ".format(
            self.msg.get())

        tk.Message(self.convo.window, width=256,
                   text=will_help, bg="#eee").grid(sticky='w')

        self.wait_variable('btn')

        if self.msg.get() in ChatWindow.negative_responses:
            tk.Message(self.convo.window, width=256,
                       text="Okay, have a nice earth day!", bg="#eee").grid(sticky='w')
            self.after(1000, self.master.destroy)
            return

        tk.Message(self.convo.window, width=256,
                   text=random.choice(self.random_questions), bg="#eee").grid(sticky='w')
        self.greeted = True

    def make_exit(self, reply):
        if reply in ChatWindow.exit_commands:
            tk.Message(self.convo.window, width=256,
                       text="Okay, have a nice earth day!", bg="#eee").grid(sticky='w')
            self.after(10, self.master.destroy)

        return False

    def chat(self, message):
        if not self.greeted:
            return
        reply = message

        if not self.make_exit(reply):
            tk.Message(self.convo.window, width=256,
                       text=self.match_reply(reply), bg="#eee").grid(sticky='w')

    def match_reply(self, reply):
        for key, value in self.alienbabble.items():
            intent = key
            regex_pattern = value
            found_match = re.match(regex_pattern, reply)
            if found_match and intent == "describe_planet_intent":
                return self.describe_planet_intent()
            elif found_match and intent == "answer_why_intent":
                return self.answer_why_intent()
            elif found_match and intent == "cubed_intent":
                return self.cubed_intent(found_match.groups()[0])
            else:
                return self.no_match_intent()

    def describe_planet_intent(self):
        responses = ("My planet is a utopia of diverse organisms and species.",
                     "I am from Opidipus, the capital of the Wayward Galaxies. ")
        return random.choice(responses)
    # Define .answer_why_intent():

    def answer_why_intent(self):
        responses = ("I come in peace", "I am here to collect data on your planet and its inhabitants",
                     "I heard the coffee is good", "Just checking, shut up!")
        return random.choice(responses)

    # Define .cubed_intent():
    def cubed_intent(self, number):
        return "Cubed Number is {}, is there anything else I can help you with?".format(int(number)**3)

    # Define .no_match_intent():
    def no_match_intent(self):
        responses = ("Please tell me more.", "Tell me more!", "Why do you say that?", "I see. Can you elaborate",
                     "Interesting, can you tell me something more on that", "I see, how do you think!", "Why?", "How do you think I feel when you say that?")
        return random.choice(responses)


if __name__ == "__main__":
    win = ChatWindow()
    win.mainloop()
