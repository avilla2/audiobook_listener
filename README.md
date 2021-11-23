# audiobook_listener

The programmer should add “The Design of Everyday Things” Chapter 2 Audio in the data subdirectory under the name “Norman Chapter 2 Audio.ogg”. 
In order to run this application, the programmer should have Python 3.10.0 and Pygame 2.0.2 installed. The main file to run is P3.py
All the Python files included in this program are:

- P3.py
- Context.py
- State.py
- SoundObject.py
- SoundObjChain.py
- Menus.py
- Sounds.py
- BookData.py

Inside the Data Directory there should be:
- book_titles.ogg
- chapters.ogg
- menu_sounds.ogg
- menus2.ogg 
- menus3.ogg 
- menus4.ogg 
- menus5.ogg

The file imports in each file are as follows:
- P3.py
  -  Context.py
  - SoundObject
  - SoundObjChain
  - pygame (2.0.2)
  - __future__ (included)
- Context.py 
  - Menus.py
- State.py
  - abc (included)
- SoundObject.py 
  - pygame (2.0.2) 
  - os (included)
- SoundObjChain.py 
  - Menus
  - pygame (2.0.2)
- Menus.py
  - State.py
  - Sounds.py
  - BookData.py
- Sounds.py
  - SoundObject.py
- BookData.py 
  - Sounds.py
