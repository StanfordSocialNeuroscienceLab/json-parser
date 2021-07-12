#!/bin/bash

# For Unix machines only
# Installs Python3 and JupyterLab
#
# Ian Richard Ferguson | Stanford University

LINK="https://raw.githubusercontent.com/Homebrew/install/master/install.sh"     # Install Homebrew
curl -fsSL -o install.sh $LINK
/bin/bash install.sh

export PATH=/usr/local/bin:$PATH >> ~/.bash_profile                             # Update shell profile (Bash & ZSH)
export PATH=/usr/local/bin:$PATH >> ~/.zshrc

source ~/.bash_profile
source ~/.zshrc

brew install python                                                             # Install Python3 and JupyterLab
brew install jupyterlab

brew unlink python && brew link python                                          # Re-link Python in case of any systematic issues with your local env

packages=("pandas" "numpy" "scikit-learn" "matplotlib" "seaborn")               # Installs several useful Python packages

for k in ${packages[@]}; do
  pip install $k
done

rm install.sh                                                                   # I was never here ...
