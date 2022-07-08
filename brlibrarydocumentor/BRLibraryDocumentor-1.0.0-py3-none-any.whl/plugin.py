import re
from markdown import Markdown
from mkdocs.plugins import BasePlugin
from mkdocs.config import config_options, Config
from jinja2 import Environment, FileSystemLoader
import os
from os import makedirs, path, listdir
from pathlib import Path

from functools import partial
from mkdocs.structure.pages import Page

from brLibrarydocumentor.functionblock import ASLibrary, ASLibraryFunction, ASLibraryDataType

DIR_PATH = Path(os.path.dirname(os.path.realpath(__file__)))

class BRLibraryDocumentor(BasePlugin):
    config_scheme = (
        ('LibraryName', config_options.Type(str, default='')),
        ('LibraryPath', config_options.Type(str, default='')),
        ('GeneralInformation', config_options.Type(bool, default=True)),
        ('FunctionBlocks', config_options.Type(bool, default=True)),
        ('DataTypes', config_options.Type(bool, default=True)),
        ('GenerateSource', config_options.Type(bool, default=True))
    )

    def on_config(self, config):
        self.lib = self.readLibrary(self.config['LibraryName'],self.config['LibraryPath'])
        #AS Help links will not work if we use directory URLs, so have to change the option if the user has not enabled this setting
        if config['use_directory_urls']:
            config['use_directory_urls'] = False
            
    def on_env(self, env, config, files):
        search_path = os.path.join(DIR_PATH, "Templates","html")
        file_loader = FileSystemLoader(search_path)
            
        env = Environment(loader = file_loader,trim_blocks=True,lstrip_blocks=True)

    def on_nav(self, nav,config, files):
               
        # Look to see if the library name is a present section
        # if it is, the user has defined their own page so we don't need to do anything there
        # if it isn't, we'll need to look and find the files and add them ourselves
        #   To enable, the user would need a folder with the library name, and then a root directory file of the name index.md underneath it
        found = False
        for n in nav:
            if n.title == self.config['LibraryName']:
                found = True
        if found:
            print("{0} found in nav".format(self.config['LibraryName']))
        else:
            print("{0} not found in nav, adding..".format(self.config['LibraryName']))

        return nav
    
    def readLibrary(self, libraryName, libraryPath):
        funFileContents = ''
        typFileContents = ''
        for i in self.getLibraryItems(libraryPath):            
            if i.endswith('.typ'):
                with open(i) as file:
                    typFileContents = file.read()
            if i.endswith('.fun'):
                with open(i) as file:
                    funFileContents = file.read()
        lib = ASLibrary(libraryName,funFileContents,typFileContents)
        return lib
    
    #Search the library directory to find all .typ, .var, .fun files and add them to a list
    def getLibraryItems(self, libraryPath):
        itm = []
        for f in os.listdir(os.path.join(libraryPath)):
            suf = Path(f).suffix
            if suf == '.typ' or suf == '.var' or suf == '.fun':
                itm.append(os.path.join(libraryPath,f))
        return itm

    def on_page_content(self,html,page,config,files):
        search_path = os.path.join(DIR_PATH, "Templates","html")
        file_loader = FileSystemLoader(search_path)
            
        env = Environment(loader = file_loader,trim_blocks=True,lstrip_blocks=True)
        if re.match(r'<p>{{(.*)}}<\/p>',html) is not None:
            #we've found a callout that needs to be enterpretted
            baseText = str(html) #doing this as strings are immutable
            for txt in re.finditer(r'<p>{{(.*)}}<\/p>',baseText):
                if txt.group(1).split('.')[0] == self.config['LibraryName']:
                    #We've found a callout that matches the configured library name
                    if txt.group(1).split('.')[1] in self.lib._functions:
                        html = re.sub(
                            r'(<p>{{' + r'({0}.{1})((.Title)|(.Description)|(.Faceplate)|(.Table))'.format(self.config['LibraryName'],txt.group(1).split('.')[1]) + r'}}</p>)',
                            partial(self.renderFunctionData, function = self.lib._functions[txt.group(1).split('.')[1]], env = env),
                            html,
                            count = 1
                            )
        return html
    
    def renderFunctionData(self, match, function, env):
        #Need to check if the user selected one of the following pieces:
                            # Function Or Function Block
                            # Data Type
                            # Enumeration
        if match.group(3) == ".Title":
            template = env.get_template("fbTitle.html")
            return template.render(LibraryName = self.lib.Name,functionBlock = function)
        elif match.group(3) == ".Description":
            template = env.get_template("fbDescription.html")
            return template.render(functionBlock = function)
        elif match.group(3) == ".Faceplate":
            template = env.get_template("fbFaceplate.html")
            return template.render(functionBlock = function)
        elif match.group(3) == ".Table":
            template = env.get_template("fbParameterTable.html")
            return template.render(functionBlock = function)

  