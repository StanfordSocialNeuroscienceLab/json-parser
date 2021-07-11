#!/bin/bash

# For Unix machines only
# Installs Python3 and JupyterLab
#
# Ian Richard Ferguson | Stanford University

# Install Homebrew
curl -fsSL -o install.sh https://raw.githubusercontent.com/Homebrew/install/master/install.sh
/bin/bash install.sh

# Update shell profile
export PATH=/usr/local/bin:$PATH >> ~/.bash_profile
export PATH=/usr/local/bin:$PATH >> ~/.zshrc

source ~/.bash_profile
source ~/.zshrc

# Install Python3 and JupyterLab
brew install python
brew install jupyterlab