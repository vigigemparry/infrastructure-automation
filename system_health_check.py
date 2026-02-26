import shutil
import psutil

def check_system_health():
    # Проверка диска
    total, used, free = shutil.disk_usage("/")
    print(f"Disk Free: {free // (2**30)} GB")
    
    # Проверка процессора
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu_usage}%")

    if cpu_usage > 80:
        print("Warning: High CPU usage!")

if __name__ == "__main__":
    check_system_health()
