"""
State.py
by Alex Villa
Adapted from A.Hornof (ajh) 11-3-2021, 11-8-2021

This file is part of a pushbutton-input audio-ouput system created by 
Anthony Hornof in the CIS 443/543 User Interfaces class that he is teaching.

This creates all the sounds needed by the menu system.
This script should get called once, when starting the main program.

Uses Python 3.10 and pygame 2.0.2
"""
import abc       # For abstract base classes.


class State(abc.ABC):

    """
    The abstract base class State class declares methods that all Concrete State
    objects should implement, and also provides a backreference to the Context
    object, associated with the State. This backreference can be used by States
    to transition the Context to another State. (From refactoring.guru.)

    The State class provides a template for all of the menus.
    """
    def __init__(self):
        self._context = None
    
    @property         # This is a getter decorator.
    def context(self):
        return self._context

    @context.setter   # This is a setter decorator.
    def context(self, context) -> None:
        self._context = context

    @abc.abstractmethod
    def entering(self) -> None:
        pass

    @abc.abstractmethod
    def handle_1(self) -> None:
        pass

    @abc.abstractmethod
    def handle_2(self) -> None:
        pass

    @abc.abstractmethod
    def handle_3(self) -> None:
        pass

    @abc.abstractmethod
    def handle_4(self) -> None:
        pass

    @abc.abstractmethod
    def handle_5(self) -> None:
        pass

