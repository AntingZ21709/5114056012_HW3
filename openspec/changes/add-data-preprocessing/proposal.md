## Why

目前專案缺乏標準化的資料前處理流程。為確保垃圾郵件分類模型的準確性與可重現性，需建立一個專責的 data preprocessing 模組，統一處理資料清理、斷詞、特徵向量化等步驟。

## What Changes
- 新增 `preprocessing` 模組，負責載入並清理 `sms_spam_no_header.csv` 資料集
- 實作文字清理（去除標點、轉小寫、去除多餘空白等）
- 斷詞（tokenization）
- TF-IDF 特徵向量化
- 模組輸出乾淨且可供模型訓練的特徵矩陣與標籤

## Impact
- 影響 specs: preprocessing
- 影響 code: src/preprocessing.py（或同等模組檔案）