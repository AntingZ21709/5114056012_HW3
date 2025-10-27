# Project Context

## Purpose
本專案旨在建立一個 Email Spam Classification 系統，能夠自動判斷電子郵件是否為垃圾郵件。系統將協助用戶過濾垃圾郵件，提升郵件管理效率。

## Tech Stack
- Python 3.x
- scikit-learn（機器學習）
- pandas（資料處理）
- Streamlit（Web 應用介面）
- Jupyter Notebook（資料探索與原型設計）

## Data Source
資料集來源為 `sms_spam_no_header.csv`，內容包含簡訊文本及其標註（spam/ham）。

## Folder Structure
- openspec/：專案規格與說明文件
- sms_spam_no_header.csv：主要資料集
- [src/]：程式原始碼（如有）
- [notebooks/]：Jupyter 筆記本（如有）
- [app.py]：Streamlit 主程式（如有）

## Project Conventions

### Code Style
- 遵循 PEP8 Python 程式風格：
	- 每行不超過 79 字元。
	- 使用 4 個空白縮排。
	- 適當空行分隔類別、函式與邏輯區塊。
	- 避免多餘空白與行尾空白。
- 命名慣例：
	- 變數、函式名稱採用小寫加底線（snake_case）。
	- 類別名稱採用大駝峰式（CapWords）。
	- 常數名稱全大寫加底線（UPPER_CASE）。
- 註解與文件字串（docstring）完整，說明每個函式、類別與模組用途。

### Folder Organization
- openspec/：專案規格與說明文件
- sms_spam_no_header.csv：主要資料集
- src/：主要程式原始碼（如有）
- notebooks/：Jupyter 筆記本（如有）
- app.py：Streamlit 主程式（如有）


### Architecture Patterns
- 採用資料前處理、特徵工程、模型訓練、預測與 Web 介面分層設計。
- Streamlit 作為前端展示與互動。

### Testing Strategy
- 以 Jupyter Notebook 進行資料與模型驗證。
- 主要功能可撰寫 pytest 測試（如有）。
- 以混淆矩陣、準確率、召回率等指標評估模型。

### Git Workflow
- 使用 main 分支為穩定版。
- 功能開發以 feature/ 為前綴建立分支。
- Commit message 格式：
	- 以動詞開頭，簡潔描述本次變更內容。
	- 範例：
		- Add spam classifier training script
		- Fix data preprocessing bug
		- Refactor feature extraction logic

## Domain Context
垃圾郵件分類屬於自然語言處理（NLP）與二元分類問題，常見應用於郵件服務、簡訊過濾等。

## Important Constraints
- 僅使用開源 Python 套件。
- 資料集不得外洩，僅用於學術或個人專案。

## External Dependencies
- 需安裝 scikit-learn、pandas、streamlit 等 Python 套件。
- 無需連接外部 API。
