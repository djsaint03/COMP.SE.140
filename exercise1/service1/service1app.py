import os
import json
import signal
import  requests
import socket
import time
from flask import Flask



app=Flask(__name__)
sleep_duration = int(os.getenv('SLEEP_DURATION', 0))
@app.route('/')
def system_info():
    # Collect information from the container
    ip_address = os.popen("hostname -I").read().strip()
    running_processes = os.popen("ps -ax").read().strip()
    disk_space = os.popen("df -h /").read().strip()
    time_since_boot = os.popen("uptime -p").read().strip()

    # Get information from Service2
    service2_info = requests.get('http://service2:5000').json()

    data = {
        "Service1": {
            "IP Address": ip_address,
            "Running Processes": running_processes,
            "Disk Space": disk_space,
            "Time Since Last Boot": time_since_boot
        },
        "Service2": service2_info
    }

    # Flattening the JSON
    flat_data = []
    for service, details in data.items():
        for key, value in details.items():
            flat_data.append(f"{service} - {key}: {value}")

    # Display as a single line
    single_line_result = " ||| ".join(flat_data)
    print(single_line_result)
    time.sleep(sleep_duration)
    return single_line_result

@app.route('/stop', methods=['POST'])
def stop_containers():
#still trying to make stop request
    os.kill(os.getpid(), signal.SIGINT)
    return "Stopping containers...", 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8199)
