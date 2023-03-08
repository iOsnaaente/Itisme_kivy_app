import importlib

import View.More_Screen.more_screen

# We have to manually reload the view module in order to apply the
# changes made to the code on a subsequent hot reload.
# If you no longer need a hot reload, you can delete this instruction.
importlib.reload(View.More_Screen.more_screen)




class More_ScreenController:
    """
    The `More_ScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.more_screen.More_ScreenModel
        self.view = View.More_Screen.more_screen.More_ScreenView(controller=self, model=self.model)

    def get_view(self) -> View.More_Screen.more_screen:
        return self.view
