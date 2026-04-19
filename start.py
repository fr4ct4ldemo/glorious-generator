import threading
import subprocess
import sys
import os

def run_bot():
    os.system("python glorious.py")

def run_dashboard():
    os.system("python dashboard/app.py")

if __name__ == "__main__":
    bot_thread = threading.Thread(target=run_bot)
    dashboard_thread = threading.Thread(target=run_dashboard)

    bot_thread.start()
    dashboard_thread.start()

    bot_thread.join()
    dashboard_thread.join()