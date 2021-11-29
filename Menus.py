"""
Menus.py
by Alex Villa 11-9-2021
adapted from Audio_Menu_State.py from A.Hornof (ajh) 10-27-2021

Uses Python 3.10 and pygame 2.0.2
----------------------------------------
"""

from State import State
import Sounds
import BookData

class Cursor:

    def __init__(self):
        self.pos = 0

    def UpdateCursor(self):
        self.pos += 1

    def ResetCursor(self):
        self.pos = 0

    def GetCursor(self):
        return self.pos
    
    def DecreaseCursor(self):
        self.pos -= 1

    def SetCursor(self, val):
        self.pos = val

CURSOR = Cursor()

class Menu_Home(State):

    def __init__(self):
        self.options = [(Sounds.general_not_available, "not_available")]
        self.option_numbers = len(self.options) - 1
        self.current = 0

    def handle_scroll_up(self) ->  None:
        if self.current < self.option_numbers:
            self.current += 1
        else:
            self.current = 0
        self.options[self.current][0].play()

    def handle_scroll_down(self) -> None: 
        if self.current > 0:
            self.current -= 1
        else:
            self.current = self.option_numbers
        self.options[self.current][0].play()

    def entering(self) -> None:
        print("Enterring Home Menu")
        self.options = [(Sounds.home_option_1, "continue"), (Sounds.home_option_2, "menu_new")]
        self.option_numbers = len(self.options) - 1
        Sounds.home_entering.play()
        Sounds.home_to_quit.chain()
        Sounds.general_for_help.chain()
        Sounds.general_your_selection.chain()
        self.options[self.current][0].chain()

    def handle_1(self) -> None:
        print("Scroll Down")
        self.handle_scroll_down()
    
    def handle_2(self) -> None:
        print("Scroll Up")
        self.handle_scroll_up()

    def handle_3(self) -> None:
        Sounds.help_running.play()
        Sounds.help_currently_in.chain()
        Sounds.help_home_menu.chain()
        Sounds.help_buttons.chain()
        Sounds.help_f.chain()
        Sounds.help_scroll_down.chain()
        Sounds.help_d.chain()
        Sounds.help_scroll_up.chain()
        Sounds.help_space.chain()
        Sounds.help_select_current.chain()
        Sounds.help_s.chain()
        Sounds.help_a.chain()
        Sounds.help_quit.chain()
        print("Press A or ; to quit the program")


    def handle_4(self) -> None:
        print("Quitting.")
        self.context.transition_to("menu_quitting")
        
    def handle_5(self) -> None: 
        print("Select")
        if self.options[self.current][1] == 'continue':
            if self.context.load_save():
                next_menu = self.context.get_mode()
                print("Successfully loaded save")
                self.context.transition_to(next_menu)
            else:
                print("No save loaded")
                Sounds.general_not_available.play()
        else:
            self.context.set_time(-1)
            self.context.transition_to(self.options[self.current][1])

class Menu_New(State):
    
    def __init__(self):
        self.options = BookData.books
        self.option_numbers = len(self.options) - 1
        self.current = 0

    def handle_scroll_up(self) ->  None:
        if self.current < self.option_numbers:
            self.current += 1
        else:
            self.current = 0
        self.options[self.current][0].play()

    def handle_scroll_down(self) -> None: 
        if self.current > 0:
            self.current -= 1
        else:
            self.current = self.option_numbers
        self.options[self.current][0].play()

    def entering(self) -> None:
        print("Enterring New Reading Menu")
        Sounds.help_book_selection.play()
        Sounds.general_your_selection.chain()
        self.options[self.current][0].chain()

    def handle_1(self) -> None:
        print("Scroll Down")
        self.handle_scroll_down()
    
    def handle_2(self) -> None:
        print("Scroll Up")
        self.handle_scroll_up()

    def handle_3(self) -> None:
        print("Help")
        Sounds.help_running.play()
        Sounds.help_currently_in.chain()
        Sounds.help_book_selection.chain()
        Sounds.help_buttons.chain()
        Sounds.help_f.chain()
        Sounds.help_scroll_down.chain()
        Sounds.help_d.chain()
        Sounds.help_scroll_up.chain()
        Sounds.help_space.chain()
        Sounds.help_select_current.chain()
        Sounds.help_s.chain()
        Sounds.help_a.chain()
        Sounds.help_back.chain()
        
    def handle_4(self) -> None:
        print("Quitting.")
        self.context.transition_back()

    def handle_5(self) -> None: 
        if self.options[self.current][1] == 'not_available':
            Sounds.general_not_available.play()
        else:
            print(self.options[self.current][1])
            self.context.set_current_book(self.options[self.current][1])
            self.context.transition_to("menu_chapters")

