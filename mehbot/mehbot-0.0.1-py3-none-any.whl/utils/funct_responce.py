def simple (input_text):
    usr_msg = str(input_text).lower()

    if usr_msg in ("hello" , "hi"):
        return "whats up "
    return "meeh"


def debut(context, update):
    update.message.reply_text('...')


def responce(update, context):
    inp = str(update.message.text).lower()
    outp = simple(inp)
    update.message.reply_text(outp)


def error(update, context):
    print(f"command {update} did cause this error {context.error}")