import time

# ANSI escape sequences cho màu sắc
RESET = "\033[0m"
FAINT = "\033[2m" 
CYAN = "\033[36m"
WHITE = "\033[37m"
YELLOW = "\033[33m"
GRAY = "\033[90m"
RED = "\033[31m"

# Danh sách lời bài hát với màu sắc, thời gian delay và tốc độ đánh máy
lyrics = [
    (f"{WHITE}Anh vui{RESET}", 1.2, 0.01),
    (f"{WHITE}Sao nước mắt cứ tuôn trào{RESET}", 2.5, 0.01),
    (f"{WHITE}Chẳng phải như thế quá tốt hay sao{RESET}", 3.0, 0.01),
    (f"{WHITE}Anh ta đáng giá những gì cho{RESET}", 2.5, 0.01),
    (f"{WHITE}Người lại nhìn anh trong chẳng ra sao{RESET}", 3.0, 0.01),
    (f"{WHITE}Cũng đừng thối{RESET}", 1.8, 0.01),
]

def typewriter_effect(text, speed=0.1):
    """Hiệu ứng đánh máy - hiển thị từng ký tự"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(speed)
    print()  # Xuống dòng sau khi hoàn thành

def display_lyrics():
    """Hiển thị lời bài hát với hiệu ứng màu sắc và timing"""
    # typewriter_effect(f"{CYAN}=== CHƯƠNG TRÌNH HIỂN THỊ LỜI BÀI HÁT ==={RESET}", 0.05)
    print()
    
    for lyric_data in lyrics:
        # Xử lý cả format cũ (2 giá trị) và format mới (3 giá trị)
        if len(lyric_data) == 3:
            line, delay, speed = lyric_data
        else:
            line, delay = lyric_data
            speed = 0.08  # Tốc độ mặc định
        
        # Hiển thị từng ký tự với tốc độ tùy chỉnh
        typewriter_effect(line, speed)
        time.sleep(delay)
    
    print()
    typewriter_effect(f"{GRAY}--- Kết thúc ---{RESET}", 0.05)

def add_lyric():
    """Thêm câu hát mới"""
    new_line = input(f"{YELLOW}Nhập câu hát mới: {RESET}")
    try:
        delay = float(input(f"{YELLOW}Nhập thời gian delay sau câu này (giây): {RESET}"))
        speed = float(input(f"{YELLOW}Nhập tốc độ đánh máy (0.05 = nhanh, 0.2 = chậm): {RESET}") or "0.08")
        lyrics.append((f"{WHITE}{new_line}{RESET}", delay, speed))
        typewriter_effect(f"{CYAN}Đã thêm câu hát mới!{RESET}", 0.05)
    except ValueError:
        typewriter_effect(f"{RED}Lỗi: Vui lòng nhập số hợp lệ!{RESET}", 0.05)

def show_menu():
    """Hiển thị menu chính"""
    print(f"\n{CYAN}=== MENU ==={RESET}")
    print("1. Phát lời bài hát")
    print("2. Thêm câu hát mới")
    print("3. Xem danh sách lời bài hát")
    print("4. Thoát")

def show_lyrics_list():
    """Hiển thị danh sách tất cả lời bài hát"""
    typewriter_effect(f"\n{CYAN}=== DANH SÁCH LỜI BÀI HÁT ==={RESET}", 0.05)
    for i, lyric_data in enumerate(lyrics, 1):
        # Xử lý cả format cũ (2 giá trị) và format mới (3 giá trị)
        if len(lyric_data) == 3:
            line, delay, speed = lyric_data
            speed_info = f", tốc độ: {speed}s/ký tự"
        else:
            line, delay = lyric_data
            speed_info = ""
        
        # Loại bỏ ANSI codes để hiển thị text thuần
        clean_line = line.replace(WHITE, "").replace(RESET, "")
        print(f"{i}. {clean_line} (nghỉ: {delay}s{speed_info})")

def main():
    """Chương trình chính"""
    while True:
        show_menu()
        choice = input(f"\n{YELLOW}Chọn chức năng (1-4): {RESET}")
        
        if choice == "1":
            display_lyrics()
        elif choice == "2":
            add_lyric()
        elif choice == "3":
            show_lyrics_list()
        elif choice == "4":
            print(f"{CYAN}Tạm biệt!{RESET}")
            break
        else:
            print(f"{RED}Lựa chọn không hợp lệ! Vui lòng chọn 1-4.{RESET}")

if __name__ == "__main__":
    main()