class Menu_Chapters(State):
    
    def __init__(self):
        self.options = [(Sounds.general_not_available, "not_available")]
        self.option_numbers = len(self.options) - 1
        self.current = 0

    def handle_scroll_up(self) ->  None:
        if self.current < self.option_numbers:
            self.current += 1
        else:
            self.current = 0
        self.options[self.current][0].play()

    def handle_scroll_down(self) -> None: 
        if self.current > 0:
            self.current -= 1
        else:
            self.current = self.option_numbers
        self.options[self.current][0].play()

    def entering(self) -> None:
        print("Enterring Select Chapter Menu")
        self.options = BookData.chapters[self.context.get_current_book()]
        self.option_numbers = len(self.options) - 1
        Sounds.help_chapter_selection.play()
        Sounds.general_your_selection.chain()
        self.options[self.current][0].chain()

    def handle_1(self) -> None:
        print("Scroll Down")
        self.handle_scroll_down()
    
    def handle_2(self) -> None:
        print("Scroll Up")
        self.handle_scroll_up()

    def handle_3(self) -> None:
        print("Help")
        Sounds.help_running.play()
        Sounds.help_currently_in.chain()
        Sounds.help_chapter_selection.chain()
        Sounds.help_buttons.chain()
        Sounds.help_f.chain()
        Sounds.help_scroll_down.chain()
        Sounds.help_d.chain()
        Sounds.help_scroll_up.chain()
        Sounds.help_space.chain()
        Sounds.help_select_current.chain()
        Sounds.help_s.chain()
        Sounds.help_a.chain()
        Sounds.help_back.chain()
        
    def handle_4(self) -> None:
        print("Quitting.")
        self.context.transition_back()

    def handle_5(self) -> None: 
        try:
            if self.options[self.current][1] == 'not_available':
                Sounds.general_not_available.play()
            else:
                # Play the sound of the chapter to see if it is available, if 
                check_if_present = BookData.audio_files[self.context.get_current_book()][self.options[self.current][1]][0]
                Sounds.file_present_test(check_if_present)
                self.context.set_current_chapter(self.options[self.current][1])
                self.context.set_time(-1)
                self.context.transition_to("menu_modes")
        except:
            Sounds.general_not_available.play()
        

class Menu_Modes(State):
    
    def __init__(self):
        self.options = [(Sounds.mode_standard, "menu_reading"), (Sounds.mode_headings, "menu_headings"), (Sounds.mode_topics, "menu_headings_and_topics"),]
        self.option_numbers = len(self.options) - 1
        self.current = 0

    def handle_scroll_up(self) ->  None:
        if self.current < self.option_numbers:
            self.current += 1
        else:
            self.current = 0
        self.options[self.current][0].play()
        print(self.options[self.current][1])

    def handle_scroll_down(self) -> None: 
        if self.current > 0:
            self.current -= 1
        else:
            self.current = self.option_numbers
        self.options[self.current][0].play()

    def entering(self) -> None:
        print("Enterring Mode Select Menu")
        Sounds.help_mode_selection.play()
        Sounds.general_your_selection.chain()
        self.options[self.current][0].chain()

    def handle_1(self) -> None:
        print("Scroll Down")
        self.handle_scroll_down()
    
    def handle_2(self) -> None:
        print("Scroll Up")
        self.handle_scroll_up()

    def handle_3(self) -> None:
        print("Help")
        Sounds.help_running.play()
        Sounds.help_currently_in.chain()
        Sounds.help_mode_selection.chain()
        Sounds.help_buttons.chain()
        Sounds.help_f.chain()
        Sounds.help_scroll_down.chain()
        Sounds.help_d.chain()
        Sounds.help_scroll_up.chain()
        Sounds.help_space.chain()
        Sounds.help_select_current.chain()
        Sounds.help_s.chain()
        Sounds.help_a.chain()
        Sounds.help_back.chain()
        
    def handle_4(self) -> None:
        print("Quitting.")
        self.context.transition_back()

    def handle_5(self) -> None: 
            print(self.options[self.current][1])
            self.context.set_mode(self.options[self.current][1])
            self.context.transition_to(self.options[self.current][1])

