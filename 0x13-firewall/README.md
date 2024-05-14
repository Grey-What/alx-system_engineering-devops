# 0x13. Firewall
This project focus on what a firewall is, the two different types of firewalls and the main function of a firewall. The firewall that will be investigated and applied is ufw.

The main task to complete is the installation of ufw on my two main nginx webservers and the server hosting the HAProxy loadbalancer

### Task:
0. Block all incoming traffic but:
   install the ufw firewall and setup a few rules on web-01.
   Requirements:
   - The requirements below must be applied to web-01 \
   (feel free to do it	on lb-01 and web-02, but it won’t be checked)
   - Configure ufw so that it blocks all incoming traffic, except the following TCP ports:
     > 22 (SSH)
     > 443 (HTTPS SSL)
     > 80 (HTTP)
---
