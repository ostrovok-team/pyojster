import os
import shutil
from subprocess import check_call

def compile(source, target):
    cdir = os.path.abspath(os.path.dirname(__file__))
    ojster = os.path.join(cdir, 'ojster/bin/ojster')
    cmd = [ojster, source, target, '--ext', '.ojst.js', '--goog']
    print "Running ojster: ", ' '.join(cmd)
    check_call(cmd)
    print "Done"

def install(target_dir):
    ojster_location = os.path.abspath(os.path.dirname(__file__))
    ojster_location = os.path.join(ojster_location, 'ojster/client/goog/ojster.js')
    shutil.copy2(ojster_location, target_dir)

    
