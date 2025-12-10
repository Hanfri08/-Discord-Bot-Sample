# 🤖 Discord Bot Sample

Pythonで開発したDiscord Botの学習用リポジトリです。  
履歴管理やGoogle Sheets連携を通じて、Bot開発の基礎を学習しています。

---

## 🔧 主な機能
- 履歴管理（/record, /show）
- リセット機能（/reset）
- Google Sheets連携（履歴をクラウド保存）

---

## 🛠 使用技術
- Python 3.x
- discord.py
- gspread
- dotenv（環境変数管理）

---

## 🚀 使い方
1. リポジトリをクローン

   ```bash
   git clone https://github.com/ユーザー名/Discord-Bot-Sample.git
   cd Discord-Bot-Sample
   ```
   
2.  必要なライブラリをインストール
```bash
   pip install -r requirements.txt
```

3. .envにBotトークンを設定
```env 
DISCORD_TOKEN=あなたのBotトークン
```

4.  Google Cloudで発行した service_account.json を配置
5.  Botを起動

```bash
python main.py
```
