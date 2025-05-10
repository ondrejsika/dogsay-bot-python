import os
import subprocess

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

async def chatid_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = ' '.join(context.args) or 'woof'
    output = subprocess.run(["dogsay", text], capture_output=True, text=True).stdout
    await update.message.reply_markdown(f'```\n{output}\n```')

if __name__ == '__main__':
    if BOT_TOKEN is None:
        raise ValueError("Please set the TELEGRAM_BOT_TOKEN environment variable.")

    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler('dogsay', chatid_command))
    app.run_polling()
