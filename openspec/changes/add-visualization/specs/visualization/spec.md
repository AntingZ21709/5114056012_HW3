## ADDED Requirements
### Requirement: Visualization and Interpretability Module
系統 SHALL 提供一個可視化模組，能夠展示模型評估結果、混淆矩陣與各項指標，提升模型可解釋性。

#### Scenario: 混淆矩陣圖形化
- **WHEN** 使用者檢視模型評估結果
- **THEN** 顯示混淆矩陣圖表

#### Scenario: 指標摘要與圖表
- **WHEN** 模型評估完成
- **THEN** 呈現準確率、精確率、召回率、F1-score 等指標的表格或長條圖

#### Scenario: Streamlit 前端互動
- **WHEN** 使用者於 Web 介面操作
- **THEN** 可於 Streamlit 前端互動檢視所有評估圖表與指標
