#!/bin/bash 

: """
Create an environment with the expected packages
Example use: 
source install.sh
"""

ENV_NAME="youtube-video"

uv venv --prompt $ENV_NAME
uv sync --all-extras
source .venv/bin/activate