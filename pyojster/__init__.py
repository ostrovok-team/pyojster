import os.path
from subprocess import check_call

def compile(source, target):
    cdir = os.path.abspath(os.path.dirname(__file__))
    ojster = os.path.join(cdir, 'ojster/bin/ojster')
    cmd = [ojster, source, target]
    print "Running ojster: ", ' '.join(cmd)
    check_call(cmd)
    print "Done"
