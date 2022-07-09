from pathlib import Path

def provider(env):
  if Path(env['root']).is_file():
    browser_cls = env['providers'].Ziper
    upload = False
  else:
    browser_cls = env['providers'].Filer
    upload = bool(env['upload_password'])
  
  if upload:
    browser = browser_cls(env['root'],
      iconer=env['providers'].Iconer(), tfman=env['tfman']())
    return env['providers'].PasswordChecker(browser, env['upload_password'])
  else:
    return env['providers'].Filer(env['root'], iconer=env['providers'].Iconer())
  

