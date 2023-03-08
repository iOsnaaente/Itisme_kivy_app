import importlib

import View.Welcome_Screen.welcome_screen

# We have to manually reload the view module in order to apply the
# changes made to the code on a subsequent hot reload.
# If you no longer need a hot reload, you can delete this instruction.
importlib.reload(View.Welcome_Screen.welcome_screen)



class Welcome_ScreenController:
    """
    The `Welcome_ScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model
        self.view = View.Welcome_Screen.welcome_screen.Welcome_ScreenView( controller = self, model = self.model)

    def get_view(self) -> View.Welcome_Screen.welcome_screen:
        return self.view

    def see_more( self ):
        print( 'button TELA VEJA MAIS pressed' )
        print( 'bg-universe path from model: ', self.model.bg_universe)
        print( 'my-photo path from model: ', self.model.my_photo)
        self.view.model_is_changed() 