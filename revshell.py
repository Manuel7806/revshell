import argparse
from Shells import shells

description = "A program that will display a reverse shell in a language of your choice"
usage = "%(prog)s -l [Local IP] -p [Port to listen on]"

parser = argparse.ArgumentParser(prog="revshell.py", description=description, usage=usage)

parser.add_argument("-l", help="local IP", required=True)
parser.add_argument("-p", help="port to listen on", required=True)
parser.add_argument('-s', help="the reverse shell you want", required=True)

args = parser.parse_args()

IP = args.l
port = args.p
shell = args.s

if shell == "bash":
    shells.bash(IP, port)
elif shell == "perl":
    shells.perl(IP, port)
elif shell == "python":
    shells.python(IP, port)
else:
    print("I am working on the other shells")
