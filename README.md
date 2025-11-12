# 📘 智能文档问答助手（RAG Web App）

一个基于 **Flask + OpenAI + ChromaDB** 的网页应用。  
用户可以上传文档（Word / PDF），系统自动提取文本、生成向量索引，并支持自然语言问答。  
输入你的问题，AI 将基于文档内容进行回答。

---

## 🚀 功能简介
- 🧩 **文档上传**：支持 `.docx`、`.pdf` 文件，自动存入向量数据库  
- 💬 **智能问答**：针对上传文档内容进行语义检索与回答  
- 🔄 **多文档切换**：支持选择不同文档进行问答  

---

## 📂 项目结构
```
智能文档问答助手/
├── doc-chat-assistant/
│ ├── chroma/ # 向量数据库
│ ├── templates/ # 网页
│ │ ├── chat.html # 聊天
│ │ └── document_upload.html # 上传
│ ├── uploads/ # 用户上传文档保存目录
│ ├── app.py # Flask 启动入口（运行此文件）
│ ├── main.py # RAG 检索与问答
├── models.py # 模型与向量接口封装
├── function_tools.py # 辅助函数
├──requirements.txt # 环境依赖
```

---

## ⚙️ 环境配置

```bash
# 1️⃣ 创建虚拟环境
python -m venv .venv
.\.venv\Scripts\activate   # Windows

# 2️⃣ 安装依赖
pip install -r requirements.txt
```
---
## ▶️ 运行方式
```dockerignore
# 启动 Flask 应用
python app.py
```
运行后在终端看到：
```angular2html
 * Running on http://127.0.0.1:5000/
```
浏览器打开 http://127.0.0.1:5000/ 即可使用：
1. 访问 /document_upload/ 上传文档
2. 回到 /chat/ 提问文档内容问题

---
## 💡 使用示例

上传一个名为 `人工智能简介.docx` 的文档后，可在聊天界面输入：

“这篇文档提到了哪些主要的AI应用领域？”

系统会自动从文档内容中检索相关信息并生成回答。