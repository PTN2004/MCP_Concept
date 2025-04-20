# 🚀 MCP GitHub Repo Manager

Đây là một ứng dụng **MCP Server** đơn giản dùng để quản lý các repository trên GitHub thông qua giao diện API. Ứng dụng được xây dựng bằng Python, sử dụng [MCP SDK](https://docs.anthropic.com/claude/mcp), `requests` và `python-dotenv`.

## 🧠 MCP là gì?

**MCP (Model Context Protocol)** là một chuẩn giao tiếp giúp các công cụ (tools) bên ngoài có thể được mô hình ngôn ngữ (LLM) gọi trực tiếp. Điều này giúp mô hình hoạt động như một "agent" có khả năng thực thi hành động trong thế giới thật.

> Với MCP, LLM không chỉ trò chuyện mà còn có thể hành động như "liệt kê repo", "xóa repo" hay "cập nhật thông tin repo" trên GitHub – một cách bảo mật và có kiểm soát.

---

## 🧰 Tính năng

| Chức năng         | Mô tả                                                                 |
|-------------------|----------------------------------------------------------------------|
| `list_repos`      | Liệt kê tất cả repository của người dùng                             |
| `create_repo`     | Tạo repository mới                                                    |
| `update_repo`     | Cập nhật mô tả hoặc trạng thái riêng tư cho repository                |
| `delete_repo`     | Xóa repository                                                       |

---

## 🛠️ Cài đặt & chạy server

### 1. Cài đặt thư viện

```bash
pip install -r requirements.txt
2. Tạo file .env với nội dung:
env
Sao chép
Chỉnh sửa
GITHUB_TOKEN=your_github_personal_access_token
MCP_PORT=8000
Bạn có thể tạo GitHub token tại: https://github.com/settings/tokens

3. Chạy MCP Server
bash
Sao chép
Chỉnh sửa
python mcp_server.py
Kết quả:

arduino
Sao chép
Chỉnh sửa
🚀 MCP Server GitHub đang chạy trên cổng 8000
📁 Cấu trúc thư mục
css
Sao chép
Chỉnh sửa
📦 mcp-github-manager
 ┣ 📄 mcp_server.py         # Tập tin khởi tạo MCP Server và định nghĩa các tool
 ┣ 📄 .env                  # Chứa token GitHub và port (không nên commit file này)
 ┣ 📄 requirements.txt      # Thư viện cần thiết
 ┗ 📄 README.md             # File tài liệu (bạn đang đọc nó!)
🧪 Ví dụ gọi tool (curl)
bash
Sao chép
Chỉnh sửa
curl http://localhost:8000/tool/list_repos -X POST -H "Content-Type: application/json" -d '{}'
🔐 Lưu ý bảo mật
KHÔNG commit file .env lên GitHub.

Token GitHub nên cấp quyền phù hợp với nhu cầu sử dụng: repo, delete_repo v.v.

📜 License
MIT License. Dùng thoải mái cho học tập và cá nhân.