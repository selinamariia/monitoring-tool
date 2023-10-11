import time
import psutil


def display_usage(cpu_usage, mem_usage, bars=50):
    cpu_percent = cpu_usage / 100.0
    cpu_bar = '*' * int(cpu_percent * bars) + '-' * (bars - int(cpu_percent * bars))
    
    mem_percent = mem_usage / 100.0
    mem_bar = '*' * int(mem_percent * bars ) + '-' * (bars - int(mem_percent * bars))

    print(f"CPU Usage: |{cpu_bar}| {cpu_usage:.2f}%  ")
    print(f"MEM Usage: |{mem_bar}| {mem_usage:.2f}%  ")


def display_networks():
    last_received = psutil.net_io_counters().bytes_recv
    last_sent = psutil.net_io_counters().bytes_sent
    last_total = last_received + last_sent

    bytes_received = psutil.net_io_counters().bytes_recv
    bytes_sent = psutil.net_io_counters().bytes_sent
    bytes_total = bytes_received + bytes_sent

    new_received = bytes_received - last_received 
    new_sent = bytes_sent - last_sent
    new_total = bytes_total - last_total

    mb_new_received =  new_received / 1024 / 1024
    mb_new_sent = new_sent / 1024 / 1024
    mb_new_total = new_total / 1024 / 1024

    print(f"{mb_new_received:.2f} MB received, {mb_new_sent:.2f} MB sent, {mb_new_total:.2f} MB total\n")
    last_received = bytes_received
    last_sent = bytes_sent
    last_total = bytes_total


while True:
    display_usage(psutil.cpu_percent(), psutil.virtual_memory().percent, 30)
    display_networks()
    time.sleep(0.5)



