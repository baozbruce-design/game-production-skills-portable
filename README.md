# 遊戲製作技能包（Codex / Claude 可攜版）

這個資料夾把目前 OpenChatX 使用的 `Game Development Skills` 匯出成標準 `SKILL.md` 資料夾，並加入我們在《星之破曉》實作過程累積的製作層技能。

## 內容

`skills/` 內每個子資料夾都是一個可攜技能，核心包含：

- `router`：遊戲開發總路由，先辨識 Godot / Unity / Unreal / Web / Roblox 等引擎，再選最少必要技能。
- Godot / Unity / Unreal / Phaser / PixiJS / three.js / Roblox 等引擎技能。
- AI、存檔、UI/UX、輸入、物理、效能、關卡、音效、遊戲手感、Shader、程序生成等通用技能。
- 2D 素材 Forge：角色、Sprite、地圖、影片轉 Sprite、媒體生成路由。
- 類型技能：RPG、Roguelike、Platformer、Puzzle、Tower Defense、Visual Novel 等。
- 發布/原型流程：快速原型、Game Jam、Steam、itch.io。

另外新增 4 個我們自己的技能：

- `game-production-director`：需求優先序、階段開發、跨 Agent 交接、驗收證據、封裝與風險界線。
- `game-music-production`：Suno/AI 配樂、場景配樂映射、下載匯入、hash、loop、背景/前景生命週期與真人聽感驗收。
- `game-cinematic-production`：角色一致性、AI 動畫/過場、參考圖、job/seed/hash、直式手機、skip/error/timeout 與回放安全。
- `star-dawn-survivors-production`：《星之破曉》專案專用 overlay，保存單一 Survivor 戰鬥引擎、Web/Android/Godot 邊界、存檔與交接規則。

## Codex 安裝

Codex 的預設使用者技能目錄為（可用 `-TargetPath` 指定其他目錄）：

`%USERPROFILE%\.codex\skills`

Windows 建議直接執行：

```bat
install-codex.cmd
```

這個 `.cmd` 只會用單次 `ExecutionPolicy Bypass` 啟動本包的 PowerShell 安裝程式，不會修改系統全域執行原則。

預設不覆蓋同名技能。要更新既有技能：

```bat
install-codex.cmd -Force
```

安裝後重新開 Codex 工作階段，對遊戲專案可先要求：

> 先使用 `router` 與 `game-production-director` 判斷需要載入哪些技能；如果是《星之破曉》，再載入 `star-dawn-survivors-production`，然後依專案 AGENTS.md / handoff / backlog 繼續。

## Claude Code 安裝

Claude Code 可使用標準 `SKILL.md` 技能資料夾。全域使用：

```bat
install-claude.cmd
```

會安裝到：

`%USERPROFILE%\.claude\skills`

若只要放進單一專案：

```bat
install-claude.cmd -ProjectPath "D:\path\to\your-game"
```

會複製到該專案的 `.claude\skills`。

## 建議使用方式

不要一次把 80+ 個技能全部塞進模型上下文。讓 Agent 先讀 `router` 的描述，再依任務只載入：

1. 一組引擎技能；
2. 一到數個通用 discipline；
3. 必要時一個 genre/workflow；
4. `game-production-director`；
5. 《星之破曉》工作再加 `star-dawn-survivors-production`。

例如 Godot 遊戲配樂：

`router → game-production-director → audio-design → godot-audio → game-music-production`

例如《星之破曉》手機過場動畫：

`router → game-production-director → star-dawn-survivors-production → create-game-assets → game-cinematic-production`

## 驗證與更新

`MANIFEST-SHA256.txt` 記錄此技能包內檔案的 SHA-256。重新打包時可再次產生 manifest，避免不同 Agent 使用到不同版本。

## 來源與使用範圍

技能來源與授權分別列於 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)：通用遊戲技能來自 awesome-gamedev-agent-skills（Apache-2.0），Sprite Forge 技能採 MIT；四個製作層新增技能與本 repository 整理工具採 MIT。本 repository 是整合與可攜化版本，保留原來源與作者聲明。


## Repository 與版本

- [完整技能目錄](docs/CATALOG.md)
- [版本紀錄](CHANGELOG.md)
- [來源與授權](THIRD_PARTY_NOTICES.md)

先驗證檔案：

```powershell
python scripts/validate_package.py
```

此版本為 `1.0.1`，以提供的 `1.0.0` ZIP 為基底，修正可攜路徑並補上 repository 文件與驗證。來源 ZIP SHA-256：`809EFFD8CE1AA165AAD64C2A5C85B9B7B1B14357EDDA3994F7A1B7B9162B10F1`。

技能安裝不會自動安裝 Godot、Unity、FFmpeg、Python 套件，或代為授權第三方服務；依實際工作使用各技能的能力檢查。