class Menu_Reading(State):

    def __init__(self) -> None:
        self.audio = None
        self.time = 0
        self.paused = False 
        self.filename = None
        self.length = 0

    def entering(self) -> None:
        print("Enterring Reading Menu")
        book = self.context.get_current_book()
        chapter = self.context.get_current_chapter()
        if book and chapter:
            try:
                filename, length, start = BookData.audio_files[book][chapter]
                if self.context.get_time() == -1: # -1 means continue reading from beginning
                    self.time = start
                if self.context.get_time() == -2: # -2 means continue from where the reading was
                    self.time = self.time # Dont change anything
                else: # A regular time means continue reading from save state 
                    self.time = self.context.get_time()
                self.filename = filename
                Sounds.help_standard_mode.play()
                Sounds.reading_reading_book.chain()
                BookData.book_titles_audio[self.filename][0].chain()
                Sounds.reading_chapter.chain()
                BookData.book_titles_audio[self.filename][1].chain()
                self.length = length
                self.audio = Sounds.load_audiobook(filename, length, self.time)
                self.audio.chain()
            except:
                print("corrupted save state")
                Sounds.reading_corrupt.play()
                self.context.clear_timeline()
                self.context.transition_to("menu_home")
        else:
            print("Error has occured")
            Sounds.general_not_available.play()
            self.context.clear_timeline()
            self.context.transition_to("menu_home")

    def handle_1(self) -> None:
        print("Rewind")
        Sounds.reading_rewind.play()
        self.time -= 30000
        if self.time <= 0:
            self.time = 0
            print("Beggining of Audio")
        self.audio = Sounds.load_audiobook(self.filename, self.length, self.time)
        self.audio.chain()
        
    def handle_2(self) -> None:
        print("Fast Forward")
        Sounds.reading_fastforward.play()
        self.time += 30000
        if self.time >= self.length:
            self.time = self.length
            print("Audio is Over")
            Sounds.reading_fastforward.play()
        self.audio = Sounds.load_audiobook(self.filename, self.length, self.time)
        self.audio.chain()
        
    def handle_3(self) -> None:
        if self.paused:
            print("Play")
            self.audio = Sounds.load_audiobook(self.filename, self.length, self.time)
            self.audio.play()
            self.paused = not self.paused
        else:
            print("Pause")
            self.time += self.audio.get_time()
            Sounds.help_running.play()
            Sounds.help_currently_in.chain()
            Sounds.help_standard_mode.chain()
            Sounds.reading_continue_audio.chain()
            Sounds.reading_reading_book.chain()
            BookData.book_titles_audio[self.filename][0].chain()
            Sounds.reading_chapter.chain()
            BookData.book_titles_audio[self.filename][1].chain()
            Sounds.help_buttons.chain()
            Sounds.help_f.chain()
            Sounds.help_fastforward.chain()
            Sounds.help_d.chain()
            Sounds.help_rewind.chain()
            Sounds.help_space.chain()
            Sounds.help_pause_and_play.chain()
            Sounds.help_s.chain()
            Sounds.help_a.chain()
            Sounds.help_save_and_back.chain()
            Sounds.reading_continue_audio.chain()
            self.paused = not self.paused

    def handle_4(self) -> None:
        print("Quit and Save")
        self.time += self.audio.get_time()
        book = self.context.get_current_book()
        chapter = self.context.get_current_chapter()
        mode = self.context.get_mode()
        self.context.temporary_save(f'{book}/{chapter}/{self.time}/{mode}')
        self.context.set_time(-2)
        self.context.transition_to('menu_saving')

    def handle_5(self) -> None:
        if self.paused:
            print("Play")
            Sounds.reading_play.play()
            self.audio = Sounds.load_audiobook(self.filename, self.length, self.time)
            self.audio.chain()
            self.paused = not self.paused
        else:
            print("Pause")
            self.time += self.audio.get_time()
            print(self.time)
            Sounds.reading_pause.play()
            self.paused = not self.paused
        

