from Model.base_model import BaseScreenModel

import os 
PATH = os.path.dirname( __file__ )
PATH_IMAGE = PATH.removesuffix('/Model') + '/images'

class Welcome_ScreenModel( BaseScreenModel ):

    __universe = PATH_IMAGE + '/universe.png'

    @property 
    def bg_universe( self ):
        return self.__universe 
    
    @bg_universe.setter
    def bg_universe( self, value ):
        self.__universe = value



    __my_photo = PATH_IMAGE + '/itismephoto-no-bg.png'
    
    @property
    def my_photo(self):
        return self.__my_photo 
    
    @my_photo.setter
    def my_photo( self, value ):
        self.__my_photo = value