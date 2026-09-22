import json

print("Assignment: Python + Git Network Automation Case")

with open('secret.json', 'r') as json_file:
    ourjson = json.load (json_file)

network_inventory = [
    {
    "hostname": "RTR-CORE-01",
    "device_type": "router",
    "management_ip": "10.1.1.1",
    "location": "Main-IDF",
    "status": "operational",
    "cpu_usage": 15.2,
    "memory_usage": 42.1,
    "uptime_days": 89,
    "backup_status": "completed"
    },
    {
    "hostname": "SW-ACCESS-02",
    "device_type": "switch",
    "management_ip": "10.1.1.50",
    "location": "Floor-2-IDF",
    "status": "operational",
    "cpu_usage": 8.7,
    "memory_usage": 33.4,
    "uptime_days": 156,
    "backup_status": "completed"
    },
    {
    "hostname": "FW-DMZ-01",
    "device_type": "firewall",
    "management_ip": "10.1.1.254",
    "location": "DMZ-Rack",
    "status": "warning",
    "cpu_usage": 34.8,
    "memory_usage": 67.2,
    "uptime_days": 45,
    "backup_status": "failed"
    },
    {
    "hostname": "RTR-CORE-02",
    "device_type": "router",
    "management_ip": "10.1.1.15",
    "location": "Main-IDF",
    "status": "operational",
    "cpu_usage": 18.4,
    "memory_usage": 45.8,
    "uptime_days": 91,
    "backup_status": "completed"
    },
    {
    "hostname": "SW-ACCESS-03",
    "device_type": "switch",
    "management_ip": "10.1.1.51",
    "location": "Floor-3-IDF",
    "status": "operational",
    "cpu_usage": 12.1,
    "memory_usage": 28.9,
    "uptime_days": 210,
    "backup_status": "completed"
    },
    {
    "hostname": "FW-ABC-02",
    "device_type": "firewall",
    "management_ip": "10.1.1.253",
    "location": "ABC-Rack",
    "status": "warning",
    "cpu_usage": 89.5,
    "memory_usage": 92.1,
    "uptime_days": 12,
    "backup_status": "failed"
    },
    {
    "hostname": "WLC-MAIN-01",
    "device_type": "wireless_controller",
    "management_ip": "10.1.1.100",
    "location": "Main-IDF",
    "status": "operational",
    "cpu_usage": 22.3,
    "memory_usage": 55.6,
    "uptime_days": 340,
    "backup_status": "completed"
    },
    {
    "hostname": "SW-ACCESS-01",
    "device_type": "switch",
    "management_ip": "10.1.1.10",
    "location": "Main-IDF",
    "status": "warning",
    "cpu_usage": 65.2,
    "memory_usage": 78.4,
    "uptime_days": 42,
    "backup_status": "failed"
    }
]

print("=== NETWORK OPERATIONAL REPORT ===")
print(f"Total devices monitored:{len(network_inventory)}")

def print_totals (inventory):
    counts_device_type = {}
    counts_location = {}

    for device in inventory:
        d_type = device["device_type"]
        loc = device["location"]
        counts_device_type[d_type] = counts_device_type.get(d_type, 0) + 1
        counts_location[loc] = counts_location.get(loc, 0) + 1

    print(f"Totals by device type: {counts_device_type}")
    print(f"Totals by location: {counts_location}")

print_totals(network_inventory)

print("\n--- DEVICE STATUS SUMMARY---")
for device in network_inventory:
    status_indicator = "OK" if device["status"] == "operational" else "NOK"
    print(f"{status_indicator} {device['hostname']:15} | {device['device_type']:8} | {device['location']:12} | CPU: {device['cpu_usage']:5}%")

print("\n--- DEVICES NEEDING ATTENTION ---")
for device in network_inventory:
    if device["cpu_usage"] > 60 or device["memory_usage"] > 80 or device["backup_status"] == "failed" or device["status"] == "warning" or device["uptime_days"] < 10:
        print(f" Check {device['hostname']}")