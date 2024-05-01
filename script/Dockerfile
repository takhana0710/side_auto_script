FROM python:3.9
RUN mkdir /script
WORKDIR /script
COPY . /script
# 安裝 chrome
# RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
#     echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list && \
#     apt-get update -qqy && \
#     apt-get -qqy install google-chrome-stable && \
#     rm /etc/apt/sources.list.d/google-chrome.list && \
#     rm -rf /var/lib/apt/lists/* /var/cache/apt/*
# install google chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable
RUN apt-get install -yqq unzip
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/
# 安裝指定在 requirements.txt 的 python 套件
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Define environment variable

CMD ["python3", "allgame.py"]