sudo apt-get update

# Install python3.9
sudo apt-get install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get install python3.9

# Create python venv and install dependencies
python3.9 -m venv venv
venv/bin/pip install -r requirements.txt