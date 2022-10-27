# Pelican static website generator for 64zbit.com

## History
* Started in January 2022 using Obsidian
* Switched to VS Code in September 2022
* Decided Obsidian was overkill for my needs and switch to a more familiar editor
* October 2022 - added method to download and format bookmarks from Pinboard.io

## Python Core System
- Python 3.9.5
- Jinja2
- Markdown
- [Pelican Docs](https://docs.getpelican.com/en/latest/quickstart.html)
- [Install Pelican](https://docs.getpelican.com/en/latest/install.html)

## Pinboard API
- [GitHub - lionheart/pinboard.py: A full-featured Python wrapper (and command-line utility) for the Pinboard API. Built by the makers of Pushpin for Pinboard.](https://github.com/lionheart/pinboard.py) 
- [Pinboard API (v1) Documentation](https://www.pinboard.in/api/)

## Included Pelican options
- [Template based on aboutwilson](https://github.com/getpelican/pelican-themes/tree/master/aboutwilson)
- [pelican.plugins.obsidian](https://github.com/jonathan-s/pelican-obsidian)
- [pelican.plugins.share_post](https://github.com/pelican-plugins/share-post)
- [pelican search](https://github.com/pelican-plugins/search)

## Pelican Plug-Ins
- [GitHub - andrewheiss/pelican_json_feed: Pelican plugin to add a JSON Feed file to your site](https://github.com/andrewheiss/pelican_json_feed)

## Pelican Usage
- Develop: pelican --listen --autoreload
- Prod: make publish    - to create a published version locally
- Prod: make build      - to create locally and upload to website
- Dev: make dev         - to create locally and start local webserver
- make pinboard         - to download the latest links from Pinboard.io

## Pelican Customizations
* File Templates - created new workspace template: .vscode/templates/Article.md
* File Templates - modified code to output ISO date format:
* .../commands/newfilefromtemplate.js: new Date().toISOString())

## VS Code Extensions
* [File Templates for VSCode v1.1.0](https://marketplace.visualstudio.com/items?itemName=bam.vscode-file-templates)
* [Paste Image v1.0.4](https://marketplace.visualstudio.com/items?itemName=mushan.vscode-paste-image)
* [Paste URL v0.5.4](https://marketplace.visualstudio.com/items?itemName=kukushi.pasteurl)
* [Spelling Checker for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker)

## Custom VSCode Short-cut keys
* ctrl-v    - paste image with markdown formatted link, and place image in images
* cmd-b     - paste markdown formatted link
* cmd-n     - new file from article template

## Tip
* Markdown comment hack, does not show up in generated html
* ```[//]: # (This may be the most platform independent comment)```



### Revisions
- Initial Release: January 2022 
- Last Update: TBD