import os
import json
import  requests
from flask import Flask


app=Flask(__name__)
@app.route('/')
def system_info():
    # Collect information from the container
    ip_address = os.popen("hostname -I").read().strip()
    running_processes = os.popen("ps -ax").read().strip()
    disk_space = os.popen("df -h /").read().strip()
    time_since_boot = os.popen("uptime -p").read().strip()

    # Get information from Service2
    service2_info = requests.get('http://service2:5000').json()

    return json.dumps({
        "Service1": {
            "IP Address": ip_address,
            "Running Processes": running_processes,
            "Disk Space": disk_space,
            "Time Since Last Boot": time_since_boot
        },
        "Service2": service2_info
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8199)

