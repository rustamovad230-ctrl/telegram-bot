import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = "BU_YERGA_TO8870339657:AAERjIEPmg-GKe2mLoE5VzYgKh6l-SquXdAKENINGIZNI_QOYING"
KANAL_LINK = "https://t.me/qalb_ovozi3"
KANAL_NOMI = "Qalb Ovozi"

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    ism = user.first_name or "Do'stim"
    xabar = (
        f"👋 Salom, {ism}!\n\n"
        f"🎭 Ko'ngilochar kontent uchun:\n\n"
        f"📢 *{KANAL_NOMI}* kanalimizga a'zo bo'ling!\n\n"
        f"👇 Quyidagi tugmani bosing:"
    )
    tugma = InlineKeyboardMarkup([
        [InlineKeyboardButton(f"🔔 {KANAL_NOMI}", url=KANAL_LINK)],
    ])
    await update.message.reply_text(xabar, parse_mode="Markdown", reply_markup=tugma)

async def xabar_qabul(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tugma = InlineKeyboardMarkup([
        [InlineKeyboardButton(f"🔔 {KANAL_NOMI}", url=KANAL_LINK)]
    ])
    await update.message.reply_text(
        f"😊 Kanalimizga a'zo bo'ling!\n👉 {KANAL_LINK}",
        reply_markup=tugma
    )

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, xabar_qabul))
    print("✅ Bot ishga tushdi!")
    app.run_polling()

if __name__ == "__main__":
    main()
