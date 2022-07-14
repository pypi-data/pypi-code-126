import click


@click.command()
@click.option('--type', prompt=True, type=click.Choice(['react_oss', 'react_k8s']), default='react_oss')
def cli(**kwargs):
  if 'react_oss' == kwargs.get('type'):
    from glab_preset.presets.react_oss import react_oss
    react_oss()
  else:
    click.echo('Not support.')


if __name__ == '__main__':
  cli()
