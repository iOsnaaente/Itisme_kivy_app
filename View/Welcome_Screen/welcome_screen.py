from View.base_screen import BaseScreenView
from kivymd.uix.floatlayout import MDFloatLayout 

from kivy.lang import Builder 

import os 
PATH = os.path.dirname( __file__ )


class Welcome_ScreenView( BaseScreenView ):

    def __init__(self, **kw):
        super().__init__(**kw)
        Builder.load_file( PATH + '/welcome_screen.kv' )


    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
        