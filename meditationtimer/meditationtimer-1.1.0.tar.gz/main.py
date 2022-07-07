import click
import time
import math

defaultargs = {
 "no_args_is_help" : False,
 "context_settings": dict(help_option_names=['-h', '--help'])
}

totalargs = {
	"default": 300,
	"help": "time in seconds"
}

delayargs = {
	"default": 10,
	"help": "Delay the countdown, to prepare for the session."
}

@click.command(**defaultargs)
@click.option('-t', '--total', **totalargs)
@click.option('-d', '--delay', **delayargs)
def progressbar(total, delay):	
	with click.progressbar(
		range(delay),
		show_percent=False,
		fill_char= "·",
		empty_char=" ",
		bar_template='%(label)s %(bar)s %(info)s',
		width=0, #full terminal width
		label="Preparing"
		) as t:
		for s in t:
			time.sleep(1)

    click.echo("\a")
	with click.progressbar(
		range(total),
		show_percent=False,
		fill_char= "·",
		empty_char=" ",
		bar_template='%(label)s %(bar)s %(info)s',
		width=0, #full terminal width
		label="Meditating"
		) as t:
		for s in t:
			time.sleep(1)

	click.echo("\a")
