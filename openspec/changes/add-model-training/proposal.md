## Why

為了讓垃圾郵件分類系統具備實際預測能力，需建立標準化的模型訓練流程，並支援多種常用分類器。

## What Changes
- 新增 model training 模組，支援 Naive Bayes 與 Logistic Regression
- 實作資料集切分（訓練/測試）
- 訓練模型並儲存
- 評估模型（準確率、精確率、召回率、F1-score）

## Impact
- 影響 specs: training
- 影響 code: src/training.py（或同等模組檔案）