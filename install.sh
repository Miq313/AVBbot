sudo apt install build-essential software-properties-common -y

sudo apt-add-repository ppa:deadsnakes/ppa -y
sudo apt update -y && sudo apt full-upgrade -y
sudo apt install python3.9 python3.9-dev python3.9-venv -y
python3.9 -m pip install --upgrade pip

# Create python venv and install dependencies
python3.9 -m venv venv
venv/bin/pip install -r requirements.txt