## ADDED Requirements
### Requirement: Model Training Module
系統 SHALL 提供一個模型訓練模組，能夠以 Naive Bayes 與 Logistic Regression 進行垃圾郵件分類模型訓練，並評估其效能。

#### Scenario: 資料集切分
- **WHEN** 載入前處理後的特徵矩陣與標籤
- **THEN** 將資料集切分為訓練集與測試集（如 8:2）

#### Scenario: 訓練與儲存模型
- **WHEN** 執行模型訓練
- **THEN** 完成 Naive Bayes 與 Logistic Regression 訓練，並將模型儲存至檔案

#### Scenario: 模型評估
- **WHEN** 訓練完成後於測試集評估
- **THEN** 輸出 accuracy、precision、recall、F1-score 等指標
