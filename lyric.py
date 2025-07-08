# author: quangphucng
# 07.08.25 16h40
import time
import os

# Danh sách các câu và thời gian hiển thị
lyrics = [
    ("Vì từ đầu anh có gì đâu", 1),
    ("Ngoài những niềm đau là thiên mệnh", 2),
    ("Anh đã có mọi thứ anh mong", 1),
    ("Nhưng chẳng thể giữ em bên mình", 1),
    ("Gió cuốn trái tim hững hờ", 2),
    ("Mơ thời giờ cuốn quanh", 1.5),
    ("Em chẳng có mong đợi gì", 2),
    ("Mong chờ gì từ anh", 2),
    ("Tiếc chân thành", 1)
]

def typewriter_effect(text, typing_speed=0.05):
    """Hiệu ứng đánh máy - hiển thị từng ký tự"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(typing_speed)
    print()  # Xuống dòng sau khi hoàn thành

def karaoke_terminal(lyrics, typing_speed=0.05):
    """Chạy karaoke với hiệu ứng typewriter"""
    os.system('cls' if os.name == 'nt' else 'clear')  # Xóa màn hình terminal
    
    print("🎵 Karaoke Terminal - Typewriter Effect 🎵\n")
    time.sleep(1)
    
    for i, (line, delay) in enumerate(lyrics, 1):
        # Hiển thị số thứ tự câu
        # print(f"[{i}/{len(lyrics)}] ", end='')
        
        # Hiệu ứng typewriter cho từng câu
        typewriter_effect(line, typing_speed)
        
        # Nghỉ giữa các câu
        time.sleep(delay)
        # print()  # Thêm dòng trống
    
    print("🎶 Kết thúc! 🎶")

# Chạy với tốc độ gõ mặc định (0.05 giây/ký tự)
karaoke_terminal(lyrics)

# Hoặc có thể tùy chỉnh tốc độ:
# karaoke_terminal(lyrics, typing_speed=0.1)  # Chậm hơn
# karaoke_terminal(lyrics, typing_speed=0.03) # Nhanh hơn