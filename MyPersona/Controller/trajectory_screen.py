import importlib

import View.Trajectory_Screen.trajectory_screen

# We have to manually reload the view module in order to apply the
# changes made to the code on a subsequent hot reload.
# If you no longer need a hot reload, you can delete this instruction.
importlib.reload(View.Trajectory_Screen.trajectory_screen)




class Trajectory_ScreenController:
    """
    The `Trajectory_ScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.trajectory_screen.Trajectory_ScreenModel
        self.view = View.Trajectory_Screen.trajectory_screen.Trajectory_ScreenView(controller=self, model=self.model)

    def get_view(self) -> View.Trajectory_Screen.trajectory_screen:
        return self.view
