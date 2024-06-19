import requests
import logging
from datetime import datetime

# Configuration
URL = "http://example.com"  # Replace with the URL of your application
LOG_FILE = "/var/log/application_uptime.log"
SUCCESS_CODES = [200]  # List of HTTP status codes indicating the application is up

# Configure logging
logging.basicConfig(filename=LOG_FILE, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def check_application_status(url):
    try:
        response = requests.get(url, timeout=10)
        status_code = response.status_code

        if status_code in SUCCESS_CODES:
            log_message("info", f"Application is up. Status code: {status_code}")
            return True
        else:
            log_message("alert", f"Application is down. Status code: {status_code}")
            return False

    except requests.RequestException as e:
        log_message("alert", f"Application is down. Error: {e}")
        return False

def log_message(level, message):
    print(message)
    if level == "info":
        logging.info(message)
    elif level == "alert":
        logging.error(message)

if __name__ == "__main__":
    is_up = check_application_status(URL)
    if is_up:
        log_message("info", "The application is functioning correctly.")
    else:
        log_message("alert", "The application is not responding or is unavailable.")
