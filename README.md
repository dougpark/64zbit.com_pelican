# Pelican static website generator for 64zbit.com

## History
* Started in January 2022 using Obsidian
* Switched to VS Code in September 2022
* Decided Obsidian was overkill for my needs and switch to a more familiar editor

## Included options
- [Template based on aboutwilson](https://github.com/getpelican/pelican-themes/tree/master/aboutwilson)
- [pelican.plugins.obsidian](https://github.com/jonathan-s/pelican-obsidian)
- [pelican.plugins.share_post](https://github.com/pelican-plugins/share-post)
- [pelican search](https://github.com/pelican-plugins/search)

## Core System
- Python 3.9.5
- Jinja2
- Markdown
- [Pelican Docs](https://docs.getpelican.com/en/latest/quickstart.html)
- [Install Pelican](https://docs.getpelican.com/en/latest/install.html)

## Usage
- Develop: pelican --listen --autoreload
- Prod: make publish - to create a published version locally
- Prod: make build - to create locally and upload to website

## VS Code Extensions
* [File Templates for VSCode v1.1.0](https://marketplace.visualstudio.com/items?itemName=bam.vscode-file-templates)
* [Paste Image v1.0.4](https://marketplace.visualstudio.com/items?itemName=mushan.vscode-paste-image)
* [Paste URL v0.5.4](https://marketplace.visualstudio.com/items?itemName=kukushi.pasteurl)
* [Spelling Checker for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker)


## Customizations
* File Templates - created new workspace template: .vscode/templates/Article.md
* File Templates - modified code to output ISO date format:
* .../commands/newfilefromtemplate.js: new Date().toISOString())

## Custom Short-cut keys
* ctrl-v paste image
* ctrl-b paste link
* cmd-n  new file from template

## Tip
* Markdown comment hack, does not show up in generated html
* ```[//]: # (This may be the most platform independent comment)```



### Revisions
- Initial Release: January 2022 
- Last Update: September 2022