class Menu_Headings(State):

    def __init__(self) -> None:
        self.audio = None
        self.time = 0
        self.paused = False 
        self.filename = None
        self.pos = 0
        self.length = 0
        self.audio_list = []

    def entering(self) -> None:
        print("Enterring Headings Only Menu")
        book = self.context.get_current_book()
        chapter = self.context.get_current_chapter()
        if book and chapter:
            try:
                # in this mode, self.context.get_time() will return the current heading number
                filename = BookData.audio_files[book][chapter][0]
                if self.context.get_time() == -1: # -1 means continue reading from beginning
                    self.pos = 0
                elif self.context.get_time() == -2: # -2 means continue from where the reading was
                    self.pos = self.pos # Dont change anything
                else: # A regular time means continue reading from save state 
                    self.pos = self.context.get_time()
                self.filename = filename
                Sounds.help_headings_mode.play()
                Sounds.reading_reading_book.chain()
                BookData.book_titles_audio[self.filename][0].chain()
                Sounds.reading_chapter.chain()
                BookData.book_titles_audio[self.filename][1].chain()
                times_list = BookData.section_times[book][chapter]
                for entry in times_list:
                    if entry[2] ==  1:
                        new_sound = Sounds.load_audiobook(self.filename, entry[1], entry[0])
                        self.audio_list.append(new_sound)
                start = self.pos
                self.length = len(self.audio_list)
                CURSOR.SetCursor(start)
                for entry in range(start, len(self.audio_list)):
                    self.audio_list[entry].chain()
            except:
                print("corrupted save state")
                Sounds.general_not_available.play()
                self.context.clear_timeline()
                self.context.transition_to("menu_home")
        else:
            print("Error has occured")
            Sounds.general_not_available.play()
            self.context.clear_timeline()
            self.context.transition_to("menu_home")

    def handle_1(self) -> None:
        print("Rewind")
        Sounds.reading_rewind.play()
        CURSOR.DecreaseCursor()
        if CURSOR.GetCursor() < 0:
            CURSOR.ResetCursor()
            print("Beginning of Audio")
        for entry in range(CURSOR.GetCursor(), len(self.audio_list)):
            self.audio_list[entry].chain()
        
    def handle_2(self) -> None:
        print("Fast Forward")
        Sounds.reading_fastforward.play()
        
        if CURSOR.GetCursor() > self.length:
            CURSOR.SetCursor(self.length)
            print("End of Audio")
        for entry in range(CURSOR.GetCursor(), len(self.audio_list)):
            self.audio_list[entry].chain()
        
    def handle_3(self) -> None:
        if self.paused:
            print("Play")
            self.pos -= 1
            if self.pos < 0:
                self.pos = 0
                print("Beginning of Audio")
            Sounds.reading_play.play()
            CURSOR.SetCursor(self.pos)
            for entry in range(CURSOR.GetCursor(), len(self.audio_list)):
                self.audio_list[entry].chain()
            self.paused = not self.paused
        else:
            print("Pause")
            self.pos = CURSOR.GetCursor()
            Sounds.help_running.play()
            Sounds.help_currently_in.chain()
            Sounds.help_headings_mode.chain()
            Sounds.reading_continue_audio.chain()
            Sounds.reading_reading_book.chain()
            BookData.book_titles_audio[self.filename][0].chain()
            Sounds.reading_chapter.chain()
            BookData.book_titles_audio[self.filename][1].chain()
            Sounds.help_buttons.chain()
            Sounds.help_f.chain()
            Sounds.help_fastforward.chain()
            Sounds.help_d.chain()
            Sounds.help_rewind.chain()
            Sounds.help_space.chain()
            Sounds.help_pause_and_play.chain()
            Sounds.help_s.chain()
            Sounds.help_a.chain()
            Sounds.help_save_and_back.chain()
            Sounds.reading_continue_audio.chain()
            self.paused = not self.paused


    def handle_4(self) -> None:
        print("Quit and Save")
        self.pos = CURSOR.GetCursor()
        book = self.context.get_current_book()
        chapter = self.context.get_current_chapter()
        mode = self.context.get_mode()
        self.context.temporary_save(f'{book}/{chapter}/{self.pos}/{mode}')
        self.context.set_time(-2)
        self.context.transition_to('menu_saving')

    def handle_5(self) -> None:
        if self.paused:
            print("Play")
            Sounds.reading_play.play()
            self.pos -= 1
            if self.pos < 0:
                self.pos = 0
                print("Beginning of Audio")
            CURSOR.SetCursor(self.pos)
            for entry in range(CURSOR.GetCursor(), len(self.audio_list)):
                self.audio_list[entry].chain()
            self.paused = not self.paused
            
        else:
            print("Pause")
            self.pos = CURSOR.GetCursor()
            Sounds.reading_pause.play()
            self.paused = not self.paused


