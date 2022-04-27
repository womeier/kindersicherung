Kindersicherung (child safety device)
-------------------------------------

Block access to sites utilizing the `/etc/hosts` file.
This script generates an `/etc/hosts` file that looks like this.

```
# original file
127.0.0.1   localhost
127.0.1.1   laptop
...

# generated
0.0.0.0     fb.com
0.0.0.0     tiktok.com
```

# Guide
1) Clone this repo to /etc/hosts.d/
2) Copy the current `/etc/hosts` to `/etc/hosts.d/base`
3) Add sites to block, see below.
4) Install the cron job using `install-cron.sh`, it runs as root.
5) You should never trust scripts from the internet, read `combine.py` and `install-cron.sh`.

# Blocking sites
To block a site, add it to `blocked-perm`.
To block a site temporarily, add it to `blocked-tmp`. (I like to allow access to news sites on Friday only.)

# Why?
I use this mainly to restrict access to news sites during the week.
There are other tools like [pi-hole](https://pi-hole.net/), that are great for blocking malicious domains.
