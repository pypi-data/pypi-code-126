import logging

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

import click
from dotenv import dotenv_values
from telegram import Update
from telegram.ext import CallbackContext, Filters, MessageHandler, Updater

from maxbot.bot import MaxBot
from maxbot.channels import TelegramShim
from maxbot.errors import BotError
from maxbot.schemas import Definitions


@click.command()
@click.option(
    "-f",
    "botyaml",
    type=click.Path(exists=True, dir_okay=False),
    required=True,
    help="Path for bot.yaml",
)
@click.option(
    "--no-updates",
    is_flag=True,
    default=False,
    help="Do not poll for updates. Just delete webhook and exit (Useful for tests)",
)
def run(botyaml, no_updates):
    """
    Run bot locally.
    """
    try:
        definitions = Definitions().from_yaml(botyaml, dotenv_values())
    except BotError as exc:
        raise click.ClickException(exc)
    shim = TelegramShim(MaxBot(definitions))

    def callback(update: Update, context: CallbackContext):
        shim(update, context.bot)

    updater = Updater(definitions.channels.telegram.api_token)
    updater.dispatcher.add_handler(MessageHandler(Filters.all, callback))
    updater.start_polling()
    if no_updates:
        updater.stop()
        return
    updater.idle()


@click.group()
def main():
    pass


main.add_command(run)
