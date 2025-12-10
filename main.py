import os
import discord
from discord.ext import commands
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from dotenv import load_dotenv

# .envから環境変数を読み込む
load_dotenv()

# Botのトークンを環境変数から取得
TOKEN = os.getenv("DISCORD_TOKEN")

# Botのプレフィックス
bot = commands.Bot(command_prefix='/', intents=discord.Intents.default())

# 履歴を保存するリスト
history = []

# Google Sheets認証設定
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

try:
    creds = ServiceAccountCredentials.from_json_keyfile_name("service_account.json", scope)
    client = gspread.authorize(creds)
    sheet = client.open("DiscordBotHistory").sheet1
except Exception as e:
    print(f"Google Sheets認証に失敗しました: {e}")
    sheet = None

@bot.event
async def on_ready():
    print(f'ログインしました: {bot.user.name}')

@bot.command()
async def record(ctx, *, content: str):
    """履歴を記録し、Google Sheetsにも保存"""
    history.append(content)
    if sheet:
        try:
            sheet.append_row([content])
        except Exception as e:
            await ctx.send(f"Google Sheetsへの保存に失敗しました: {e}")
            return
    await ctx.send(f'記録しました: {content}')

@commands.has_permissions(administrator=True)
@bot.command()
async def reset(ctx):
    """履歴をリセット（管理者のみ実行可能）"""
    history.clear()
    if sheet:
        try:
            sheet.clear()
            sheet.append_row(["履歴"])
        except Exception as e:
            await ctx.send(f"Google Sheetsのリセットに失敗しました: {e}")
            return
    await ctx.send('履歴をリセットしました。')

@bot.command()
async def show(ctx):
    """履歴を表示"""
    if history:
        await ctx.send('\n'.join(history))
    else:
        await ctx.send('履歴は空です。')

# Botの起動
if TOKEN:
    bot.run(TOKEN)
else:
    print("DISCORD_TOKENが設定されていません。.envを確認してください。")
