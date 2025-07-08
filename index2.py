import time
import os
import sys
import random
import threading
from datetime import datetime
import json

# ==================== MÀU SẮC & HIỆU ỨNG ====================
class Colors:
    # Basic Colors
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    REVERSE = "\033[7m"
    
    # Text Colors
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    
    # Bright Colors
    BRIGHT_BLACK = "\033[90m"
    BRIGHT_RED = "\033[91m"
    BRIGHT_GREEN = "\033[92m"
    BRIGHT_YELLOW = "\033[93m"
    BRIGHT_BLUE = "\033[94m"
    BRIGHT_MAGENTA = "\033[95m"
    BRIGHT_CYAN = "\033[96m"
    BRIGHT_WHITE = "\033[97m"
    
    # Background Colors
    BG_BLACK = "\033[40m"
    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_YELLOW = "\033[43m"
    BG_BLUE = "\033[44m"
    BG_MAGENTA = "\033[45m"
    BG_CYAN = "\033[46m"
    BG_WHITE = "\033[47m"

class Effects:
    @staticmethod
    def rainbow_text(text):
        """Tạo hiệu ứng rainbow cho text"""
        colors = [Colors.RED, Colors.YELLOW, Colors.GREEN, Colors.CYAN, Colors.BLUE, Colors.MAGENTA]
        result = ""
        for i, char in enumerate(text):
            if char != ' ':
                result += colors[i % len(colors)] + char + Colors.RESET
            else:
                result += char
        return result
    
    @staticmethod
    def gradient_text(text, start_color, end_color):
        """Tạo hiệu ứng gradient cho text"""
        # Simplified gradient effect
        mid_point = len(text) // 2
        result = ""
        for i, char in enumerate(text):
            if i < mid_point:
                result += start_color + char + Colors.RESET
            else:
                result += end_color + char + Colors.RESET
        return result
    
    @staticmethod
    def glow_effect(text, color):
        """Tạo hiệu ứng phát sáng"""
        return f"{color}{Colors.BOLD}{text}{Colors.RESET}"
    
    @staticmethod
    def typewriter_with_sparks(text, speed=0.05):
        """Hiệu ứng đánh máy với tia lửa"""
        sparkles = ["✨", "⭐", "💫", "🌟", "✴️", "💥"]
        for i, char in enumerate(text):
            print(char, end='', flush=True)
            if random.random() > 0.8:  # 20% chance cho sparkle
                spark = random.choice(sparkles)
                print(f" {spark}", end='', flush=True)
                time.sleep(0.1)
                print(f"\b\b ", end='', flush=True)
            time.sleep(speed)
        print()

class AudioEffects:
    @staticmethod
    def play_sound_effect(effect_type):
        """Phát âm thanh hiệu ứng đơn giản"""
        try:
            if effect_type == "start":
                # Âm thanh bắt đầu
                for freq in [440, 554, 659]:
                    AudioEffects.beep(freq, 0.1)
            elif effect_type == "complete":
                # Âm thanh hoàn thành
                for freq in [523, 659, 784, 1047]:
                    AudioEffects.beep(freq, 0.15)
            elif effect_type == "error":
                # Âm thanh lỗi
                AudioEffects.beep(200, 0.3)
        except:
            pass  # Bỏ qua nếu không thể phát âm thanh
    
    @staticmethod
    def beep(frequency, duration):
        """Tạo âm beep đơn giản"""
        try:
            import winsound
            winsound.Beep(int(frequency), int(duration * 1000))
        except:
            # Fallback cho các hệ điều hành khác
            print(f"\a", end='', flush=True)

class ProgressBar:
    def __init__(self, total, length=50):
        self.total = total
        self.length = length
        self.current = 0
    
    def update(self, value):
        self.current = value
        percent = (self.current / self.total) * 100
        filled = int((self.current / self.total) * self.length)
        bar = "█" * filled + "░" * (self.length - filled)
        
        # Rainbow progress bar
        rainbow_bar = ""
        colors = [Colors.RED, Colors.YELLOW, Colors.GREEN, Colors.CYAN, Colors.BLUE, Colors.MAGENTA]
        for i, char in enumerate(bar):
            if char == "█":
                rainbow_bar += colors[i % len(colors)] + char + Colors.RESET
            else:
                rainbow_bar += Colors.DIM + char + Colors.RESET
        
        print(f"\r{Colors.CYAN}Progress: {rainbow_bar} {percent:.1f}%{Colors.RESET}", end='', flush=True)

