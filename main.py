from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final = '7307621135:AAEtDz5g5jxexa4LVfMVskjulQVoSWe3AFA'
BOT_USERNAME: Final = '@ak_taha_bot'

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('start bot')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('help ')

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('sustom ')

def handle_response(text: str) -> str:
    processed: str = text.lower()

    if 'سلام' in processed:
        return 'درود بر تو '

    if 'اسمت چیه' in processed:
        return 'اسم بنده طاها است'

    if 'حالت چطوره' in processed:
        return 'خوبم ممنون'

    return 'لطفا مثل یک انسان با شخصیت صحبت کنید'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    print("Bot response:", response)
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
    print('Starting bot...')
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start_command))  
    app.add_handler(CommandHandler('help', help_command))  
    app.add_handler(CommandHandler('custom', custom_command))  

    app.add_handler(MessageHandler(filters.TEXT, handle_message)) 
    app.add_error_handler(error)

    print('Polling...')
    app.run_polling(poll_interval=3)
