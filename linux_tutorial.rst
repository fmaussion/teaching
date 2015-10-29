.. -*- rst -*- -*- restructuredtext -*-
.. This file should be written using restructured text conventions

==========================================
A short tutorial to the Linux command line
==========================================

This document is a very short introduction to the linux systems used at the Univeristy of Innsbruck and the Linux command line. 

It was largely inspired from the first parts of Michael Stonebank's `UNIX tutorial <http://www.ee.surrey.ac.uk/Teaching/Unix/index.html>`_

What is Linux and why should I use it?
--------------------------------------

The `world wide web <http://lmgtfy.com/?q=What+is+Linux%3F>`_ is going to give a better answer than me to the first question.

I think that every student in sciences should know about the existence of Linux and know the basics of it. Meteorology students in particular will have to use it soon or late, as it is highly probable that most of the the tools and data they are using are running or have been created on Linux systems.

Linux has always been an environment for programmers and has the reputation of beiing "geeky" and "complicated", but this is less true today, with many Linux distributions becoming mainstream and easy to use (my current personal favorite is `Mint <http://linuxmint.com/>`_).  

I personnaly think that Linux is even more user-friendly than Windows: once some particularities of its functioning are understood (which can be frustrating in the beginning since it works *very* differently than windows), one can see that there is much less "hidden" in Linux than in Windows, especially when installing/deinstalling softwares.

Its command line utilities are very powerful, but we are just learning the basics of it here in order to get started with Python.

Linux at the UIBK
-----------------

In order to use Linux in the computer room you have to register for an account `here <http://orawww.uibk.ac.at/public_prod/owa/uvw$web$10.p001>`_. After an hour or so you will be able to connect to any computer using your username and password. 

The Linux `distribution <https://en.wikipedia.org/wiki/Linux_distribution>`_ used at the university is `CentOS <https://www.centos.org/>`_ (version 6.7), and the `desktop environment <https://en.wikipedia.org/wiki/Desktop_environment>`_ is `Gnome <https://en.wikipedia.org/wiki/GNOME>`_. These details are not very important, since you will see that most of the applications we will use are similar to those in windows. For example, you will recognise the Firefox icon on the task bar.

Open a terminal
---------------

To open a terminal window, click on the "Terminal" icon from Applications/Accessories menu.

.. image:: http://www.ee.surrey.ac.uk/Teaching/Unix/media/gnome-window.gif

A terminal window will then appear with a $ prompt, waiting for you to start entering commands.

Listing files and directories
-----------------------------

**ls (list)**

When you first login, your current working directory is your home directory. Your home directory has the same name as your user-name, for example, c7071047, and it is where your personal files and subdirectories are saved.

To find out what is in your home directory, type::

  $ ls

The ``ls`` command lists the contents of your current working directory.

``ls`` does not, in fact, cause all the files in your home directory to be listed, but only those ones whose name does not begin with a dot (.) Files beginning with a dot (.) are known as hidden files and usually contain important program configuration information. They are hidden because you should not change them unless you know what you do.

To list all files in your home directory including those whose names begin with a dot, type::

  $ ls -a

As you can see, ``ls -a`` lists files that are normally hidden. 

``ls`` is an example of a command which can take options: ``-a`` is an example of an option. The options change the behaviour of the command. There are online manual pages that tell you which options a particular command can take, and how each option modifies the behaviour of the command. ``ls -lh`` is an other way tow call ``ls`` with two options, ``l`` for "listing format" and ``h`` for "human readable".


The directory structure
-----------------------

All the files are grouped together in the directory structure. The file-system is arranged in a hierarchical structure, like an inverted tree. The top of the hierarchy is traditionally called root (written as a slash ``/`` )

.. image:: http://www.ee.surrey.ac.uk/Teaching/Unix/media/unix-tree.png

When loging in we are automatically located in our personal ``home`` directory, which is aptly named:
- we won't need to leave ``home`` during our excercises
- we are allowed to do whatever we want in our ``home``, while we are not allowed to write, delete or change things in the other directories.

To know where we are in the directory structure, there is a useful command::

  $ pwd
  
which prints the name of the current working directory.

Making Directories 
------------------

**mkdir (make directory)**

We will now make a subdirectory in your home directory to hold the files you will be creating and using in the course of this tutorial. To make a subdirectory called ``unixstuff`` in your current working directory type::

  $ mkdir unixstuff 

To see the directory you have just created, type::

  $ ls
  
Changing to a different directory
---------------------------------

**cd (change directory)**

The command ``cd directory`` means change the current working directory to "directory". The current working directory may be thought of as the directory you are in, i.e. your current position in the file-system tree.

To change to the directory you have just made, type::

  $ cd unixstuff

Type ``ls`` to see the contents (which should be empty)

The directories . and ..
------------------------

Still in the unixstuff directory, type::

  $ ls -a

As you can see, in the unixstuff directory (and in all other directories), there are two special directories called (.) and (..)

**The current directory (.)**

In linux, (.) means the current directory, so typing::

  $ cd .

means "stay where you are" (the unixstuff directory).

This may not seem very useful at first, but using (.) as the name of the current directory will save a lot of typing, as we shall see.

**The parent directory (..)**

(..) means the parent of the current directory, so typing::

  $ cd ..

will take you one directory up the hierarchy (back to your home directory). Try it now.

**Note**: typing cd with no argument always returns you to your home directory. This is very useful if you are lost in the file system. 
