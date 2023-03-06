# The screens dictionary contains the objects of the models and controllers
# of the screens of the application.


from Model.welcome_screen import Welcome_ScreenModel
from Controller.welcome_screen import Welcome_ScreenController
from Model.about_screen import About_me_ScreenModel
from Controller.about_screen import About_me_ScreenController
from Model.item_screen import Item_ScreenModel
from Controller.item_screen import Item_ScreenController
from Model.more_screen import More_ScreenModel
from Controller.more_screen import More_ScreenController
from Model.trajectory_screen import Trajectory_ScreenModel
from Controller.trajectory_screen import Trajectory_ScreenController
from Model.running_screen import Running_ScreenModel
from Controller.running_screen import Running_ScreenController

screens = {
    "welcome screen": {
        "model": Welcome_ScreenModel,
        "controller": Welcome_ScreenController,
    },

    "about screen": {
        "model": About_me_ScreenModel,
        "controller": About_me_ScreenController,
    },

    "item screen": {
        "model": Item_ScreenModel,
        "controller": Item_ScreenController,
    },

    "more screen": {
        "model": More_ScreenModel,
        "controller": More_ScreenController,
    },

    "trajectory screen": {
        "model": Trajectory_ScreenModel,
        "controller": Trajectory_ScreenController,
    },

    "running screen": {
        "model": Running_ScreenModel,
        "controller": Running_ScreenController,
    },
}