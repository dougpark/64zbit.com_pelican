Title: Publish Pelican To Remote Web server
Date: 2021-12-24 14:14
Modified: 2022-01-05 18:05
Category: Tech
Summary: Tips and ideas on best way to publish a static site generated with Pelican using the Makefile and creating Obsidian commands.

## Makefile
When you install Pelican be sure to install the Makefile too. This allows you to use the make command to build your static website. It takes a bit of configuration for your specific server details, but it's easy to setup.

All the details are handled in these three files:

```shell
pelicanconf.py
publishconf.py
Makefile
```

The command I ended up using is: `make ssh_upload`

This creates a production build and uploads all the files to the server.

I actually renamed `ssh_upload` in the Makefile to `prod`, so now I use the command: `make prod`

## Obsidian Shell Command

It's not bad to open a shell command and execute the `make prod` command, but it's even better to hit a hotkey within Obsidian to do the same thing.

Install the [Obsidian ShellCommands Plugin](https://github.com/Taitava/obsidian-shellcommands)

This plugin allows you to execute a shell command from within Obsidian.

It also allows you to execute that command from the Obsidian command pallet.

Which allows you to execute the command from a hotkey.

## Copy all files to remote web server

If you want to manually upload the files then here is a good use of the `scp` command.

```bash
scp -r /Users/doug/OneDrive/www_root/pelican/projects/64zbit/output/* user@64zbit.com:/home/pi/dev_volumes/public_html/apache/new/
```
