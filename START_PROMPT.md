# 建議啟動提示詞

## 一般遊戲專案

請先讀取 `router` 與 `game-production-director` 技能，辨識本專案引擎、目前版本、權威需求文件與交接狀態，再只載入本次工作需要的最少技能。先確認 current implementation / target design / historical docs 的差異，完成後執行適當驗證並更新 handoff；未實機、未真人聽感、未視覺驗收的部分不要宣稱已完成。

## 《星之破曉》

請先讀取 `router`、`game-production-director`、`star-dawn-survivors-production`，然後依序讀專案 `AGENTS.md`、`CODEX_HANDOFF.md`、目前產品優先 backlog，以及本次功能對應的需求書。維持單一 Survivor 戰鬥引擎、Profile/Run 分離、Web/Android/Godot 實作邊界與既有存檔相容；只做目前優先項，完成後跑相關測試並更新 `CODEX_HANDOFF.md`。

## 遊戲配樂

請使用 `router`、`game-production-director`、`audio-design`、引擎音訊技能與 `game-music-production`。先盤點現有曲目與場景需求，再決定是否需要生成新曲；避免浪費生成額度，保留 provider ID / metadata / SHA-256，完成 runtime 接線、生命週期驗證與真人聽感待驗項目紀錄。

## 過場動畫 / AI 影片

請使用 `router`、`game-production-director`、`create-game-assets`、`game-cinematic-production`。先鎖定角色 bible 與 canonical reference，再分鏡；保留 job/seed/reference/hash，runtime 必須有 ended/skip/error/timeout 單次續行與背景暫停，回放模式不得重複發獎勵。
