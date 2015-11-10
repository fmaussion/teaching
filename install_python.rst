Install Python for the exercises
================================

Unlike Matlab or IDL, Python's scientific track is not installed "out of the box" with a single installation file. 

Fortunately, there are very useful tools out there to help us out. The most useful is `Miniconda <http://conda.pydata.org/miniconda.html>`_, which will help us to install Python **and** the packages we need for the exercises within a couple of minutes. The first installation step is platform specific (Windows, Linux, or Mac) while the other steps are the same on all platforms. 

Install Miniconda
-----------------

Got to the miniconda `website <http://conda.pydata.org/miniconda.html>`_ and download the **python 3.4** installer for your platform (be careful to check wether you need a 64- or 32-bit version). 

The installation is really easy and described `here <http://conda.pydata.org/docs/install/quick.html>`_.

To see if everything worked well, open a terminal window (on Windows, a `command prompt <http://windows.microsoft.com/en-us/windows-vista/open-a-command-prompt-window>`_), and type in::

    conda update conda
    
If you type::

   python

A new python prompt should appear, with something like::

   Python X.X.X |Continuum Analytics, Inc.| (default, Oct 19 2015, 21:52:17) 
   xxxx
   Type "help", "copyright", "credits" or "license" for more information.
   >>>

You can type ``exit()`` to get out of the python prompt.

Make a new environment called "climate"
---------------------------------------

Conda also helps us to define so-called "environments". A conda environment is a directory that contains a specific collection of packages that you have installed. Please have a short look at the conda introduction `here <http://conda.pydata.org/docs/intro.html>`_ before going on.

In the terminal, type::

    conda create -n climate python=3.4
    
This created a new environment called "climate" which has python V3.4 as default. This environment can be activated with one command::

   source activate climate
   
Note that after activation, the prompt changed to something like ``[climate]xxx>``. One in a specific environment, all the packages we install will be available in this environment only. This is very useful if you need different versions of python for different projects for example.

Think about activating this environment every time you want to work on the exercises or when installing a new package. You can deactivate an environment with::

   source deactivate

Install the basic packages
--------------------------

