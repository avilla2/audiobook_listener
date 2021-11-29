"""
Context.py
by Alex Villa
Adapted from A.Hornof (ajh) 11-3-2021, 11-8-2021

This file is part of a pushbutton-input audio-ouput system created by 
Anthony Hornof in the CIS 443/543 User Interfaces class that he is teaching.

This creates all the sounds needed by the menu system.
This script should get called once, when starting the main program.

Uses Python 3.10 and pygame 2.0.2
"""
import Menus

MenuInstances = {
                "menu_home": Menus.Menu_Home(),
                "menu_reading": Menus.Menu_Reading(),
                "menu_new": Menus.Menu_New(), 
                "menu_quitting": Menus.Menu_Quitting(),
                "menu_chapters": Menus.Menu_Chapters(),
                "menu_modes": Menus.Menu_Modes(),
                "menu_headings": Menus.Menu_Headings(),
                "menu_headings_and_topics": Menus.Menu_Headings_And_Topics(),
                "menu_options": Menus.Menu_Options()
                }
                
# Initialize Global Module Variables
last_state = [] # Keep track of the last state.

class Context:
    """
    The Context defines the interface of interest to clients. It also maintains
    a reference to an instance of a State subclass, which represents the currently
    active menu in the Context. (Code and comments from https://refactoring.guru.)
    """

    # Private class variable.
    _state = None   # A reference to the current state of the Context.
    _program_running = True

    # Public class variables.

    def __init__(self, state_lookup: str) -> None:
    # (In the above line, ": State" and "-> None" are annotations.)
    # This sets the initial menu the users arrives at.
        state = MenuInstances[state_lookup]
        global last_state
        print(f"Context: Initializing Context to {type(state).__name__}")
        last_state.append(self._state)  # Keep track of the last state.
        self._state = state         # Uses @property (the getter decorator)
        self._state.context = self  # Uses @context.setter (setter decorator)
        self._state.entering()  
        self._temp_save = None # Temporary variable only, not to be accessed
        self.old_save = None
        self.mode = "menu_reading"
        self.current_book = None
        self.current_chapter = None
        self.time = -1
        self.times_list = [] # stores the audio objects for headings and headings/topic sentences modes
        self._temp_time = 0
        self.switch_from = None

    def temporary_save(self, save: str):
        self._temp_save = save

    def temporary_time(self, time: int):
        self._temp_time = time
        print("Temporary Time:", self._temp_time)

    def load_save(self) -> bool:
        try:
            f = open('data/savestate.txt', 'r')
            save = f.readline()
            data = save.split('/')
            self.current_book = data[0]
            self.current_chapter = data[1]
            self.time = int(data[2])
            self.mode = data[3]
            return True
        except:
            print("No previous Save")
            self.old_save = None
            self.current_book = None
            self.current_chapter = None
            self.time = 0
            return False
    
    def convert_time_stamp(self, from_mode, to_mode):
        """
        Convert a time stamp from one mode to another mode
        """
        if from_mode == "menu_headings":
            if to_mode == "menu_reading":
                self.time = self._temp_time
                print("Converted")
        if from_mode == "menu_headings_and_topics":
            if to_mode == "menu_reading":
                self.time = self._temp_time

    def set_times_list(self, objects):
        self.times_list = objects

    def get_times_list(self):
        return self.times_list

    def set_switch_from(self, value):
        self.switch_from = value

    def get_switch_from(self):
        return self.switch_from

    def set_save(self):
        f = open('data/savestate.txt', 'w')
        f.write(self._temp_save)
        f.close()

    def set_mode(self, mode): 
        self.mode = mode

    def get_mode(self):
        return self.mode

    def set_time(self, time):
        self.time = time
    
    def get_time(self):
        return self.time

    def set_current_book(self, book):
        self.current_book = book
    
    def get_current_book(self):
        return self.current_book

    def set_current_chapter(self, chapter):
        self.current_chapter = chapter
    
    def get_current_chapter(self):
        return self.current_chapter
    
    # Other menu objects must be able to change the current menu at runtime.
    def transition_to(self, state_lookup: str):
        state = MenuInstances[state_lookup]
        global last_state
        print(f"Context: Transition to {type(state).__name__}")
        last_state.append(self._state) # Keep track of the last state.
        self._state = state         # Uses @property (the getter decorator)
        self._state.context = self  # Uses @context.setter (setter decorator)
        self._state.entering()            # Enter the state.

    def transition_back(self):
        global last_state
        self._state = last_state.pop()
        self._state.context = self
        self._state.entering()
        
    def clear_timeline(self):
        global last_state
        last_state = []
    
    def timeline_skip(self):
        global last_state
        last_state.pop()

    # Quit the program
    def quit(self):
        self._program_running = False

    # Getter for _program_running
    def program_running(self):
        return (self._program_running)

    # The Context delegates part of its behavior to the current State object.
    #   The functions handle each possible button press.
    def button_1_press(self):
        self._state.handle_1()
    def button_2_press(self):
        self._state.handle_2()
    def button_3_press(self):
        self._state.handle_3()
    def button_4_press(self):
        self._state.handle_4()
    def button_5_press(self):
        self._state.handle_5()
