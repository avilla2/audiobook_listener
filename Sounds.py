"""
Sounds.py
by Alex Villa
Adapted from A.Hornof (ajh) 11-3-2021, 11-8-2021

This file is part of a pushbutton-input audio-ouput system created by 
Anthony Hornof in the CIS 443/543 User Interfaces class that he is teaching.

This creates all the sounds needed by the menu system.
This script should get called once, when starting the main program.

Uses Python 3.10 and pygame 2.0.2
"""

# GLOBAL VARIABLES
DATA_DIR = "data"                # Data subdirectory.
S_FILE_NAV = "menu_sounds.ogg"   # Navigation sounds file name.
TITLES_NAV = "book_titles.ogg"
CHAPTERS_NAV =  "chapters.ogg"
MENUS2 = 'menus2.ogg'
MENUS3 = 'menus3.ogg'
MENUS4 = 'menus4.ogg'
MENUS5 = 'menus5.ogg'

import SoundObject

def load_audiobook(filename, length, start = 0):
    return SoundObject.SoundObject(DATA_DIR, filename, start, length)

def file_present_test(filename):
    """
    will cause error if fails, use this function in a try except block only
    """
    load_audiobook(filename, 3000, 0).load_sound(DATA_DIR, filename)


# General Sounds
general_not_available = SoundObject.SoundObject(DATA_DIR, MENUS2, 11647, 822)
general_your_selection = SoundObject.SoundObject(DATA_DIR, MENUS2, 6659, 1315)
general_for_help = SoundObject.SoundObject(DATA_DIR, MENUS2, 4522, 1891)

# Book Titles
book_1 = SoundObject.SoundObject(DATA_DIR, S_FILE_NAV, 20670, 1648)
book_2 = SoundObject.SoundObject(DATA_DIR, TITLES_NAV, 733, 3160)
book_3 = SoundObject.SoundObject(DATA_DIR, TITLES_NAV, 4442, 1420)
book_4 = SoundObject.SoundObject(DATA_DIR, TITLES_NAV, 6457, 3068)
book_5 = SoundObject.SoundObject(DATA_DIR, TITLES_NAV, 9801, 2702)
book_6 = SoundObject.SoundObject(DATA_DIR, TITLES_NAV, 13190, 3297)
book_7 = SoundObject.SoundObject(DATA_DIR, TITLES_NAV, 29265, 1695)
book_8 = SoundObject.SoundObject(DATA_DIR, TITLES_NAV, 22212, 1466)
book_9 = SoundObject.SoundObject(DATA_DIR, TITLES_NAV, 24456, 1099)
book_10 = SoundObject.SoundObject(DATA_DIR, TITLES_NAV, 26471, 1969)
book_11 = SoundObject.SoundObject(DATA_DIR, TITLES_NAV, 17311, 4259)

# Chapter Titles
chapter_1_book_1 = SoundObject.SoundObject(DATA_DIR, CHAPTERS_NAV, 1127, 3031)
chapter_2_book_1 = SoundObject.SoundObject(DATA_DIR, CHAPTERS_NAV, 5009, 2680)
chapter_3_book_1 = SoundObject.SoundObject(DATA_DIR, CHAPTERS_NAV, 8566, 2680)
chapter_4_book_1 = SoundObject.SoundObject(DATA_DIR, CHAPTERS_NAV, 12048, 1854)
chapter_5_book_1 = SoundObject.SoundObject(DATA_DIR, CHAPTERS_NAV, 14778, 1929)

# Home Sounds
home_option_1 = SoundObject.SoundObject(DATA_DIR, S_FILE_NAV, 5769, 1681)
home_option_2 = SoundObject.SoundObject(DATA_DIR, S_FILE_NAV, 8143, 1681)
home_entering = SoundObject.SoundObject(DATA_DIR, S_FILE_NAV, 890, 1253)
home_to_quit = SoundObject.SoundObject(DATA_DIR, MENUS2, 2165, 1891)

# New Reading Menu Sounds
new_entering = SoundObject.SoundObject(DATA_DIR, S_FILE_NAV, 19121, 857)

# Quitting Menu Sounds
quit_quit =  SoundObject.SoundObject(DATA_DIR, S_FILE_NAV, 15725, 1088)
quit_bye = SoundObject.SoundObject(DATA_DIR, S_FILE_NAV, 17637, 659)

