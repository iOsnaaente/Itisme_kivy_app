import importlib

import View.Item_Screen.item_screen

# We have to manually reload the view module in order to apply the
# changes made to the code on a subsequent hot reload.
# If you no longer need a hot reload, you can delete this instruction.
importlib.reload(View.Item_Screen.item_screen)




class Item_ScreenController:
    """
    The `Item_ScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.item_screen.Item_ScreenModel
        self.view = View.Item_Screen.item_screen.Item_ScreenView(controller=self, model=self.model)

    def get_view(self) -> View.Item_Screen.item_screen:
        return self.view
