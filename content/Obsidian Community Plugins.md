Title: Obsidian Community Plugins
Date: 2022-01-16 20:37
Category: Tech	
Tags: Obsidian
Summary: There are several Community Plugins used to create the 64Zbit.com website. Here are a list of the ones I'm currently using.


There are several Community Plugins used to create the 64Zbit.com website. Here are a list of the ones I'm currently using.

---
### * Obsidian Shell Command

It's not bad to open a shell command and execute the `make prod` command, but it's even better to hit a hotkey within Obsidian to do the same thing.

[More info on GitHub](https://github.com/Taitava/obsidian-shellcommands)

This plugin allows you to execute a shell command from within Obsidian.

![Settings](/images/Pasted%20image%2020220117151420.png)

It also allows you to execute that command from the Obsidian command pallet. Which allows you to execute the command from a hotkey.

#### Example bash script to copy all files to remote web server

If you want to manually upload the files then here is a good use of the `scp` command.

```bash
scp -r /Users/doug/OneDrive/www_root/pelican/projects/64zbit/output/* user@64zbit.com:/home/pi/dev_volumes/public_html/apache/new/
```

---

### * Customizable Page Header

Add a button to the page header area of Obsidian to run an Obsidian command. Such as the afore mentioned Shell Command to publish the Pelican website to the production server.

![Settings](/images/Pasted%20image%2020220117151631.png)

[More info on GitHub](https://github.com/kometenstaub/customizable-page-header-buttons)

---

### * Paste URL Into Selection
A super helpful utility that detects when there is a URL in the clipboard and then pastes it in the correct format into Obsidian. Detects images too.

![Settings](/images/Pasted%20image%2020220117155138.png)

[More info on GitHub](https://github.com/denolehov/obsidian-url-into-selection)