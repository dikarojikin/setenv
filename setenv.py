import os
import sys

clawdir = os.path.abspath('.')   
CLAW = clawdir

print " "
print "------------------------------------------------------------"

try:
    # check if the Fortran Compiler is already set:
    FC = os.environ['FC']
except:
    FC = 'gfortran'

if FC in ['f77','g77']:
    print '*** FC = ',FC,' will not work with this version.'  
    print '    gfortran or other flavor of f90/95 required'
    print '*** resetting FC to gfortran\n'
    FC = 'gfortran'

clawpythondir = os.path.join(clawdir,'python')
PYTHONPATH = ":".join((clawpythondir,"${PYTHONPATH}"))


clawmatlabdir = os.path.join(clawdir,'matlab')
try:
    MATLABPATH = os.environ['MATLABPATH']
except:
    MATLABPATH = clawmatlabdir

if clawmatlabdir not in MATLABPATH:
    MATLABPATH = MATLABPATH +":"+ clawmatlabdir

print "Full path to claw directory should be:"
print "      $CLAW = ",clawdir
    

setenvcsh = open("setenv.csh","w")
setenvcsh.write("setenv CLAW '%s'\n" % CLAW)
setenvcsh.write("setenv FC '%s'\n\n" % FC)
setenvcsh.write("setenv MATLABPATH '%s'\n\n" % MATLABPATH)
setenvcsh.write("setenv PYTHONPATH '%s'\n" % PYTHONPATH)
setenvcsh.write("alias clawserver 'xterm -e python $CLAW/python/startserver.py &' \n")
setenvcsh.close()

setenvbash = open("setenv.bash","w")
setenvbash.write("export CLAW='%s'\n" % CLAW)
setenvbash.write("export FC='%s'\n\n" % FC)
setenvbash.write("export MATLABPATH='%s'\n\n" % MATLABPATH)
setenvbash.write('export PYTHONPATH="%s"\n' % PYTHONPATH)
setenvbash.write("alias clawserver='xterm -e python $CLAW/python/startserver.py &' \n")
setenvbash.close()

print "------------------------------------------------------------"
print "The files setenv.csh and setenv.bash contain the appropriate"
print "commands to set environment variables for csh or bash shells"
print "  and also some aliases you may find convenient             "
print "------------------------------------------------------------"
