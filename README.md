# 📧 垃圾郵件分類系統 (Spam Email Classification)

本專案開發了一個智能垃圾郵件分類系統，基於機器學習技術，能夠自動判斷郵件或文本是否為垃圾訊息。專案採用 OpenSpec 開發流程，整合了完整的機器學習管線，並提供友善的 Web 使用介面。

## 🌟 主要特色

- 採用 OpenSpec 工作流程進行開發
- 完整的機器學習訓練流程
- 直觀的 Streamlit 互動介面
- 詳細的模型評估與視覺化
- 支援即時文本分類

## 📁 專案結構

```
5114056012_HW3/
├── app/
│   └── app.py                    # Streamlit 應用程式
├── data/
│   └── sms_spam_no_header.csv    # 訓練資料集
├── models/                       # 預訓練模型存放
│   ├── spam_model.pkl
│   ├── nb_model.pkl
│   └── vectorizer.pkl
├── notebooks/                    # Jupyter 筆記本
│   └── spam_email_analysis.ipynb
├── openspec/                     # OpenSpec 文件
│   ├── project.md
│   ├── AGENTS.md
│   └── changes/
├── src/                         # 核心程式碼
│   ├── data/
│   ├── models/
│   └── visualization/
├── tests/                       # 單元測試
└── requirements.txt            # 相依套件

## 🚀 快速開始

### 環境要求
- Python 3.8+
- Git
- pip 或 conda

### 安裝步驟

1. Clone 專案到本地：
```bash
git clone https://github.com/AntingZ21709/5114056012_HW3.git
cd 5114056012_HW3
```

2. 建立虛擬環境：
```bash
python -m venv venv
.\venv\Scripts\activate  # Windows
# 或
source venv/bin/activate  # Linux/Mac
```

3. 安裝相依套件：
```bash
pip install -r requirements.txt
```

## 💻 使用指南

### 訓練模型
```bash
python src/models/training.py
```

### 啟動 Web 介面
```bash
streamlit run app/app.py
```

## 🌐 線上 Demo

本專案已部署至 Streamlit Cloud，您可以直接體驗：

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://5114056012hw3.streamlit.app)

> 詳細部署文件請參考 [DEPLOYMENT.md](DEPLOYMENT.md)

## 📋 主要模組說明

### Data Processing (`src/data/preprocessing.py`)
- 資料載入與清理
- 文本預處理（移除標點、轉小寫等）
- TF-IDF 特徵向量化
- 資料集分割

### Model Training (`src/models/training.py`)
- 支援多種分類器：
  - Naive Bayes
  - Logistic Regression
- 模型訓練與評估
- 模型序列化與保存

### Visualization (`src/visualization/visualization.py`)
- 混淆矩陣視覺化
- 性能指標圖表
- 學習曲線分析

### Web Interface (`app/app.py`)
- 文本輸入介面
- 即時預測結果顯示
- 預測信心度展示
- 整體模型性能視覺化

## 📊 模型評估結果

| 模型                | 準確率 | 精確率 | 召回率 | F1分數 |
|-------------------|--------|--------|--------|--------|
| Naive Bayes       | 0.9704 | 1.0000 | 0.7950 | 0.8858 |
| Logistic Regression| 0.9543 | 0.9825 | 0.6957 | 0.8145 |

> 註：實際結果可能因資料集分割或隨機種子而略有不同。完整評估報告請見 Streamlit 介面。

## 🛠️ 開發方法論

本專案採用 OpenSpec 工作流程開發，完整文件位於 `openspec/` 目錄：

- `project.md`：專案規格書
- `AGENTS.md`：開發規範
- `changes/`：功能改動提案
  - 資料預處理
  - 模型訓練
  - 視覺化
  - Streamlit UI

## 👥 作者與授權

- **作者：** 鄭安婷 (5114056012)
- **授權：** MIT License

## 📫 聯絡方式

- GitHub: [@AntingZ21709](https://github.com/AntingZ21709)
- Email: anting@smail.nchu.edu.tw

## 🙏 致謝

- 感謝課程教師與助教的指導
- [Hands-On AI for Cybersecurity](https://github.com/PacktPublishing/Hands-On-Artificial-Intelligence-for-Cybersecurity)
- SMS Spam Collection Dataset
