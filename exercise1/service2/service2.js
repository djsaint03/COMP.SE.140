// service2.js
const express = require('express');
const { execSync } = require('child_process');
const app = express();

app.get('/', (req, res) => {
    // Collect container information
    const ip_address = execSync('hostname -I').toString().trim();
    const running_processes = execSync('ps -ax').toString().trim();
    const disk_space = execSync('df -h /').toString().trim();
    const time_since_boot = execSync('uptime -p').toString().trim();

    res.json({
        "IP Address": ip_address,
        "Running Processes": running_processes,
        "Disk Space": disk_space,
        "Time Since Last Boot": time_since_boot
    });
});

app.listen(5000, () => {
    console.log('Service2 is running on port 5000');
});
