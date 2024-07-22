import psutil
import schedule
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime

#Email configuration
EMAIL_ADDRESS = 'some@example.com'
EMAIL_PASSWORD = 'password'
RECIPIENT_EMAIL = 'some@example.com'
SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = '80'

def get_system_info():
    disk_usage = psutil.disk_usage('/')
    free_disk_space = disk_usage.free

    processes = []
    for p in psutil.process_iter(['name', 'memory_info']):
        try:
            processes.append((p.pid, p.info['name'], p.info['memory_info'].rss))
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

        processes.sort(key=lambda x: x[2], reverse=True)
        top_memory_processes = processes[:5]
    
    return free_disk_space, top_memory_processes

def write_log_file():
    free_disk_space, top_memory_processes = get_system_info()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_content = f"Timestamp: {timestamp}"
    log_content += f"Free Disk Space: {free_disk_space / (1024 * 1024 * 1024):.2f} GB \n"
    log_content += "Top 5 memory processes: "
    for pid, name, mem in top_memory_processes:
        log_content += f"PID: {pid}, Name: {name}, Memory Usage: {mem / (1024 * 1024):.2f} MB\n"
        with open("system_log.txt", "w") as log_file:
            log_file.write(log_content)

def send_email():
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = RECIPIENT_EMAIL
    msg['Subject'] = "System log"

    with open("system.log_txt", "rb") as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="system_log.txt"')
        msg.attach(part)
    
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL_ADDRESS, RECIPIENT_EMAIL, msg.as_string())

def job():
    write_log_file()
    send_email()
    schedule.every().day.at("09:00").do(job)
    schedule.every().day.at("19:00").do(job)

if __name__ == '__main__':
    while True:
        schedule.run_pending()
        time.sleep(1)