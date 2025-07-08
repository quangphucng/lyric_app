# 🎵 Lyrics Terminal Player

> *Trình phát lời bài hát với hiệu ứng typewriter đẹp mắt trong terminal*

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Author](https://img.shields.io/badge/Author-quangphucng-orange.svg)](https://github.com/quangphucng)

## 📸 Demo

```
🎵 Karaoke Terminal - Typewriter Effect 🎵

Vì từ đầu anh có gì đâu

Ngoài những niềm đau là thiên mệnh

Anh đã có mọi thứ anh mong

🎶 Kết thúc! 🎶
```

## ✨ Tính năng

- 🖥️ **Terminal-based**: Chạy trực tiếp trong command line
- ⌨️ **Typewriter Effect**: Hiệu ứng đánh máy từng ký tự
- ⏱️ **Timing Control**: Tùy chỉnh tốc độ hiển thị và thời gian nghỉ
- 🎨 **Clean Interface**: Giao diện terminal sạch sẽ và đẹp mắt
- 🔧 **Customizable**: Dễ dàng thay đổi lời bài hát và cài đặt

## 🚀 Cài đặt và Sử dụng

### Yêu cầu hệ thống
- Python 3.6 trở lên

### Cách chạy

#### 1. Clone repository
```bash
git clone https://github.com/quangphucng/lyrics-terminal-player.git
cd lyrics-terminal-player
```

#### 2. Chạy chương trình
```bash
python lyrics_player.py
```

#### 3. Hoặc chạy với Python trực tiếp
```bash
python3 lyrics_player.py
```

## ⚙️ Tùy chỉnh

### Thay đổi lời bài hát
Chỉnh sửa mảng `lyrics` trong file `lyrics_player.py`:

```python
lyrics = [
    ("Câu lời đầu tiên", 1.5),    # (text, delay_seconds)
    ("Câu lời thứ hai", 2.0),
    ("Câu lời cuối", 1.0)
]
```

### Điều chỉnh tốc độ hiển thị

```python
# Chậm và dramatic
karaoke_terminal(lyrics, typing_speed=0.1)

# Nhanh và mượt mà
karaoke_terminal(lyrics, typing_speed=0.03)

# Siêu chậm như máy đánh chữ cổ
karaoke_terminal(lyrics, typing_speed=0.15)
```

## 📁 Cấu trúc Project

```
lyrics-terminal-player/
├── lyrics_player.py    # File chính
├── README.md          # Tài liệu này
└── LICENSE           # Giấy phép MIT
```

## 🔧 API Reference

### `typewriter_effect(text, typing_speed=0.05)`
Hiệu ứng đánh máy cho một đoạn text

**Parameters:**
- `text` (str): Văn bản cần hiển thị
- `typing_speed` (float): Thời gian delay giữa mỗi ký tự (giây)

**Returns:**
- None

### `karaoke_terminal(lyrics, typing_speed=0.05)`
Chạy karaoke với hiệu ứng typewriter cho toàn bộ danh sách lời

**Parameters:**
- `lyrics` (list): Danh sách tuple [(text, delay), ...]
- `typing_speed` (float): Tốc độ gõ cho mỗi ký tự

**Returns:**
- None

## 🎯 Ví dụ sử dụng

### Ví dụ cơ bản
```python
from lyrics_player import karaoke_terminal

my_lyrics = [
    ("Hello World", 1.0),
    ("Xin chào Python", 2.0),
    ("Goodbye!", 1.5)
]

karaoke_terminal(my_lyrics)
```

### Ví dụ với tùy chỉnh tốc độ
```python
# Hiệu ứng chậm và trang trọng
karaoke_terminal(my_lyrics, typing_speed=0.1)

# Hiệu ứng nhanh và năng động
karaoke_terminal(my_lyrics, typing_speed=0.03)
```

## 🎨 Screenshots

### Terminal trên Windows
```
C:\> python lyrics_player.py
🎵 Karaoke Terminal - Typewriter Effect 🎵

Vì từ đầu anh có gì đâu
```

### Terminal trên Linux/Mac
```
$ python3 lyrics_player.py
🎵 Karaoke Terminal - Typewriter Effect 🎵

Vì từ đầu anh có gì đâu
```

## 🛠️ Phát triển

### Thêm tính năng mới
1. Fork repository này
2. Tạo branch mới: `git checkout -b feature/amazing-feature`
3. Commit changes: `git commit -m 'Add amazing feature'`
4. Push to branch: `git push origin feature/amazing-feature`
5. Tạo Pull Request

### Báo lỗi
Nếu gặp lỗi, vui lòng tạo [issue mới](https://github.com/quangphucng/lyrics-terminal-player/issues)

## 📊 Roadmap

- [ ] 🎨 Thêm màu sắc cho text
- [ ] 🎵 Hỗ trợ phát nhạc nền
- [ ] 📱 GUI version với tkinter
- [ ] 🌐 Web version với Flask
- [ ] 📁 Import lời từ file .txt/.json
- [ ] ⏯️ Tạm dừng/tiếp tục
- [ ] 📊 Progress bar hiển thị tiến độ

## 🤝 Contributing

Contributions are welcome! Vui lòng đọc [CONTRIBUTING.md](CONTRIBUTING.md) để biết thêm chi tiết.

### Contributors
- **[@quangphucng](https://github.com/quangphucng)** - *Initial work* - Creator

## 📄 License

Project này được phân phối dưới giấy phép MIT. Xem file [LICENSE](LICENSE) để biết thêm chi tiết.

## 📞 Liên hệ

- **Author**: quangphucng
- **GitHub**: [@quangphucng](https://github.com/quangphucng)
- **Email**: your-email@example.com

## 🙏 Acknowledgments

- Cảm ơn Python community
- Inspired bởi terminal-based applications
- Special thanks cho những ai đóng góp feedback

## 📈 Stats

![GitHub stars](https://img.shields.io/github/stars/quangphucng/lyrics-terminal-player?style=social)
![GitHub forks](https://img.shields.io/github/forks/quangphucng/lyrics-terminal-player?style=social)
![GitHub issues](https://img.shields.io/github/issues/quangphucng/lyrics-terminal-player)

---

### 🎵 *"Code is poetry, make it beautiful"* 🎵

**Made with ❤️ by [quangphucng](https://github.com/quangphucng)**

*Created: 07.08.25 16h40*