// Hiệu ứng gõ chữ
const textElement = document.getElementById("typing-text");
const content = "Xin chào! Tôi là Nguyễn Quang Phúc.";
let index = 0;

function typeText() {
  if (index < content.length) {
    textElement.innerHTML += content.charAt(index);
    index++;
    setTimeout(typeText, 100);
  }
}
typeText();

// Chuyển chế độ sáng/tối
document.getElementById("toggle-theme").addEventListener("click", () => {
  document.body.classList.toggle("dark");
});
