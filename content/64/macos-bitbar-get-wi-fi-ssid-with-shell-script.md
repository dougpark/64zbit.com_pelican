Title: macOS - BitBar - Get Wi-Fi SSID with shell script
Date: 2020-10-18 00:14
Author: D
Category: Tech
Tags: Tech
Slug: macos-bitbar-get-wi-fi-ssid-with-shell-script


So, [Jason Snell](https://sixcolors.com/) got me hooked on [BitBar](https://sixcolors.com/post/2020/08/put-anything-in-your-macs-menu-bar-with-bitbar/) (BitBar (by [Mat Ryer - @matryer](https://twitter.com/matryer)) lets you put the output from any script/program in your Mac OS X Menu Bar.) and I've been working on a plugin ever since. Here's a quick way to get your current Wi-Fi SSID.

```bash
function display-ssid {
	echo "---"
ssid=$(/System/Library/PrivateFrameworks/Apple80211.framework/Resources/airport -I  | awk -F' SSID: '  '/ SSID: / {print $2}') 
	echo "Wi-Fi: $ssid | terminal=false bash='$0' param1=copy param2=$ssid"
	
}
```



Get wireless SSID through shell script on Mac OS X

Is there any way to get the SSID of the current wireless network through a shell script on Mac OS X?

![](https://cdn.sstatic.net/Sites/stackoverflow/Img/apple-touch-icon.png?v=c78bd457575a)Mark SzymanskiStack Overflow



[SSID with shell script](https://stackoverflow.com/questions/4481005/get-wireless-ssid-through-shell-script-on-mac-os-x)