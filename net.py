#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
🌐 Python Network & System Information Tool
Tập hợp các thư viện thú vị để lấy thông tin mạng và hệ thống
"""

import requests
import socket
import psutil
import platform
import uuid
import subprocess
import json
import time
from datetime import datetime
import os
import sys

# Thêm màu sắc cho terminal
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'  # Thêm DIM màu

def print_header(title):
    """In header đẹp"""
    print(f"\n{Colors.CYAN}{'='*60}{Colors.RESET}")
    print(f"{Colors.YELLOW}{Colors.BOLD}{title.center(60)}{Colors.RESET}")
    print(f"{Colors.CYAN}{'='*60}{Colors.RESET}\n")

def print_info(label, value, color=Colors.WHITE):
    """In thông tin với format đẹp"""
    print(f"{Colors.GREEN}{label:<25}{Colors.RESET}: {color}{value}{Colors.RESET}")

# ==================== 1. THÔNG TIN IP VÀ MẠNG ====================
def get_network_info():
    """Lấy thông tin mạng cơ bản"""
    print_header("🌐 THÔNG TIN MẠNG")
    
    try:
        # IP local
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        print_info("Hostname", hostname)
        print_info("IP Local", local_ip)
        
        # IP Public (sử dụng nhiều service)
        public_ip_services = [
            "https://api.ipify.org",
            "https://ifconfig.me/ip", 
            "https://icanhazip.com",
            "https://ident.me"
        ]
        
        for service in public_ip_services:
            try:
                response = requests.get(service, timeout=3)
                if response.status_code == 200:
                    public_ip = response.text.strip()
                    print_info("IP Public", public_ip, Colors.CYAN)
                    break
            except:
                continue
        
        # Thông tin chi tiết về IP
        try:
            ip_info = requests.get(f"http://ip-api.com/json/{public_ip}").json()
            print_info("Quốc gia", f"{ip_info.get('country')} ({ip_info.get('countryCode')})")
            print_info("Thành phố", ip_info.get('city'))
            print_info("ISP", ip_info.get('isp'))
            print_info("Tọa độ", f"{ip_info.get('lat')}, {ip_info.get('lon')}")
            print_info("Timezone", ip_info.get('timezone'))
        except:
            print_info("Chi tiết IP", "Không lấy được", Colors.RED)
            
    except Exception as e:
        print_info("Lỗi", str(e), Colors.RED)

# ==================== 2. THÔNG TIN HỆ THỐNG ====================
def get_system_info():
    """Lấy thông tin hệ thống chi tiết"""
    print_header("💻 THÔNG TIN HỆ THỐNG")
    
    # Thông tin cơ bản
    print_info("Hệ điều hành", platform.system())
    print_info("Phiên bản OS", platform.release())
    print_info("Kiến trúc", platform.architecture()[0])
    print_info("Processor", platform.processor())
    print_info("Machine", platform.machine())
    print_info("Node", platform.node())
    
    # Thông tin chi tiết với psutil
    print_info("CPU Cores", psutil.cpu_count(logical=False))
    print_info("CPU Threads", psutil.cpu_count(logical=True))
    print_info("CPU Usage", f"{psutil.cpu_percent(interval=1)}%", Colors.YELLOW)
    
    # RAM
    memory = psutil.virtual_memory()
    print_info("RAM Total", f"{memory.total / (1024**3):.2f} GB")
    print_info("RAM Available", f"{memory.available / (1024**3):.2f} GB", Colors.GREEN)
    print_info("RAM Used", f"{memory.percent}%", Colors.YELLOW)
    
    # Disk
    disk = psutil.disk_usage('/')
    print_info("Disk Total", f"{disk.total / (1024**3):.2f} GB")
    print_info("Disk Free", f"{disk.free / (1024**3):.2f} GB", Colors.GREEN)
    print_info("Disk Used", f"{(disk.used / disk.total) * 100:.1f}%", Colors.YELLOW)

# ==================== 3. THÔNG TIN MẠNG CHI TIẾT ====================
def get_network_interfaces():
    """Lấy thông tin tất cả interface mạng"""
    print_header("🔌 NETWORK INTERFACES")
    
    interfaces = psutil.net_if_addrs()
    
    for interface_name, interface_addresses in interfaces.items():
        print(f"\n{Colors.BLUE}{Colors.BOLD}Interface: {interface_name}{Colors.RESET}")
        
        for address in interface_addresses:
            if str(address.family) == 'AddressFamily.AF_INET':
                print_info("  IPv4", address.address)
                print_info("  Netmask", address.netmask)
            elif str(address.family) == 'AddressFamily.AF_INET6':
                print_info("  IPv6", address.address)
            elif str(address.family) == 'AddressFamily.AF_PACKET':
                print_info("  MAC Address", address.address)

# ==================== 4. NETWORK STATISTICS ====================
def get_network_stats():
    """Thống kê mạng"""
    print_header("📊 NETWORK STATISTICS")
    
    net_io = psutil.net_io_counters()
    print_info("Bytes Sent", f"{net_io.bytes_sent / (1024**2):.2f} MB")
    print_info("Bytes Received", f"{net_io.bytes_recv / (1024**2):.2f} MB")
    print_info("Packets Sent", f"{net_io.packets_sent:,}")
    print_info("Packets Received", f"{net_io.packets_recv:,}")
    
    # Connections
    connections = psutil.net_connections()
    tcp_count = len([conn for conn in connections if conn.type == socket.SOCK_STREAM])
    udp_count = len([conn for conn in connections if conn.type == socket.SOCK_DGRAM])
    
    print_info("TCP Connections", tcp_count)
    print_info("UDP Connections", udp_count)

# ==================== 5. WIFI INFORMATION ====================
def get_wifi_info():
    """Lấy thông tin WiFi (Windows)"""
    print_header("📶 WIFI INFORMATION")
    
    try:
        if platform.system() == "Windows":
            # Lấy thông tin WiFi hiện tại - Sửa encoding
            result = subprocess.run(['netsh', 'wlan', 'show', 'profile'], 
                                  capture_output=True, text=True, encoding='utf-8', errors='ignore')
            
            if result.returncode == 0:
                profiles = []
                for line in result.stdout.split('\n'):
                    if 'All User Profile' in line:
                        profile = line.split(':')[1].strip()
                        profiles.append(profile)
                
                print_info("WiFi Profiles", f"{len(profiles)} networks saved")
                
                # Hiển thị một số profile
                for i, profile in enumerate(profiles[:5]):
                    print_info(f"  Network {i+1}", profile)
                
                if len(profiles) > 5:
                    print_info("  ...", f"và {len(profiles)-5} mạng khác")
            
            # Thông tin WiFi đang kết nối - Sửa encoding
            result = subprocess.run(['netsh', 'wlan', 'show', 'interfaces'], 
                                  capture_output=True, text=True, encoding='utf-8', errors='ignore')
            
            if result.returncode == 0:
                for line in result.stdout.split('\n'):
                    line = line.strip()
                    if 'SSID' in line and 'BSSID' not in line:
                        ssid = line.split(':')[1].strip()
                        print_info("Current SSID", ssid, Colors.CYAN)
                    elif 'Signal' in line:
                        signal = line.split(':')[1].strip()
                        print_info("Signal Strength", signal, Colors.GREEN)
        
        else:
            print_info("WiFi Info", "Chỉ hỗ trợ Windows", Colors.YELLOW)
            
    except Exception as e:
        print_info("WiFi Error", str(e), Colors.RED)

# ==================== 6. PING TEST ====================
def ping_test():
    """Test ping đến các server phổ biến"""
    print_header("🏓 PING TEST")
    
    test_hosts = [
        ("Google DNS", "8.8.8.8"),
        ("Cloudflare DNS", "1.1.1.1"),
        ("Google", "google.com"),
        ("Facebook", "facebook.com"),
        ("YouTube", "youtube.com")
    ]
    
    for name, host in test_hosts:
        try:
            if platform.system() == "Windows":
                result = subprocess.run(['ping', '-n', '1', host], 
                                      capture_output=True, text=True, encoding='utf-8', errors='ignore')
            else:
                result = subprocess.run(['ping', '-c', '1', host], 
                                      capture_output=True, text=True, encoding='utf-8', errors='ignore')
            
            if result.returncode == 0:
                # Tìm thời gian ping
                output = result.stdout
                if 'time=' in output:
                    time_part = output.split('time=')[1].split()[0]
                    print_info(f"Ping {name}", f"{time_part}", Colors.GREEN)
                elif 'Average =' in output:  # Windows format
                    time_part = output.split('Average =')[1].strip().split()[0]
                    print_info(f"Ping {name}", f"{time_part}", Colors.GREEN)
                else:
                    print_info(f"Ping {name}", "OK", Colors.GREEN)
            else:
                print_info(f"Ping {name}", "Failed", Colors.RED)
                
        except Exception as e:
            print_info(f"Ping {name}", "Error", Colors.RED)

# ==================== 7. SPEED TEST (đơn giản) ====================
def simple_speed_test():
    """Test tốc độ download đơn giản"""
    print_header("🚀 SPEED TEST")
    
    # Sử dụng URLs ổn định hơn
    test_urls = [
        ("Small File (100KB)", "https://httpbin.org/bytes/102400"),
        ("Medium File (1MB)", "https://httpbin.org/bytes/1048576")
    ]
    
    for name, url in test_urls:
        try:
            print(f"{Colors.YELLOW}Testing {name}...{Colors.RESET}")
            start_time = time.time()
            
            response = requests.get(url, timeout=15, stream=True)
            
            if response.status_code == 200:
                # Download với chunks để đo chính xác
                total_size = 0
                for chunk in response.iter_content(chunk_size=8192):
                    total_size += len(chunk)
                
                end_time = time.time()
                duration = end_time - start_time
                size_mb = total_size / (1024 * 1024)
                speed_mbps = (size_mb * 8) / duration  # Convert to Mbps
                
                print_info(f"  {name}", f"{speed_mbps:.2f} Mbps ({size_mb:.2f}MB in {duration:.2f}s)", Colors.GREEN)
            else:
                print_info(f"  {name}", f"HTTP {response.status_code}", Colors.RED)
                
        except requests.exceptions.Timeout:
            print_info(f"  {name}", "Timeout", Colors.RED)
        except requests.exceptions.RequestException as e:
            print_info(f"  {name}", f"Request Error: {str(e)[:30]}...", Colors.RED)
        except Exception as e:
            print_info(f"  {name}", f"Error: {str(e)[:30]}...", Colors.RED)

# ==================== 8. HARDWARE INFO ====================
def get_hardware_info():
    """Thông tin phần cứng chi tiết"""
    print_header("🔧 HARDWARE INFO")
    
    # CPU Info
    print(f"{Colors.BLUE}{Colors.BOLD}CPU Information:{Colors.RESET}")
    cpu_freq = psutil.cpu_freq()
    if cpu_freq:
        print_info("  Current Freq", f"{cpu_freq.current:.2f} MHz")
        print_info("  Max Freq", f"{cpu_freq.max:.2f} MHz")
    
    # Battery (if available)
    try:
        battery = psutil.sensors_battery()
        if battery:
            print(f"{Colors.BLUE}{Colors.BOLD}Battery Information:{Colors.RESET}")
            print_info("  Percentage", f"{battery.percent}%")
            print_info("  Plugged In", "Yes" if battery.power_plugged else "No")
            if not battery.power_plugged:
                secs_left = battery.secsleft
                if secs_left != psutil.POWER_TIME_UNKNOWN:
                    hours = secs_left // 3600
                    minutes = (secs_left % 3600) // 60
                    print_info("  Time Left", f"{hours}h {minutes}m")
    except:
        pass
    
    # Disk partitions
    print(f"{Colors.BLUE}{Colors.BOLD}Disk Partitions:{Colors.RESET}")
    partitions = psutil.disk_partitions()
    for partition in partitions:
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
            print_info(f"  {partition.device}", 
                      f"{partition_usage.total / (1024**3):.1f}GB total")
        except PermissionError:
            print_info(f"  {partition.device}", "Permission Denied")

# ==================== 9. UNIQUE IDENTIFIERS ====================
def get_unique_ids():
    """Lấy các ID duy nhất của máy"""
    print_header("🆔 UNIQUE IDENTIFIERS")
    
    # MAC Address
    mac = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) 
                   for elements in range(0,2*6,2)][::-1])
    print_info("MAC Address", mac)
    
    # UUID
    machine_uuid = str(uuid.uuid4())
    print_info("Random UUID", machine_uuid)
    
    # User info
    print_info("Username", os.getlogin())
    print_info("Home Directory", os.path.expanduser("~"))

# ==================== MENU CHÍNH ====================
def show_menu():
    """Hiển thị menu chính"""
    print(f"\n{Colors.MAGENTA}{Colors.BOLD}")
    print("🌐 PYTHON NETWORK & SYSTEM INFO TOOL")
    print("="*50)
    print(f"{Colors.RESET}")
    
    menu_items = [
        "1. 🌐 Thông tin mạng cơ bản",
        "2. 💻 Thông tin hệ thống", 
        "3. 🔌 Network interfaces",
        "4. 📊 Network statistics",
        "5. 📶 WiFi information",
        "6. 🏓 Ping test",
        "7. 🚀 Speed test (đơn giản)",
        "8. 🔧 Hardware info",
        "9. 🆔 Unique identifiers",
        "10. 🎯 Tất cả thông tin",
        "0. 🚪 Thoát"
    ]
    
    for item in menu_items:
        print(f"{Colors.CYAN}{item}{Colors.RESET}")

def main():
    """Chương trình chính"""
    
    while True:
        show_menu()
        
        try:
            choice = input(f"\n{Colors.YELLOW}Chọn chức năng (0-10): {Colors.RESET}")
            
            if choice == "1":
                get_network_info()
            elif choice == "2":
                get_system_info()
            elif choice == "3":
                get_network_interfaces()
            elif choice == "4":
                get_network_stats()
            elif choice == "5":
                get_wifi_info()
            elif choice == "6":
                ping_test()
            elif choice == "7":
                simple_speed_test()
            elif choice == "8":
                get_hardware_info()
            elif choice == "9":
                get_unique_ids()
            elif choice == "10":
                # Chạy tất cả
                get_network_info()
                get_system_info()
                get_network_interfaces()
                get_network_stats()
                get_wifi_info()
                ping_test()
                simple_speed_test()
                get_hardware_info()
                get_unique_ids()
            elif choice == "0":
                print(f"\n{Colors.GREEN}Cảm ơn bạn đã sử dụng! 👋{Colors.RESET}")
                break
            else:
                print(f"{Colors.RED}Lựa chọn không hợp lệ!{Colors.RESET}")
            
            input(f"\n{Colors.DIM}Nhấn Enter để tiếp tục...{Colors.RESET}")
            
        except KeyboardInterrupt:
            print(f"\n{Colors.YELLOW}Đã thoát chương trình!{Colors.RESET}")
            break
        except Exception as e:
            print(f"{Colors.RED}Lỗi: {e}{Colors.RESET}")

if __name__ == "__main__":
    # Cài đặt các thư viện cần thiết
    required_libraries = """
    Cần cài đặt các thư viện sau:
    
    pip install requests psutil
    
    Các thư viện được sử dụng:
    - requests: Gọi API và download
    - psutil: Thông tin hệ thống và mạng
    - socket: Network programming cơ bản
    - platform: Thông tin hệ điều hành
    - uuid: Tạo unique identifiers
    - subprocess: Chạy lệnh hệ thống
    """
    
    try:
        main()
    except ImportError as e:
        print(f"{Colors.RED}Thiếu thư viện: {e}{Colors.RESET}")
        print(f"{Colors.YELLOW}{required_libraries}{Colors.RESET}")