class Menu_Headings_And_Topics(State):

 
    def __init__(self) -> None:
        self.audio = None
        self.time = 0
        self.paused = False 
        self.filename = None
        self.pos = 0
        self.length = 0
        self.audio_list = []

    def entering(self) -> None:
        print("Enterring Headings and Topics Menu")
        book = self.context.get_current_book()
        chapter = self.context.get_current_chapter()
        if book and chapter:
            try:
                # in this mode, self.context.get_time() will return the current heading number
                filename = BookData.audio_files[book][chapter][0]
                if self.context.get_time() == -1: # -1 means continue reading from beginning
                    self.pos = 0
                elif self.context.get_time() == -2: # -2 means continue from where the reading was
                    self.pos = self.pos # Dont change anything
                else: # A regular time means continue reading from save state 
                    self.pos = self.context.get_time()
                self.filename = filename
                Sounds.help_topics_mode.chain()
                Sounds.reading_reading_book.chain()
                BookData.book_titles_audio[self.filename][0].chain()
                Sounds.reading_chapter.chain()
                BookData.book_titles_audio[self.filename][1].chain()
                times_list = BookData.section_times[book][chapter]
                for entry in times_list:
                    new_sound = Sounds.load_audiobook(self.filename, entry[1], entry[0])
                    self.audio_list.append(new_sound)
                start = self.pos
                self.length = len(self.audio_list)
                CURSOR.SetCursor(start)
                for entry in range(start, len(self.audio_list)):
                    self.audio_list[entry].chain()
            except:
                print("corrupted save state")
                Sounds.general_not_available.play()
                self.context.clear_timeline()
                self.context.transition_to("menu_home")
        else:
            print("Error has occured")
            Sounds.general_not_available.play()
            self.context.clear_timeline()
            self.context.transition_to("menu_home")

    def handle_1(self) -> None:
        print("Rewind")
        Sounds.reading_rewind.play()
        CURSOR.DecreaseCursor()
        if CURSOR.GetCursor() < 0:
            CURSOR.ResetCursor()
            print("Beginning of Audio")
        for entry in range(CURSOR.GetCursor(), len(self.audio_list)):
            self.audio_list[entry].chain()
        
    def handle_2(self) -> None:
        print("Fast Forward")
        Sounds.reading_fastforward.play()
        
        if CURSOR.GetCursor() > self.length:
            CURSOR.SetCursor(self.length)
            print("End of Audio")
        for entry in range(CURSOR.GetCursor(), len(self.audio_list)):
            self.audio_list[entry].chain()
        
    def handle_3(self) -> None:
        if self.paused:
            print("Play")
            self.pos -= 1
            if self.pos < 0:
                self.pos = 0
                print("Beginning of Audio")
            Sounds.reading_play.play()
            CURSOR.SetCursor(self.pos)
            for entry in range(CURSOR.GetCursor(), len(self.audio_list)):
                self.audio_list[entry].chain()
            self.paused = not self.paused
            
        else:
            print("Pause")
            self.pos = CURSOR.GetCursor()
            Sounds.help_running.play()
            Sounds.help_currently_in.chain()
            Sounds.help_topics_mode.chain()
            Sounds.reading_continue_audio.chain()
            Sounds.reading_reading_book.chain()
            BookData.book_titles_audio[self.filename][0].chain()
            Sounds.reading_chapter.chain()
            BookData.book_titles_audio[self.filename][1].chain()
            Sounds.help_buttons.chain()
            Sounds.help_f.chain()
            Sounds.help_fastforward.chain()
            Sounds.help_d.chain()
            Sounds.help_rewind.chain()
            Sounds.help_space.chain()
            Sounds.help_pause_and_play.chain()
            Sounds.help_s.chain()
            Sounds.help_a.chain()
            Sounds.help_save_and_back.chain()
            Sounds.reading_continue_audio.chain()
            self.paused = not self.paused


    def handle_4(self) -> None:
        print("Quit and Save")
        self.pos = CURSOR.GetCursor()
        book = self.context.get_current_book()
        chapter = self.context.get_current_chapter()
        mode = self.context.get_mode()
        self.context.temporary_save(f'{book}/{chapter}/{self.pos}/{mode}')
        self.context.set_time(-2)
        self.context.transition_to('menu_saving')

    def handle_5(self) -> None:
        if self.paused:
            print("Play")
            Sounds.reading_play.play()
            self.pos -= 1
            if self.pos < 0:
                self.pos = 0
                print("Beginning of Audio")
            CURSOR.SetCursor(self.pos)
            for entry in range(CURSOR.GetCursor(), len(self.audio_list)):
                self.audio_list[entry].chain()
            self.paused = not self.paused
            
        else:
            print("Pause")
            self.pos = CURSOR.GetCursor()
            Sounds.reading_pause.play()
            self.paused = not self.paused


