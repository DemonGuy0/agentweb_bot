from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from modelo import *
import requests

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
  await update.message.reply_text("Hola, soy un bot hecho por @killerj00 y te informare sobre el estado de cualquier pagina")
  
  await update.message.reply_text("🔰LISTA DE COMANDOS🔰\n /add-agregar sitio web ejemplo(/add https://cite.com)\n /isup Ver estado de la pagina.\n")

async def add(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Debes escribir la página seguido del comando (sin https://)")
        return
    else:
      await update.message.reply_text("Pagina agregada")
    
    try:
        # Añadir https:// si no está presente
        url = context.args[0] if context.args[0].startswith(('http://', 'https://')) else f'https://{context.args[0]}'
        
        # Verificar la URL
        response = requests.get(url)
        
        if response.status_code == 200:
            await update.message.reply_text(f"La página {url} está funcionando y se ha guardado correctamente")
            # Aquí deberías guardar la URL en tu lista/database
        else:
            await update.message.reply_text(f"La página {url} está caida (código {response.status_code})")
            
    except requests.exceptions.MissingSchema:
        await update.message.reply_text("URL inválida. Asegúrate de incluir el dominio completo (ejemplo: google.com)")
    except requests.exceptions.RequestException as e:
        await update.message.reply_text(f"Error al acceder a la página: {str(e)}")
  
  
  