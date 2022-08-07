from time import sleep
from bot import aria2, get_client, DOWNLOAD_DIR
from shutil import rmtree




def sendMessage(text: str, bot, message: Message):
    try:
        return bot.sendMessage(message.chat_id,
                            reply_to_message_id=message.message_id,
                            text=text, allow_sending_without_reply=True, parse_mode='HTMl', disable_web_page_preview=True)
    except RetryAfter as r:
        LOGGER.warning(str(r))
        sleep(r.retry_after * 1.5)
        return sendMessage(text, bot, message)
    except Exception as e:
        LOGGER.error(str(e))
        return
      
def clean_all():
    aria2.remove_all(True)
    #get_client().torrents_delete(torrent_hashes="all")
    try:
        rmtree(DOWNLOAD_DIR)
    except:
        pass
