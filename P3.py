"""
P3.py
by Alex Villa 11-2-2021
adapted from Audio_Menu_State.py from A.Hornof (ajh) 10-27-2021

User input: <Space>    5
            <D> or <J> 1
            <F> or <K> 2
            <S> or <L> 3
            <A> or <;> 4

Uses Python 3.10 and pygame 2.0.2
----------------------------------------
Sources for ideas:
eventlist.py from
https://www.pygame.org/docs/ref/examples.html#pygame.examples.eventlist.main
"""

# Import modules
from __future__ import annotations # For annotations in function arguments.
import pygame    # Currently using 2.0.2.

# The following should accompany this file, and were created by ajh.
from Context import Context
import SoundObject
import SoundObjChain


# Initialize Global Module Variables
last_state = None # Keep track of the last state.

# Create one instance of each menu.

def main():

    """
    This function is called when the program starts. it initializes everything
    it needs, and then loops until the program terminates.
    """

    # Initialize pygame.
    pygame.init()
    # Create a small window to make sure that pygame can be accessed.
    pygame.display.set_mode((100, 100))

    # Load the clock
    clock = pygame.time.Clock()
        
    # Create the one SoundObjChain object that the program should be using.
    # There should be only one. You should never have to access it directly.
    SoundObject_chain = SoundObjChain.SoundObjChain( )
    # Give the SoundObject module access to the  SoundObjChain object.
    SoundObject.set_SoundObjChain( SoundObject_chain )

    # Create the initial enterring-application sound.
    # Send in the data directory name, the sound file name, the start time,
    #   and the duration. Sometimes different sounds are in the same file.

    # Variables used within Main Loop
    program_running = True

    # Initialized the menu state.
    context = Context('menu_home')

    # Main Loop
    while program_running and context.program_running():

        # Limits the while loop to a max of 60 clock-ticks per second.
        clock.tick(60)

        # Handle Input Events
        for event in pygame.event.get():

            # This permits closing the pygame window to quit the program.
            if event.type == pygame.QUIT:
                program_running = False

            # Handle Keystroke Events
            elif event.type == pygame.KEYDOWN:

                # Button 1 is pressed
                if event.key == pygame.K_k or event.key == pygame.K_d:
                    context.button_1_press()

                # Button 2 is pressed
                elif event.key == pygame.K_j or event.key == pygame.K_f:
                    context.button_2_press()

                # Button 3 is pressed
                elif event.key == pygame.K_l or event.key == pygame.K_s:
                    context.button_3_press()

                # Button 4 is pressed
                elif event.key == pygame.K_SEMICOLON or event.key == pygame.K_a:
                    context.button_4_press()
                # Button 4 is pressed
                elif event.key == pygame.K_SPACE:
                    context.button_5_press()

                # <ESC> or <Q> quits
                elif event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    print("User pressed <ESC> or <Q>.")
                    # Ideally, this would give a warning before quitting,
                    #   but that is not implemented yet.
                    program_running = False

        # Stop the sound that is playing when it is done.
        SoundObject_chain.play_until_empty()

    # Done
    pygame.quit()



# This calls the 'main' function when this script is executed.
if __name__ == "__main__":
    main( )
