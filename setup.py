import os
from setuptools import setup
from setuptools.command.develop import develop
from subprocess import check_call

DESCRIPTION = 'Simple wrap django views to render json '

def install_deps():
    print "Installing dependencies"
    cdir = os.path.abspath(os.path.dirname(__file__))
    os.chdir(cdir)
    check_call(['git', 'submodule', 'update', '--init', '--force'])
    os.chdir(os.path.join(cdir, 'pyojster/ojster'))
    check_call(['npm', 'install', '.'])
    os.chdir(cdir)

class do_develop(develop):
    def run(self):
        install_deps()
        develop.run(self)


setup(
    cmdclass={'develop': do_develop,},
    name='pyojster',
    version='0.1',
    packages=['pyojster'],
    package_dir={'pyojster': '.'},
    package_data={'pyojster': ['ojster/*']},
    author='Yasha Borevich',
    author_email='j.borevich@gmail.com',
    url='http://github.com/ostrovok-team/pyojster',
    description=DESCRIPTION,
    long_description=DESCRIPTION,
    platforms='any',
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
)

