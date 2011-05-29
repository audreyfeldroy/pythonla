##############
LAPython Setup
##############

These instruction will help you to get going on setting LAPython website on your local machine.

Getting the source
~~~~~~~~~~~~~~~~~~

Checkout git repository for LAPython project onto your computer. For the sake of
this tutorial we will assume the following path ::

   cd ~/code/lapython

Enter tools/files and download virtualenv ::

   cd tools/files
   wget -N http://pypi.python.org/packages/source/v/virtualenv/virtualenv-1.6.1.tar.gz
   tar xvf virtualenv-*.tar.gz


Determine and Export Python Interpreter Path, Type and Version
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now, export environmental variable with desired python interpreter version and
its major version (Note: this requires bash shell).

On Ubuntu the path to the default system python is /usr/bin/python. Usually you
can search for the python binary in your PATH using ::

   which python

In case of OSX, the default system python is likely to be outdated so you’ll
need to specify the path you installed it in (usually /opt) ::

   export TMP_MY_PYPATH="<specify your python path>"
   export TMP_MY_PY_TYPE_AND_VER=$($TMP_MY_PYPATH -c 'import platform; print ("_%s%s" % (platform.python_implementation().lower(), "".join(platform.python_version_tuple()[:2]))).replace("_cpython", "")')


Create and Enter Virtual Environment for Pharaoh
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now “cd” into the LAPython site/ folder and set up the virtual environment with the folder name containing python interpreter type and version. Please note we are also using “distribute” not “setuptools” and setting a VirtualEnv shell prompt to reflect the project and the environment we are in::

   cd ../../site
   $TMP_MY_PYPATH ../tools/files/virtualenv*/virtualenv.py --no-site-packages --prompt=\(lapython-${TMP_MY_PY_TYPE_AND_VER/_//}\) _env$TMP_MY_PY_TYPE_AND_VER

Create default _env ::

   ln -s _env$TMP_MY_PY_TYPE_AND_VER _env

Enter VirtualEnv ::

   source ./_env/bin/activate

To exit run ::

  deactivate


Add Python Shell Tools and Package Management
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Install in ipython since its a better python shell ::

   pip install ipython

Add in yolk for future package management ::

   pip install yolk