# ==================== DỮ LIỆU & QUẢN LÝ ====================
class LyricsManager:
    def __init__(self, filename="lyrics_data.json"):
        self.filename = filename
        self.lyrics = self.load_lyrics()
    
    def load_lyrics(self):
        """Tải dữ liệu từ file JSON"""
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            # Dữ liệu mặc định
            return [
                {"text": "Anh vui", "delay": 1.2, "speed": 0.08, "color": "WHITE"},
                {"text": "Sao nước mắt cứ tuôn trào", "delay": 2.5, "speed": 0.08, "color": "CYAN"},
                {"text": "Chẳng phải như thế quá tốt hay sao", "delay": 3.0, "speed": 0.08, "color": "YELLOW"},
                {"text": "Anh ta đáng giá những gì cho", "delay": 2.5, "speed": 0.08, "color": "GREEN"},
                {"text": "Người lại nhìn anh trong chẳng ra sao", "delay": 3.0, "speed": 0.08, "color": "MAGENTA"},
                {"text": "Cũng đừng thối", "delay": 1.8, "speed": 0.08, "color": "RED"},
            ]
    
    def save_lyrics(self):
        """Lưu dữ liệu vào file JSON"""
        try:
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump(self.lyrics, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"{Colors.RED}Lỗi khi lưu file: {e}{Colors.RESET}")
    
    def add_lyric(self, text, delay, speed, color="WHITE"):
        """Thêm lời bài hát mới"""
        self.lyrics.append({
            "text": text,
            "delay": delay,
            "speed": speed,
            "color": color
        })
        self.save_lyrics()

