# Tasks for Model Training

## 實作進度 (Status: 85% 完成)

### 模型開發
- [x] 1.1 建立 training 模組檔案 (src/models/training.py)
- [x] 1.2 實作多個分類器
  - [x] Logistic Regression
  - [x] Naive Bayes
  - [ ] Support Vector Machine (計劃中)
- [x] 1.3 模型訓練流程
  - [x] 載入預處理數據
  - [x] 模型擬合
  - [x] 模型保存

### 模型評估
- [x] 2.1 實作評估指標計算
  - [x] 準確率 (Accuracy)
  - [x] 精確率 (Precision)
  - [x] 召回率 (Recall)
  - [x] F1 分數
- [ ] 2.2 進階評估方法
  - [ ] 交叉驗證
  - [ ] ROC 曲線
  - [ ] 學習曲線

### 模型優化
- [ ] 3.1 超參數調整
  - [ ] 網格搜索
  - [ ] 隨機搜索
- [ ] 3.2 模型集成
  - [ ] Voting 分類器
  - [ ] Stacking

## 後續規劃
1. 實作更多分類器
2. 優化模型性能
3. 添加模型解釋功能
