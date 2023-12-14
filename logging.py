import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def start_bot():
    # Insert the  bot launch code 
    logging.info("Bot launch code should go here")

if __name__ == "__main__":
    logging.info("Starting the bot")
    try:
        start_bot()
    except Exception as e:
        logging.exception("An error occurred while starting the bot")
