FROM anasty17/mltb:heroku

WORKDIR /usr/src/app
RUN chmod 777 /usr/src/app

RUN apt -qq update --fix-missing && \
    apt -qq install -y git \
    aria2 \
    wget \
    curl \
    busybox \
    unzip \
    unrar \
    tar \
    python3 \
    ffmpeg \
    python3-pip \
    p7zip-full \
    p7zip-rar
    
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD ["bash", "start.sh"]