# ==================== HIỆU ỨNG NÂNG CAO ====================
class AdvancedEffects:
    @staticmethod
    def clear_screen():
        """Xóa màn hình"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    @staticmethod
    def center_text(text, width=80):
        """Căn giữa text"""
        return text.center(width)
    
    @staticmethod
    def create_border(text, char="═", color=Colors.CYAN):
        """Tạo khung viền cho text"""
        lines = text.split('\n')
        max_length = max(len(line) for line in lines)
        
        border_top = f"{color}╔{'═' * (max_length + 2)}╗{Colors.RESET}"
        border_bottom = f"{color}╚{'═' * (max_length + 2)}╝{Colors.RESET}"
        
        result = [border_top]
        for line in lines:
            result.append(f"{color}║{Colors.RESET} {line.ljust(max_length)} {color}║{Colors.RESET}")
        result.append(border_bottom)
        
        return '\n'.join(result)
    
    @staticmethod
    def animate_text_wave(text, delay=0.1):
        """Hiệu ứng sóng cho text"""
        for i in range(len(text) + 10):
            display = ""
            for j, char in enumerate(text):
                distance = abs(i - j)
                if distance < 3:
                    if distance == 0:
                        display += f"{Colors.BRIGHT_YELLOW}{Colors.BOLD}{char}{Colors.RESET}"
                    elif distance == 1:
                        display += f"{Colors.YELLOW}{char}{Colors.RESET}"
                    else:
                        display += f"{Colors.DIM}{char}{Colors.RESET}"
                else:
                    display += char
            
            print(f"\r{display}", end='', flush=True)
            time.sleep(delay)
        print()
    
    @staticmethod
    def matrix_rain(duration=3):
        """Hiệu ứng mưa Matrix"""
        import random
        
        def rain():
            chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
            start_time = time.time()
            
            while time.time() - start_time < duration:
                line = ""
                for _ in range(80):
                    if random.random() > 0.7:
                        char = random.choice(chars)
                        line += f"{Colors.GREEN}{char}{Colors.RESET}"
                    else:
                        line += " "
                print(line)
                time.sleep(0.05)
        
        threading.Thread(target=rain, daemon=True).start()

# ==================== CHƯƠNG TRÌNH CHÍNH ====================
class UltraLyricsPlayer:
    def __init__(self):
        self.manager = LyricsManager()
        self.is_playing = False
        
    def show_welcome_screen(self):
        """Màn hình chào mừng thanh lịch"""
        AdvancedEffects.clear_screen()
        
        # Logo đơn giản và đẹp
        print(f"\n{Colors.CYAN}")
        print("    ╔═══════════════════════════════════╗")
        print("    ║                                   ║")
        print("    ║        LYRICS  PLAYER             ║")
        print("    ║                                   ║")
        print("    ║     Phiên bản nâng cao 2.0       ║")
        print("    ║                                   ║")
        print("    ╚═══════════════════════════════════╝")
        print(f"{Colors.RESET}\n")
        
        print(f"{Colors.WHITE}    Chào mừng bạn đến với trình phát lời bài hát{Colors.RESET}")
        print(f"{Colors.DIM}    Với các hiệu ứng typewriter đặc biệt{Colors.RESET}\n")
        
        # Loading đơn giản
        print(f"{Colors.YELLOW}    Đang khởi tạo", end="", flush=True)
        for i in range(3):
            time.sleep(0.5)
            print(".", end="", flush=True)
        print(f" Hoàn thành!{Colors.RESET}\n")
        
        print(f"{Colors.GREEN}    Nhấn Enter để bắt đầu...{Colors.RESET}")
        input()
    
    def show_menu(self):
        """Menu chính đẹp và không dị hợm"""
        AdvancedEffects.clear_screen()
        
        # Logo đơn giản
        print(f"{Colors.CYAN}{Colors.BOLD}")
        print("    ██╗     ██╗   ██╗██████╗ ██╗ ██████╗███████╗")
        print("    ██║     ╚██╗ ██╔╝██╔══██╗██║██╔════╝██╔════╝")
        print("    ██║      ╚████╔╝ ██████╔╝██║██║     ███████╗")
        print("    ██║       ╚██╔╝  ██╔══██╗██║██║     ╚════██║")
        print("    ███████╗   ██║   ██║  ██║██║╚██████╗███████║")
        print("    ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝ ╚═════╝╚══════╝")
        print(f"{Colors.RESET}\n")
        
        print(f"{Colors.WHITE}{Colors.BOLD}    Lyrics Player - Phiên bản đặc biệt{Colors.RESET}")
        print(f"{Colors.DIM}    Tổng lời bài hát: {len(self.manager.lyrics)}{Colors.RESET}\n")
        
        # Menu đơn giản không emoji
        print(f"{Colors.YELLOW}┌─────────────────────────────────────┐{Colors.RESET}")
        print(f"{Colors.YELLOW}│{Colors.RESET}              MENU CHÍNH             {Colors.YELLOW}│{Colors.RESET}")
        print(f"{Colors.YELLOW}├─────────────────────────────────────┤{Colors.RESET}")
        print(f"{Colors.YELLOW}│{Colors.RESET} {Colors.BRIGHT_WHITE}1.{Colors.RESET} Phát lời bài hát               {Colors.YELLOW}│{Colors.RESET}")
        print(f"{Colors.YELLOW}│{Colors.RESET} {Colors.BRIGHT_WHITE}2.{Colors.RESET} Thêm lời mới                   {Colors.YELLOW}│{Colors.RESET}")
        print(f"{Colors.YELLOW}│{Colors.RESET} {Colors.BRIGHT_WHITE}3.{Colors.RESET} Xem danh sách                  {Colors.YELLOW}│{Colors.RESET}")
        print(f"{Colors.YELLOW}│{Colors.RESET} {Colors.BRIGHT_WHITE}4.{Colors.RESET} Cài đặt                       {Colors.YELLOW}│{Colors.RESET}")
        print(f"{Colors.YELLOW}│{Colors.RESET} {Colors.BRIGHT_WHITE}0.{Colors.RESET} Thoát                          {Colors.YELLOW}│{Colors.RESET}")
        print(f"{Colors.YELLOW}└─────────────────────────────────────┘{Colors.RESET}\n")
    
    def display_lyrics_with_effects(self):
        """Phát lời bài hát với hiệu ứng đẹp và thanh lịch"""
        if not self.manager.lyrics:
            print(f"{Colors.RED}Không có lời bài hát nào để phát!{Colors.RESET}")
            return
        
        AdvancedEffects.clear_screen()
        self.is_playing = True
        
        # Header đơn giản
        print(f"{Colors.CYAN}{'═' * 50}{Colors.RESET}")
        print(f"{Colors.WHITE}{Colors.BOLD}              ĐANG PHÁT NHẠC              {Colors.RESET}")
        print(f"{Colors.CYAN}{'═' * 50}{Colors.RESET}\n")
        
        try:
            total = len(self.manager.lyrics)
            
            for i, lyric in enumerate(self.manager.lyrics):
                if not self.is_playing:
                    break
                
                # Hiển thị progress đơn giản
                progress = f"[{i+1}/{total}]"
                print(f"{Colors.DIM}{progress}{Colors.RESET}", end=" ")
                
                # Lấy màu sắc
                color = getattr(Colors, lyric.get('color', 'WHITE'), Colors.WHITE)
                
                # Hiệu ứng typewriter đơn giản nhưng đẹp
                text = lyric['text']
                print(f"{color}", end="")
                
                for char in text:
                    print(char, end='', flush=True)
                    time.sleep(lyric['speed'])
                
                print(f"{Colors.RESET}")
                print()  # Dòng trống
                
                # Nghỉ giữa các câu
                time.sleep(lyric['delay'])
            
            print(f"{Colors.GREEN}{'─' * 30}{Colors.RESET}")
            print(f"{Colors.GREEN}    Hoàn thành! {Colors.RESET}")
            print(f"{Colors.GREEN}{'─' * 30}{Colors.RESET}")
            
        except KeyboardInterrupt:
            print(f"\n{Colors.YELLOW}Đã dừng phát!{Colors.RESET}")
        
        self.is_playing = False
        input(f"\n{Colors.DIM}Nhấn Enter để quay lại menu...{Colors.RESET}")
    
    def add_lyric_interactive(self):
        """Thêm lời bài hát với giao diện đẹp"""
        AdvancedEffects.clear_screen()
        
        header = AdvancedEffects.create_border("➕ THÊM LỜI BÀI HÁT MỚI", color=Colors.GREEN)
        print(header)
        print()
        
        try:
            # Nhập text
            print(f"{Colors.YELLOW}📝 Nhập lời bài hát:{Colors.RESET}")
            text = input(f"{Colors.CYAN}> {Colors.RESET}")
            
            if not text.strip():
                print(f"{Colors.RED}❌ Không thể để trống!{Colors.RESET}")
                return
            
            # Nhập delay
            print(f"\n{Colors.YELLOW}⏱️  Thời gian nghỉ sau câu này (giây):{Colors.RESET}")
            delay = float(input(f"{Colors.CYAN}> {Colors.RESET}") or "2.0")
            
            # Nhập speed
            print(f"\n{Colors.YELLOW}⚡ Tốc độ hiển thị (0.05=nhanh, 0.2=chậm):{Colors.RESET}")
            speed = float(input(f"{Colors.CYAN}> {Colors.RESET}") or "0.08")
            
            # Chọn màu
            colors = ["WHITE", "RED", "GREEN", "YELLOW", "BLUE", "MAGENTA", "CYAN"]
            print(f"\n{Colors.YELLOW}🎨 Chọn màu sắc:{Colors.RESET}")
            for i, color in enumerate(colors, 1):
                color_code = getattr(Colors, color)
                print(f"  {i}. {color_code}{color}{Colors.RESET}")
            
            color_choice = input(f"{Colors.CYAN}> Chọn số (1-{len(colors)}) hoặc Enter cho mặc định: {Colors.RESET}")
            
            if color_choice.isdigit() and 1 <= int(color_choice) <= len(colors):
                color = colors[int(color_choice) - 1]
            else:
                color = "WHITE"
            
            # Thêm vào danh sách
            self.manager.add_lyric(text, delay, speed, color)
            
            print(f"\n{Colors.GREEN}✅ Đã thêm thành công!{Colors.RESET}")
            
            # Preview
            print(f"\n{Colors.CYAN}🔍 Preview:{Colors.RESET}")
            color_code = getattr(Colors, color)
            Effects.typewriter_with_sparks(f"{color_code}{text}{Colors.RESET}", speed)
            
            AudioEffects.play_sound_effect("complete")
            
        except ValueError:
            print(f"{Colors.RED}❌ Lỗi: Vui lòng nhập số hợp lệ!{Colors.RESET}")
            AudioEffects.play_sound_effect("error")
        except Exception as e:
            print(f"{Colors.RED}❌ Lỗi: {e}{Colors.RESET}")
            AudioEffects.play_sound_effect("error")
        
        input(f"\n{Colors.CYAN}Nhấn Enter để quay lại menu...{Colors.RESET}")
    
    def show_lyrics_list(self):
        """Hiển thị danh sách với hiệu ứng đẹp"""
        AdvancedEffects.clear_screen()
        
        header = AdvancedEffects.create_border("📋 DANH SÁCH LỜI BÀI HÁT", color=Colors.BLUE)
        print(header)
        print()
        
        if not self.manager.lyrics:
            print(f"{Colors.RED}❌ Chưa có lời bài hát nào!{Colors.RESET}")
        else:
            for i, lyric in enumerate(self.manager.lyrics, 1):
                color_code = getattr(Colors, lyric.get('color', 'WHITE'), Colors.WHITE)
                
                # Hiển thị với số thứ tự và màu sắc
                print(f"{Colors.CYAN}{i:2d}.{Colors.RESET} {color_code}{lyric['text']}{Colors.RESET}")
                print(f"    {Colors.DIM}⏱️  {lyric['delay']}s | ⚡ {lyric['speed']}s/char | 🎨 {lyric.get('color', 'WHITE')}{Colors.RESET}")
                print()
        
        print(f"{Colors.YELLOW}📊 Tổng cộng: {len(self.manager.lyrics)} câu hát{Colors.RESET}")
        input(f"\n{Colors.CYAN}Nhấn Enter để quay lại menu...{Colors.RESET}")
    
    def demo_effects(self):
        """Demo các hiệu ứng đặc biệt"""
        AdvancedEffects.clear_screen()
        
        effects_demo = [
            ("🌈 Rainbow Text", lambda: print(Effects.rainbow_text("Đây là hiệu ứng Rainbow Text tuyệt đẹp!"))),
            ("✨ Glow Effect", lambda: print(Effects.glow_effect("Text này đang phát sáng!", Colors.CYAN))),
            ("🌊 Wave Animation", lambda: AdvancedEffects.animate_text_wave("Hiệu ứng sóng cực kỳ mượt mà!")),
            ("💫 Typewriter + Sparks", lambda: Effects.typewriter_with_sparks("Đánh máy với tia lửa lung linh!")),
            ("🎭 Matrix Rain", lambda: AdvancedEffects.matrix_rain(2)),
        ]
        
        header = AdvancedEffects.create_border("🎨 DEMO HIỆU ỨNG ĐẶC BIỆT", color=Colors.MAGENTA)
        print(header)
        print()
        
        for name, effect_func in effects_demo:
            print(f"{Colors.YELLOW}Đang demo: {name}{Colors.RESET}")
            print("-" * 50)
            effect_func()
            print("\n")
            time.sleep(1)
        
        print(f"{Colors.GREEN}🎉 Demo hoàn thành!{Colors.RESET}")
        input(f"\n{Colors.CYAN}Nhấn Enter để quay lại menu...{Colors.RESET}")
    
    def run(self):
        """Chạy chương trình chính"""
        self.show_welcome_screen()
        
        while True:
            self.show_menu()
            
            choice = input(f"{Colors.CYAN}Lựa chọn: {Colors.RESET}")
            
            if choice == "1":
                self.display_lyrics_with_effects()
            elif choice == "2":
                self.add_lyric_interactive()
            elif choice == "3":
                self.show_lyrics_list()
            elif choice == "4":
                print(f"{Colors.YELLOW}Tính năng cài đặt đang phát triển...{Colors.RESET}")
                time.sleep(1)
            elif choice == "0":
                AdvancedEffects.clear_screen()
                print(f"\n{Colors.CYAN}    Cảm ơn bạn đã sử dụng Lyrics Player!{Colors.RESET}")
                print(f"{Colors.DIM}    Hẹn gặp lại! {Colors.RESET}\n")
                break
            else:
                print(f"{Colors.RED}Lựa chọn không hợp lệ! Vui lòng chọn 0-4.{Colors.RESET}")
                time.sleep(1)

if __name__ == "__main__":
    try:
        player = UltraLyricsPlayer()
        player.run()
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}👋 Đã thoát chương trình!{Colors.RESET}")
    except Exception as e:
        print(f"\n{Colors.RED}❌ Lỗi: {e}{Colors.RESET}")