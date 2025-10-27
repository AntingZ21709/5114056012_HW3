# Email Spam Classification System

本專案為一個基於 Python、scikit-learn、pandas 與 Streamlit 的垃圾郵件分類系統，能自動判斷郵件是否為垃圾郵件，並提供互動式 Web 介面。

## 專案結構
- `openspec/`：專案規格與 OpenSpec 變更管理
- `sms_spam_no_header.csv`：主要資料集
- `src/`：主要程式原始碼（如 preprocessing.py、training.py、visualization.py）
- `notebooks/`：Jupyter 筆記本（資料探索與原型設計）
- `app.py`：Streamlit 主程式

## 安裝與環境建置
1. 建議使用 Python 3.8 以上版本。
2. 安裝必要套件：

```bash
pip install -r requirements.txt
# 或手動安裝
pip install scikit-learn pandas streamlit matplotlib
```

## 部署

詳細的部署說明請參考 [DEPLOYMENT.md](DEPLOYMENT.md)。

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app-name.streamlit.app)

## 執行 Streamlit Demo

```bash
streamlit run app.py
```

開啟瀏覽器後即可看到互動式垃圾郵件分類介面。

## 各模組簡介
- **preprocessing.py**：資料前處理，包含資料載入、文字清理、斷詞、TF-IDF 特徵向量化。
- **training.py**：模型訓練，支援 Naive Bayes 與 Logistic Regression，並進行資料切分、模型儲存與評估。
- **visualization.py**：模型評估結果可視化，包含混淆矩陣、各項指標圖表。
- **app.py**：Streamlit 前端，支援用戶輸入郵件內容並即時顯示 spam/not-spam 預測結果，並提供模型整體表現的視覺化圖表。

## 評估結果範例
| Model                | Accuracy | Precision | Recall | F1-score |
|----------------------|----------|-----------|--------|----------|
| Naive Bayes          | 0.9704   | 1.0000    | 0.7950 | 0.8858   |
| Logistic Regression  | 0.9543   | 0.9825    | 0.6957 | 0.8145   |

> *實際結果依資料集與隨機種子略有不同，詳細請見 `visualization.py` 或 Streamlit 介面。*

## 其他
- 僅使用開源 Python 套件，無需連接外部 API。
- 詳細規格與開發流程請參考 `openspec/` 目錄。
