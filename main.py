from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from control import *

TOKEN = "7946940728:AAEacC2_THEg7lwOJKGOgYnkWvz1cg_5GKc"

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.add_handler(CommandHandler("add", add))

app.run_polling(drop_pending_updates=True)

print("Programa funcionando correctamente")
