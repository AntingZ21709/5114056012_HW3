## ADDED Requirements
### Requirement: Streamlit UI for Real-Time Prediction
系統 SHALL 提供一個 Streamlit 前端介面，讓使用者可輸入郵件內容並即時獲得垃圾郵件預測結果。

#### Scenario: 頁面佈局與說明
- **WHEN** 使用者開啟 UI
- **THEN** 顯示標題、簡要說明、輸入區與預測結果區

#### Scenario: 文字輸入與預測
- **WHEN** 使用者輸入郵件內容並按下預測按鈕
- **THEN** 介面即時顯示 spam/not-spam 預測結果

#### Scenario: 串接模型推論
- **WHEN** 使用者送出輸入內容
- **THEN** 系統自動進行前處理並呼叫已訓練模型進行預測，回傳結果於 UI 顯示
