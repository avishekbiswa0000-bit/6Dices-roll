# async_bot.py
import os
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.environ["BOT_TOKEN"]

async def roll(update: Update, context: ContextTypes.DEFAULT_TYPE):
    dice = [str(random.randint(1, 6)) for _ in range(6)]
    await update.message.reply_text("🎲 You rolled: " + " ".join(dice))

async def healthcheck(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("OK")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("roll", roll))
    app.add_handler(CommandHandler("health", healthcheck))
    # Start webhook
    port = int(os.environ.get("PORT", "10000"))
    app.run_webhook(
        listen="0.0.0.0",
        port=port,
        url_path=TOKEN,
        webhook_url=f"https://YOUR-APP-NAME.onrender.com/{TOKEN}"
    )

if __name__ == "__main__":
    main()