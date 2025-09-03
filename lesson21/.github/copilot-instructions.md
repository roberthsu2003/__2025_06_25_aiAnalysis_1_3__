# Copilot 指令（針對 lesson21）

## 專案概述
這是一個 Flask Web 應用專案，使用模板系統來渲染網頁內容。專案採用簡潔的 MVC 架構設計。

## 環境設置
### Python 環境
- 使用 conda 環境：`data_analysis_1_3`
- Python 版本：3.12.11
- 執行前必須啟動環境：`conda activate data_analysis_1_3`

### 依賴套件
主要套件（詳見 `requirements.txt`）：
- Flask 3.0.2：Web 框架
- python-dotenv 1.0.1：環境變數管理

## 專案架構
```
lesson21/
├── app.py              # Flask 應用主程式
├── templates/          # HTML 模板目錄
│   └── home.html      # 首頁模板
└── requirements.txt    # 相依套件列表
```

## 關鍵模式和慣例
### 模板設計
- 使用 `templates/` 目錄存放所有 HTML 模板
- HTML 模板採用 UTF-8 編碼，支援中文顯示
- 模板中包含內聯 CSS 樣式
- 使用響應式設計支援多種設備

### 路由規則
- 所有路由定義在 `app.py` 中
- 使用 Flask 的 `render_template()` 來渲染模板

## 開發工作流程
1. **環境準備**：
   ```bash
   conda activate data_analysis_1_3
   ```

2. **安裝依賴**：
   ```bash
   pip install -r requirements.txt
   ```

3. **執行應用**：
   ```bash
   python app.py
   ```

## 注意事項
- 開發模式已啟用（debug=True）
- 應用程式預設運行在 http://localhost:5000
- 使用 微軟正黑體 作為預設中文字體
- 採用響應式設計，最大內容寬度為 800px


