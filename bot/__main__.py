from pyrogram.handlers import MessageHandler
from utils.restart_fn import restart
from bot import RESTART_COMMAND, DOWNLOAD_DIR


if __name__ == "__main__":
    # create download directory, if not exist
    if not os.path.isdir(DOWNLOAD_DIR):
        os.makedirs(DOWNLOAD_DIR)
    # Starting The Bot
    app.start()
    
    restart_com = MessageHandler(
        restart,
        filters=filters.command([RESTART_COMMAND]),
    )
    app.add_handler(restart_command)
    
    
    logging.info(f"@{(app.get_me()).username} Bot Started! 😎")
    
    idle()
    
    app.stop()
