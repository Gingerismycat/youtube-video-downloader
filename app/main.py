from typing import Any
import logging

import param 
import panel as pn
from panel.viewable import Viewable

from core.utils_logging import setup_logger, get_logging_level

# template config
TITLE = "VUK'S COOL APP"

def setup_template(app: Any, sidebar: list[Any] = None):
    """Return a configured template instance."""
    sidebar = sidebar or []  # if None, use empty list to ensure a sidebar is not used
    template = pn.template.BootstrapTemplate(
        title=TITLE,
        sidebar=sidebar,
        header_background="#808080",
    )
    template.main.append(app)
    return template


class SideBarViewer(pn.viewable.Viewer):
    """Sidebar Viewer."""

    def __panel__(self) -> Viewable:
        """Return panel layout."""

        self._layout = pn.Column()

        return self._layout


class PanelApp(pn.viewable.Viewer):
    """A neat Panel application."""

    # This is the data you want to keep track off
    # Set these as class attributes 
    int_value = param.Integer()
    my_bool = param.Boolean()

    def __panel__(self) -> Viewable:
        """Return panel layout."""
        # Inside the __panel__ method, add the layout to your component and define 
        # the widgets you want. If a widget needs to be "track", instantiate it from 
        # one of the class "param" objects (i.e., `my_bool`)
        self.my_static_text = pn.widgets.StaticText(name="foo", value="foo")

        # This is the layout, it controls the "layout" of your app. 
        self._layout = pn.Row(
            pn.Column(
                pn.widgets.IntSlider.from_param(self.param.int_value, start=0, end=10, step=1),
                pn.widgets.Checkbox.from_param(self.param.my_bool, name="checkbox", value=True), 
            ),
            pn.widgets.Select(name="dropdown", options=["a", "b", "c"]), 
            self.my_static_text, 
        )

        return self._layout
    
    @param.depends("int_value", watch=True)
    def set_integer(self): 
        print(self.int_value)
        print(self.my_bool)
        
        if self.my_bool is True:
            self.my_static_text.value = "I'm True!"
        else: 
            self.my_static_text.value = "I'm False!"


    
if __name__ == "__main__":
    pass

else:
    setup_logger()
    logger = logging.getLogger("cae-dtx")
    logger.info(f"Logging level set from config as {get_logging_level()}")

    template = setup_template(app=PanelApp(), sidebar=SideBarViewer())
    template.servable()
    logger.info("Launching app/template from app/main.py")