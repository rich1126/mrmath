# Python module to feed Asymptote with commands
# (modified from gnuplot.py)
from subprocess import *
class asy:
    def __init__(self):
        self.session = Popen(['asy','-quiet','-inpipe=0','-outpipe=2'],stdin=PIPE)
        self.help()
    def send(self, cmd):
        self.session.stdin.write((cmd+'\n').encode('ascii'))
        self.session.stdin.flush()
    def size(self, size):
        self.send(f"size({size});")
    def draw(self, string):
        self.send(f"draw({string});")
    def path(self, v, string):
        self.send(f"path {v} = {string};")
    def fill(self, string):
        self.send(f"fill({string});")
    def clip(self, string):
        self.send(f"clip({string});")
    def label(self, string):
        self.send(f"label({string});")
    def shipout(self, string):
        self.send(f"shipout(\"{string}\");")
    def erase(self):
        self.send("erase();")
    def help(self):
        print ("Asymptote session is open.  Available methods are:")
        print ("    help(), size(int), draw(str), fill(str), clip(str), label(str), shipout(str), send(str), erase()")
    def __del__(self):
        print ("closing Asymptote session...")
        self.send('quit');
        self.session.stdin.close();
        self.session.wait()

