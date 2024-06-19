import psutil
import logging
from datetime import datetime

# Define thresholds
CPU_THRESHOLD = 80
MEM_THRESHOLD = 80
DISK_THRESHOLD = 90

# Configure logging
LOG_FILE = "/var/log/system_health.log"
logging.basicConfig(filename=LOG_FILE, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def log_message(level, message):
    print(message)
    if level == "info":
        logging.info(message)
    elif level == "alert":
        logging.warning(message)

# Check CPU usage
def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        log_message("alert", f"ALERT: CPU usage is at {cpu_usage}%")
    else:
        log_message("info", f"INFO: CPU usage is at {cpu_usage}%")

# Check memory usage
def check_memory_usage():
    mem = psutil.virtual_memory()
    mem_usage = mem.percent
    if mem_usage > MEM_THRESHOLD:
        log_message("alert", f"ALERT: Memory usage is at {mem_usage}%")
    else:
        log_message("info", f"INFO: Memory usage is at {mem_usage}%")

# Check disk space usage
def check_disk_usage():
    disk = psutil.disk_usage('/')
    disk_usage = disk.percent
    if disk_usage > DISK_THRESHOLD:
        log_message("alert", f"ALERT: Disk space usage is at {disk_usage}%")
    else:
        log_message("info", f"INFO: Disk space usage is at {disk_usage}%")

# Check number of running processes
def check_running_processes():
    process_count = len(psutil.pids())
    log_message("info", f"INFO: Number of running processes: {process_count}")

# Main function
def main():
    check_cpu_usage()
    check_memory_usage()
    check_disk_usage()
    check_running_processes()

if __name__ == "__main__":
    main()
