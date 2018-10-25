
# Selenium Installation
To create virtual Environment with python3 and install dependencies:
```
python3 -m venv venv-ucto
source venv-ucto/bin/activate
pip install -r requirements.txt
```

Chrome driver should be downloaded and placed to directory that in $PATH(like /usr/bin).
```
wget https://chromedriver.storage.googleapis.com/2.43/chromedriver_linux64.zip
unzip hromedriver_linux64.zip
sudo mv chromedriver /usr/bin/
```
Selenium Server which can be downloaded from https://www.seleniumhq.org/download/ should be started (Openjdk or Oracle Java  should be installed before run this):
```
 nohup java -jar selenium-server-standalone-3.14.0.jar &
```
nohup is used for start at background.

# Crawling

Crawling can be started with:
```
python crawler.py
```