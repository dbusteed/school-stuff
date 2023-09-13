# IS 404 -- Firewall Lab

[<< Back to main](readme.md)

This walkthrough will get you started managing firewall rules for a Linux system. You should already conceptually understand what firewalls are and how they work.

## Intro to IPTables, Setup

IPTables is the most command firewall used on Linux systems. It monitors incoming and outgoing traffic to the server. Your Linux server will most likely have it installed already. You can double check by entering the `iptables` command with the `--version` option:
```
$ iptables --version
```
Checkout the manual page for `iptables` or use the `--help` option to see all the possible commands for IPTables. We aren't going to cover every possible `iptables` command, but remember to use this built-in reference if you run in to any issues along the way.

Let's get started by viewing all the rules associated with our firewall. Remember that firewalls are essentially a big list of rules that determine what packets are allowed to pass in and out of the server. If you look closely in the `iptables` documentation, you should see that we can use the `-L` / `--list` option to list the firewall rules. Give it a try!
```
$ iptables -L
```
What happened? Did you get a "Permission denied" error? As you can imagine, we don't want just any user messing around with our firewall, only administrators or those with elevated priveleges should be able to manage firewall rules. Try adding `sudo` to run the command as the root user:
```
$ sudo iptables -L
```
This works just fine, but you might get tired of writing `sudo` before every command. Instead, let's do something that you **generally SHOULDN'T do (especially at work)**. Let's become the root user and run all our commands there!
```
$ sudo -s
```
You'll notice that the shell examples will be prefixed with `#` instead of `$`, a conventional marker of the root user. Double check that you are the root user with the following command:
```
# whoami
root
```

---
## Basic Rule Management

Now that that's taken care of, let's actually get started managing our firewall rules. If you haven't already, view the firewall rules with 
```
# iptables -L
```
Even though we don't have any rules yet, you should see that there are three different rule types: INPUT, FORWARD, and OUTPUT. These should be pretty self-explanatory, but basically, INPUT rules are for traffic that are entering the server, OUTPUT rules deal with traffic leaving the server, and FORWARD are for rules that define traffic passing through the server.

The basic command structure we will be using for managing firewall rules is as follows:
```
# iptables -[ACD] TYPE -p <protocol (tcp/udp)> --dport <port no.>  -j <target>
```
The first option will be either `-A` for add, `-C` for check, and `-D` for delete. The following parameters specify the rule we will be working with.

Let's make a rule to get a feel for the command. Let's say we have a website on our server, and we want to make sure that HTTP requests can pass through the firewall. Since HTTP is uses TCP on port 80, the command would be as follows:
```
# iptables -A INPUT -p tcp --dport 80 -j ACCEPT
```
Pretty simple right? We add an INPUT rule, that accepts all TCP requests on port 80. You can use `iptables -L -v` to check out the new rule you made (the `-v` option just gives us more details).

Let's try something similar, but this time let's block incoming traffic. Pretend that someone is running their personal website on the company server by using port 8081. We can block traffic to this connection by doing the following:
```
# iptables -A INPUT -p tcp --dport 8081 -j DROP
```
Instead of using the `ACCEPT` keyword, we are telling the firewall to `DROP` all incoming traffic from port 8081. Instead of blocking individual ports one-by-one, it is easier to simply "open up" the ports that we need access to, then block all remaining ports with:
```
# iptables -A INPUT -j DROP
``` 

---
## Hands-On Example

Now that you are a master of managing firewall rules, let's see these rules in action.

Instead of writing more commands and instructions, I thought it was easier to make a video that you can follow along with. 

[WATCH VIDEO](https://www.youtube.com/watch?v=Mv3FABASr5U)


---
## THANKS!

(and thanks to [this tuorial](https://www.hostinger.com/tutorials/iptables-tutorial))