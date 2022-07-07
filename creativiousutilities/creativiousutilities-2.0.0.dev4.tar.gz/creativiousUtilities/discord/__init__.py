import discord
import os
from os import path
import logging
from discord.ext import commands


def loadAllCogs(bot : commands.Bot, cogFolder : str, logger : logging.Logger = None):
    """Loads all cogs when given the bot object and the folder for the cog"""
    cogs = []
    cogFolderExtensionFormat = (f"{cogFolder.replace('/', '.')}." if cogFolder.replace('/', '.')[-1:] != "." else cogFolder.replace('/', '.')) # Quick checks and fixes
    if path.exists(cogFolder):
        items = os.listdir(cogFolder)
        cogs = [bot.load_extension(f"{cogFolderExtensionFormat}{item[:-3]}") for item in items if item[-3:] == ".py"] # Grabbing all the cogs
    if logger is not None:
        logger.debug(cogs)

    else:
        raise "Couldn't find the given path, please enter the correct path and try again!"