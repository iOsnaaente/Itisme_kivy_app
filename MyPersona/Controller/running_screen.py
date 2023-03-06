import importlib

import View.Running_Screen.running_screen

# We have to manually reload the view module in order to apply the
# changes made to the code on a subsequent hot reload.
# If you no longer need a hot reload, you can delete this instruction.
importlib.reload(View.Running_Screen.running_screen)




class Running_ScreenController:
    """
    The `Running_ScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.running_screen.Running_ScreenModel
        self.view = View.Running_Screen.running_screen.Running_ScreenView(controller=self, model=self.model)

    def get_view(self) -> View.Running_Screen.running_screen:
        return self.view
