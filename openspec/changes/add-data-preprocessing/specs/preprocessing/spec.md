## ADDED Requirements
### Requirement: Data Preprocessing Module
系統 SHALL 提供一個資料前處理模組，能夠載入 `sms_spam_no_header.csv`，並完成資料清理、斷詞與 TF-IDF 特徵向量化。

#### Scenario: 成功載入並清理資料
- **WHEN** 使用者呼叫前處理模組載入資料集
- **THEN** 回傳已去除標點、轉小寫、去除多餘空白的純文字與標籤

#### Scenario: 文字斷詞與向量化
- **WHEN** 前處理模組處理純文字資料
- **THEN** 回傳經過斷詞與 TF-IDF 向量化的特徵矩陣（X）與標籤（y）

#### Scenario: 輸出格式正確
- **WHEN** 前處理完成
- **THEN** 輸出 X 為數值特徵矩陣，y 為標籤陣列，且可直接用於模型訓練
