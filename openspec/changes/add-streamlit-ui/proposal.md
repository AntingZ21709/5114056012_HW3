## Why

為了讓使用者能方便地體驗垃圾郵件分類系統，需提供 Streamlit UI，支援即時文字輸入與預測結果顯示。

## What Changes
- 新增 Streamlit 前端介面，支援用戶輸入郵件內容
- 即時顯示 spam/not-spam 預測結果
- 介面包含輸入表單、預測按鈕、結果區塊
- 串接已訓練模型進行預測

## Impact
- 影響 specs: ui
- 影響 code: app.py 或 src/ui.py