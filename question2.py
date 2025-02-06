import psutil
import time

# Define the threshold for the CPU usage
THRESHOLD = 80

# To monitor CPU usage
def monitor_cpu():
    print("Monitoring CPU usage...")
    try:
        while True:
            # Get the current CPU usage as a percentage
            cpu_usage = psutil.cpu_percent(interval=1)
            
            # Debug: print CPU usage for each check
            print(f"Current CPU usage: {cpu_usage}%")
            
            # Check if the CPU usage exceeds the threshold
            if cpu_usage > THRESHOLD:
                print(f"Alert! CPU usage exceeds threshold: {cpu_usage}%")
            
            # Sleep for a while before checking again
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")
    except Exception as e:
        print(f"Error occurred: {e}")

# Start monitoring CPU
monitor_cpu()
