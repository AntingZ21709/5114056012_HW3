## Why

為了讓使用者能直觀了解模型效能與預測結果，需提供可視化模組，展示混淆矩陣、各項評估指標與圖表，提升模型可解釋性。

## What Changes
- 新增 visualization 模組，顯示模型評估圖表
- 呈現混淆矩陣、準確率、精確率、召回率、F1-score 等指標
- 支援圖形化展示（如長條圖、表格）

## Impact
- 影響 specs: visualization
- 影響 code: src/visualization.py（或同等模組檔案）