# Mode Menu Sounds
mode_standard = SoundObject.SoundObject(DATA_DIR, MENUS4, 822, 1430)
mode_headings = SoundObject.SoundObject(DATA_DIR, MENUS4, 2788, 1597)
mode_topics = SoundObject.SoundObject(DATA_DIR, MENUS5, 3476, 2406)

# Reading Menu Sounds
reading_entering = SoundObject.SoundObject(DATA_DIR, S_FILE_NAV, 10516, 1319)
reading_book_name = SoundObject.SoundObject(DATA_DIR, S_FILE_NAV, 12461, 2472)
reading_rewind = SoundObject.SoundObject(DATA_DIR, MENUS4, 7174, 655)
reading_fastforward = SoundObject.SoundObject(DATA_DIR, MENUS4, 9795, 679)
reading_pause = SoundObject.SoundObject(DATA_DIR, MENUS4, 10928, 477)
reading_play = SoundObject.SoundObject(DATA_DIR, MENUS4, 11595, 310)
reading_reading_book = SoundObject.SoundObject(DATA_DIR, MENUS5, 802, 1012)
reading_chapter = SoundObject.SoundObject(DATA_DIR, MENUS5, 2082, 802)
reading_continue_audio = SoundObject.SoundObject(DATA_DIR, MENUS5, 6397, 2807)
reading_corrupt = SoundObject.SoundObject(DATA_DIR, MENUS5, 9873, 1318)

# Save Menu Sounds
save_a = SoundObject.SoundObject(DATA_DIR, MENUS5, 11744, 2731)
save_space = SoundObject.SoundObject(DATA_DIR, MENUS5, 14781, 2425)
save_any = SoundObject.SoundObject(DATA_DIR, MENUS5, 17798, 3246)

# Help Sounds
help_running = SoundObject.SoundObject(DATA_DIR, MENUS2, 13017, 1836)
help_currently_in = SoundObject.SoundObject(DATA_DIR, MENUS2, 15155, 1398)
help_home_menu = SoundObject.SoundObject(DATA_DIR, MENUS2, 16717, 795)
help_book_selection = SoundObject.SoundObject(DATA_DIR, MENUS2, 17868, 1178)
help_chapter_selection = SoundObject.SoundObject(DATA_DIR, MENUS2, 19210, 1315)
help_mode_selection = SoundObject.SoundObject(DATA_DIR, MENUS2, 20964, 1343)
help_standard_mode = SoundObject.SoundObject(DATA_DIR, MENUS2, 22800, 1535)
help_headings_mode = SoundObject.SoundObject(DATA_DIR, MENUS2, 25835, 1139)
help_topics_mode = SoundObject.SoundObject(DATA_DIR, MENUS2, 27464, 2741)
help_buttons = SoundObject.SoundObject(DATA_DIR, MENUS3, 692, 1039)
help_f = SoundObject.SoundObject(DATA_DIR, MENUS3, 2077, 1731)
help_d = SoundObject.SoundObject(DATA_DIR, MENUS3, 4147, 1673)
help_space = SoundObject.SoundObject(DATA_DIR, MENUS3, 6193, 1212)
help_s = SoundObject.SoundObject(DATA_DIR, MENUS3, 7751, 2635)
help_a = SoundObject.SoundObject(DATA_DIR, MENUS3, 11136, 2154)
help_scroll_down = SoundObject.SoundObject(DATA_DIR, MENUS3, 13655, 1750)
help_scroll_up = SoundObject.SoundObject(DATA_DIR, MENUS3, 15444, 1654)
help_select_current = SoundObject.SoundObject(DATA_DIR, MENUS3, 17329, 1500)
help_quit = SoundObject.SoundObject(DATA_DIR, MENUS3, 19271, 1096)
help_back = SoundObject.SoundObject(DATA_DIR, MENUS3, 20752, 654)
help_fastforward = SoundObject.SoundObject(DATA_DIR, MENUS3, 21954, 1715)
help_skip = SoundObject.SoundObject(DATA_DIR, MENUS3, 24034, 1514)
help_previous = SoundObject.SoundObject(DATA_DIR, MENUS3, 26000, 1661)
help_pause_and_play = SoundObject.SoundObject(DATA_DIR, MENUS3, 28053, 924)
help_save_and_back = SoundObject.SoundObject(DATA_DIR, MENUS3, 29339, 924)
help_rewind = SoundObject.SoundObject(DATA_DIR, MENUS4, 8330, 1168)


