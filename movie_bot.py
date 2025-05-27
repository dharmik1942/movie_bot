from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = "8086018015:AAHyV7Lm363uNbPwvx7OdH9baVn98qqw-O8"  # ⚠️ Keep this private

MOVIE_LINKS = {
    "sikandar": "https://hdhub4u.frl/sikandar-2025-hindi-proper-webrip-full-movie/",
    "hit": "https://hdhub4u.frl/hit-the-third-case-2025-hindi-webrip-full-movie/",
}


# ─────────── Commands ───────────
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎬 Welcome to Movie Bot!\n"
        "Type a movie name to get the download link.\n"
        "Use /hello or /help for more."
    )

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello from Movie Bot! 🍿")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✅ Commands:\n"
        "/start – Welcome message\n"
        "/hello – Say hello\n"
        "/help – This help\n\n"
        "Or just type the movie name like: to get the link!",
        parse_mode="Markdown"
    )


# ─────────── Message Handler ───────────
async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text.strip().lower()

    for keyword, link in MOVIE_LINKS.items():
        if keyword in user_text:
            await update.message.reply_text(f"🎬 Link for *{keyword.title()}*:\n{link}", parse_mode="Markdown")
            return

    await update.message.reply_text("❌ Movie not found. Please Enter the Correct Movie Name", parse_mode="Markdown")


# ─────────── Main ───────────
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("hello", hello))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))

    print("🎥 Movie Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
