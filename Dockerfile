FROM anasty17/mltb:heroku

WORKDIR /usr/src/app
RUN chmod 777 /usr/src/app


COPY requirements.txt .
RUN pip3 install --no-cache-dir pyrogram \
    tgcrypto \
    aria2p \
    asyncio \
    python3 \
    python-dotenv \
    aiohttp \
    lxml \
    requests \
    Pillow 

COPY . .

CMD ["bash", "start.sh"]
