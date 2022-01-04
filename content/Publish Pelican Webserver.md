Title: Publish Pelican To Remote Webserver
Date: 2021-12-24 14:14
Category: Tech

Copy all files to remote webserver

	:::bash
	scp -r /Users/dougpark/OneDrive/www_root/pelican/projects/64zbit/output/* pi@64zbit.com:/home/pi/dev_volumes/public_html/apache/new/
