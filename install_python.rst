Install Python for the exercises
================================

**Note:** if you already have miniconda installed (for example since the 
physics of climate or the glaciology courses) you can jump directly to 
`Update the packages`_ . 

Unlike Matlab or IDL, Python's scientific track is not installed
"out of the box" with a single installation file.

Fortunately, there are very useful tools out there to help us out.
The most useful is `Miniconda <http://conda.pydata.org/miniconda.html>`_,
which will help us to install Python **and** the packages we need for the
exercises within a couple of minutes. The first installation step is platform
specific (Windows, Linux, or Mac) while the other steps are the same on all
platforms.


Install Miniconda
-----------------

Got to the miniconda `website <http://conda.pydata.org/miniconda.html>`_ and
download the **python 3.5** installer for your platform (be careful to
check whether you need a 64- or 32-bit version).

The installation is really easy and described
`here <http://conda.pydata.org/docs/install/quick.html>`_. Be careful to
choose an installation directory where you have enough space
(conda installations can quickly grow larger than a few GB).

To see if everything worked well, open a terminal window (on Windows, a
`command prompt <http://windows.microsoft.com/en-us/windows-vista/open-a-command-prompt-window>`_)
, and type in::

    conda update conda
    
If you type::

   python

A new python prompt should appear, with something like::

   Python X.X.X |Continuum Analytics, Inc.| (default, Oct 19 2015, 21:52:17) 
   xxxx
   Type "help", "copyright", "credits" or "license" for more information.
   >>>

You can type ``exit()`` aor ``[CTRL+D]``to get out of the python prompt.


Make a new environment called "climate"
---------------------------------------

Conda also helps us to define so-called "environments". A conda environment is
a directory that contains a specific collection of packages that you have
installed. Please have a short look at the conda introduction
`here <http://conda.pydata.org/docs/intro.html>`_ before going on.

In the terminal, type::

    conda create -n climate python=3.5
    
This created a new environment called "climate" which has python V3.5 as
default interpreter. This environment can be activated with one command::

   source activate climate
   
or on windows::

   activate climate
   
Note that after activation, the prompt changed to something like
``[climate]xxx>``. Once in a specific environment, all the packages we
install will be available in this environment only. This is very useful
if you need different versions of python for different projects for example.

**Don't forget to activate this environment** every time you want to work on
the exercises or when you want to install a new package. You can deactivate
the current environment with::

   source deactivate
   
or on windows::

   deactivate


Install the packages
--------------------

First we are going to tell conda where to look for packages:: 

   conda config --add channels conda-forge
 
This has to be done only once. `conda-forge <http://conda-forge.github.io/>`_ 
is a package repository, once you have set it up as default you don't 
have to worry about it any more.

There are a couple of packages that you will always need, whatever you are
working on. These are: `ipython <http://ipython.org/>`_,
`Jupyter <https://jupyter.org/>`_, `numpy <http://www.numpy.org/>`_,
`matplotlib <http://matplotlib.org/>`_.

Once you are in the "climate" environment, type::

    conda install numpy matplotlib ipython jupyter

This will download the packages and install them, as well as their
dependencies. This can take a while! If successful, you should now be able to
start the notebook for example::

    jupyter-notebook
    
Use ``control-c`` to close the server and get back to the prompt.

For the glaciology excercises it will be necessary to install 
`pandas <http://pandas.pydata.org/>`_::

    conda install pandas

I also recommend to install further useful packages (for example to 
read meteorological and climatological data),
`netcdf4 <http://unidata.github.io/netcdf4-python/>`_
and `xarray <http://xarray.pydata.org/>`_::

    conda install netcdf4 xarray

And finally, install the package required to plot on map projections::

    conda install cartopy
    

Update the packages
-------------------

If you already have a working conda, you can simply update your packages
instead of making a new environment. Note that the xray package has changed 
a bit during the last year, and that your climate notebooks won't work anymore
(but you can always correct them). First, activate your environment::

   source activate climate
 
If not already done before, set the conda-forge default channel::

   conda config --add channels conda-forge
 
And then simply update them all::

   conda update --all



Download the exercises and the data
-----------------------------------

The exercises (*.ipynb files) and the data can be downloaded from OLAT.
Open `00_Getting_Started.ipynb` to start to learn Python!

