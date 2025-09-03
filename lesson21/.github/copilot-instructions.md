# Copilot 指令（針對 lesson21）

## 專案概述
這是一個 Flask Web 應用專案.

## 環境設置
### Python 環境
- 使用 conda 環境：`data_analysis_1_3`
- Python 版本：3.12.11
- 執行前必須啟動環境：`conda activate data_analysis_1_3`

### 依賴套件
主要套件（詳見 `requirements.txt`）：
- Flask 3.0.2
- python-dotenv 1.0.1

## 專案架構
```
lesson21/
├── app.py              # Flask 應用主程式
├── requirements.txt    # 相依套件列表

```

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
- 資料庫相關的模型應定義在 `app.py` 中


