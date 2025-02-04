import os
import time
import platform
import psutil
import logging

# Configure logging
logging.basicConfig(filename='autoworks.log', level=logging.INFO, format='%(asctime)s - %(message)s')

class AutoWorks:
    def __init__(self):
        self.user_alerts = []

    def monitor_processes(self):
        """Monitors running processes for suspicious activity."""
        suspicious_processes = ['keylogger.exe', 'hacktool.exe', 'malware.exe']
        running_processes = [p.info['name'] for p in psutil.process_iter(['name'])]
        
        for process in suspicious_processes:
            if process in running_processes:
                alert_message = f"Suspicious process detected: {process}"
                self.user_alerts.append(alert_message)
                logging.warning(alert_message)
    
    def check_privacy_settings(self):
        """Checks Windows privacy settings."""
        # Simulating privacy setting checks
        privacy_issues = []
        if not os.environ.get('NO_TRACKING'):
            privacy_issues.append("Windows tracking settings are enabled.")
        
        for issue in privacy_issues:
            self.user_alerts.append(issue)
            logging.warning(issue)

    def alert_user(self):
        """Alerts the user of any privacy risks found."""
        if self.user_alerts:
            for alert in self.user_alerts:
                print(f"ALERT: {alert}")
            # Reset alerts after notifying user
            self.user_alerts.clear()
        else:
            print("No privacy risks detected.")

    def run(self):
        """Runs the AutoWorks monitoring system."""
        if platform.system() != "Windows":
            print("AutoWorks is designed to run on Windows systems only.")
            return

        while True:
            self.monitor_processes()
            self.check_privacy_settings()
            self.alert_user()
            time.sleep(60)  # Check every minute


if __name__ == "__main__":
    auto_works = AutoWorks()
    auto_works.run()