class Menu_Quitting(State):
    
    def __init__(self):
        pass

    def entering(self) -> None:
        print("Enterring Quitting Menu")
        Sounds.quit_quit.play() 

    # Handle the four possible key inputs.
    def handle_1(self) -> None:
        print("Return to Previous Menu.")
        self.context.transition_back()

    def handle_2(self) -> None:
        print("Return to Previous Menu.")
        self.context.transition_back()

    def handle_3(self) -> None:
        print("Return to Previous Menu.")
        self.context.transition_back()

    def handle_4(self) -> None:
        print("Quitting.")
        Sounds.quit_bye.play()
        self.context.quit()

    def handle_5(self) -> None:
        print("Return to Previous Menu.")
        self.context.transition_back()

class Menu_Saving(State):
    
    def __init__(self):
        pass

    def entering(self) -> None:
        print("Press A again to save, space to cancel, or press any other button to go to home menu")
        Sounds.save_a.play()
        Sounds.save_space.chain()
        Sounds.save_any.chain()

    # Handle the four possible key inputs.
    def handle_1(self) -> None:
        print("Return Home and Dont Save.")
        self.context.clear_timeline()
        self.context.transition_to("menu_home")

    def handle_2(self) -> None:
        print("Return Home and Dont Save.")
        self.context.clear_timeline()
        self.context.transition_to("menu_home")

    def handle_3(self) -> None:
        print("Return Home and Dont Save.")
        self.context.clear_timeline()
        self.context.transition_to("menu_home")

    def handle_4(self) -> None:
        print("Returning Home and Saving.")
        self.context.set_save()
        self.context.clear_timeline()
        self.context.transition_to("menu_home")

    def handle_5(self) -> None:
        print("Go Back")
        self.context.transition_back()
