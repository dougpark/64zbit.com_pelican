Title: Ping network monitor
Date: 2021-03-08 22:38
Author: D
Category: Tech
Tags: Ping, Shell
Slug: ping-network-monitor

The ping command is a built in linux and macOS command that shows the performance of the network connection to a remote server. It can be used to log network performance issues over time. The default ping command displays the results to standard output (the shell window). Used with the following options it routes the output to a file that you can look at later.

> The ping command will ping the remote server every second until you manually kill the process. This will create 86,400 pings per day in the output file. It's not something you want to forget about and let it run forever. It could create a very large file that fills up your drive space and crashes your system. I run my ping network monitor on a Raspberry Pi 4 so that it will run 24 hours per day in low power and uninterupted environment.

### Ping directed to a file

You would normally just run the ping command interactivly and then stop it when you are done. But, that's not what we are doing today. We are looking for an intermident bug that may happen anytime in the future. For this we need to run the command for weeks at a time and be able to look at the results after a network error has been detected.

Here is the `ping` command, running in the background, with the output directed to a file called "network.log".  
Copy and paste this text to your command line.

```
ping google.com 2>&1 | while read pong; do date "+%c: $pong"; done >network.log &
```

Here are the details of what this command does

-   `ping` // the ping command to run
-   `google.com` // name of the remote server
-   `2>&1` // routes stderr to stdout
-   `| while read pong; do date "+%c: $pong"; done` // pipe the ping results and add the current date and time
-   `>network.log` // routes output to file network.log
-   `&` // at end means to run in background

The `pipe` command, represented by the vertical bar `|` takes the output of the first command and routes it into the second command. In this case it takes the output of the `ping` command and routes it into a command that prepends the current date and then uses the `>` command to route everthing to a file instead of standard out (stdout).

The `&` at the end of the line makes this command run in the background. This frees up your terminal so you can run other commands. It will continue running even when you exit your terminal and logout. The commands below show you how to find the background command later and control it.

### Jobs and Processes

The jobs command only works for jobs you have started in the current shell. If you exit the shell and open a new one then this command will not display your jobs. You will need to use the other commands listed below to work with system level processes.

> Fun fact: jobs are started by a user, processes are started and managed by the system. A users job is also a system process.

### Process Id

Every command running on the computer is assigned a unique process id (PID). You can use this PID to interact with background processes.

> The terms Command, Job, and Process are basically the same thing. They are programs running on your computer.

> Type `top` into your shell to see a list of the top processes running on your current computer. Notice the PID column listed on the far left. Type `q` to exit this view. For a fun day of reading type `man top` to read all the details of the `top` command.

Use the jobs command to see running background jobs, `-l` shows the process id (PID). (That’s a lowercase L)

```
jobs -l 
```

### Viewing your ping log

Use the `cat` command to view contents of the output file, use the `| more` option to show a page at a time. This could take awhile, you are getting 86,400 lines per day and paging through them a few lines at a time will get tedious.

```
cat network.log 
or
cat network.log | more
```

### Look at the output

If all goes well you should see a `time=` value at the end of each line. This tells you the ping completed successfully and you have a good connection to the server.

When the connection goes down you will receive error messages. These will be helpful in determining what went wrong.

![](https://64zbit.com/content/images/2021/03/Screenshot_2021-03-08-21.51.21_ya0Tr6.png)

Example showing a request timout error

### Use grep to find interesting data

The `grep` command will help you find interesting data in your output file.

```
cat network.log | grep -v time
```

The `-v` option tells grep to "invert match", so any line that does not contain the "time" string.

This command will search the network.log for any line that does not contain the string "time". So for any ping command that returns anything other than a normal ping time will be displayed. This includes any error messages that you should look at.

![Example showing an unreachable server](https://64zbit.com/content/images/2021/03/Screenshot_2021-03-09-11.44.55_rGKrOj.png "Example showing an unreachable server")  
Example showing an unreachable server

### Find your running ping command

Use the `pgrep` command to find running ping jobs and return the process id (PID). Pgrep is included in many Linux distributions.

```
pgrep ping 
```

![Example showing pgrep ping output](https://64zbit.com/content/images/2021/03/Screenshot_2021-03-09-11.57.09_k4jkp7.png "Example showing pgrep ping output")

`pgrep` returns the process id (PID) where the string matches. In this case the PID = 24895. Warning: Don't use this PID, use the PID you find on your own system.

### Stopping the ping command

Use the `kill` command to stop a running job. Be careful, you can kill the wrong job and crash your system. Make sure you enter the correct process id (PID) you found above.

```
kill PID 
```

Here's nother command to find the running ping processes. Use `ps` if your distribution doesn’t include the `pgrep` command. The `ps` command displays the current process status for all running processes. It's a long list and you can use `grep` to show you just what you want.

```
ps -aux | grep ping 
```

![Example showing ps -aux output](https://64zbit.com/content/images/2021/03/Screenshot_2021-03-09-12.01.43_GMlonb.png "Example showing ps -aux output")

The process id on this distribution is in the second column from the left. In this case the PID = 24895.

### Removing the network.log

When you are done with your analysis you can remove the network.log file with the `rm` command. Becareful not to remove the wrong file, this can crash your system.

```
rm network.log
```

### References

More info about the Jobs Command  
[https://www.computerhope.com/unix/ujobs.htm](https://www.computerhope.com/unix/ujobs.htm)

Date logic from  
[https://stackoverflow.com/questions/10679807/how-do-i-timestamp-every-ping-result](https://stackoverflow.com/questions/10679807/how-do-i-timestamp-every-ping-result)

Use the linux manual pages to learn more about each command.  
man kill  
man ps  
man grep  
man pgrep  
man ping  
man cat  
man more  
man jobs  
man date  
man top  
man rm

You can search for the linux pipe command too.