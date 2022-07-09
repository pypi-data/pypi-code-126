from pathlib import Path as libpath

WebBasePath = libpath(__file__).parent
BuiltStaticPath = f"{WebBasePath}/_built-static"
TemplatePath = f"{WebBasePath}/_template"
SingleTemplatePath = f"{WebBasePath}/_single_template.py"
