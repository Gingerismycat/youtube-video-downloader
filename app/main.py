from typing import Any
import logging

import param 
import panel as pn
from panel.viewable import Viewable
import subprocess
import argparse

from core.utils_logging import setup_logger, get_logging_level
from get_audio import generate_command

pn.extension(notifications=True)
logger = logging.getLogger(__file__)

# template config
TITLE = "Youtube Video Downloader"

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
    url = param.String()

    def __panel__(self) -> Viewable:
        
        
        self.file_format = pn.widgets.Select(name="File Type", options=["mp3", "mp4"])
        self.button = pn.widgets.Button(name='Download', icon='caret-right',button_type='primary')
        self.url_input = pn.widgets.TextInput.from_param(self.param.url, name="URL",placeholder="Paste your URL here...")
        #Set watchers
        self.button.on_click(self.download)

        self._layout = pn.Column(
            pn.Row(
                self.url_input,
                self.file_format,
            ),
            self.button,
        )
        return self._layout
    
    #@param.depends('url',watch=True)
    def download(self, button_press) -> None:
        if self.url_input.value == "":
            pn.state.notifications.error("Please type in the URL!")
        else:
            logger.info("Download button was clicked!")
            logger.info(f"{self.url_input.value}")
            logger.info(f"{self.file_format.value}")
            cmd = generate_command(self.url_input.value, self.file_format.value)
            print(cmd)
            print(self.url_input.value, type(self.url_input.value))
            subprocess.run(cmd, check=True)
            logger.info("Download Complete!")
            pn.state.notifications.success("Download Complete!")

if __name__ == "__main__":
    pass

else:
    setup_logger()
    logger = logging.getLogger("cae-dtx")
    logger.info(f"Logging level set from config as {get_logging_level()}")

    template = setup_template(app=PanelApp())
    template.servable()
    logger.info("Launching app/template from app/main.py")