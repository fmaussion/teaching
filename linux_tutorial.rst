.. -*- rst -*- -*- restructuredtext -*-
.. This file should be written using restructured text conventions

==========================================
A short tutorial to the Linux command line
==========================================

This document is a very short introduction to the linux systems used at the Univeristy of Innsbruck and to the Linux command line. 

It was largely inspired from the first parts of Michael Stonebank's `UNIX tutorial <http://www.ee.surrey.ac.uk/Teaching/Unix/index.html>`_

What is Linux and why should I use it?
--------------------------------------

The `world wide web <http://lmgtfy.com/?q=What+is+Linux%3F>`_ is going to give a better answer than me to the first question.

I think that every student in sciences should know about the existence of Linux and know the basics of it. Meteorology students in particular will have to use it soon or late, as it is highly probable that most of the the tools and data they are using are running or have been created on Linux systems.

Linux has always been an environment for programmers and has the reputation of beiing "geeky" and "complicated". This is less true today, with many Linux distributions becoming mainstream and easy to use (my current personal favorite is `Mint <http://linuxmint.com/>`_).  

I personnaly think that Linux is even more user-friendly than Windows: once some of its particularities are understood (which can be frustrating in the beginning since it works *very* differently than windows), one can see that there is much less "hidden" in Linux than in Windows (especially when installing/deinstalling softwares).

Its command line utilities are very powerful, but we will just learn the basics before we get started with Python.

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

When loging in we are automatically located in our personal ``home`` directory, which is aptly named because:

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

**Exercise**: make a directory called ``backup`` in the ``unixstuff`` directory


The directories . and ..
------------------------

Still in the ``unixstuff`` directory, type::

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

**~ (your home directory)**

Home directories can also be referred to by the tilde ``~`` character. It can be used to specify paths starting at your home directory. So typing::

  $ ls ~/unixstuff

will list the contents of your unixstuff directory, no matter where you currently are in the file system.

Copying files
-------------

**cp (copy)**

``cp file1 file2`` is the command which makes a copy of ``file1`` in the current working directory and calls it ``file2``

What we are going to do now, is to take a file stored in an open access area of the file system, and use the ``cp`` command to copy it to your unixstuff directory.

First, ``cd`` to your unixstuff directory::

  $ cd ~/unixstuff

Then type::

  $ cp /scratch/c707/c7071047/tuto/science.txt .

**Note**: Don't forget the dot . at the end. Remember, in linux, the dot means the current directory.

The above command means "copy the file science.txt to the current directory, keeping the name the same".

**Note**: The directory ``/scratch/c707/c7071047/tuto`` is an area to which everyone in the University has read and copy access. If you are from outside the University, you can grab a copy of the file from the internet. For this, you can use another very useful command, ``wget``::

  $ wget http://www.ee.surrey.ac.uk/Teaching/Unix/science.txt
  
This will download the file ``science.txt`` to your current directory

**Exercise**: Create a backup of your ``science.txt`` file by copying it to a file called ``science.bak``

Moving files
------------

**mv (move)**

``mv file1 file2`` moves (or renames) ``file1`` to ``file2``

To move a file from one place to another, use the ``mv`` command. This has the effect of moving rather than copying the file, so you end up with only one file rather than two.

It can also be used to rename a file, by moving the file to the same directory, but giving it a different name.

We are now going to move the file ``science.bak`` to your ``backup`` directory.

First, change directories to your ``unixstuff`` directory. Then type::

  $ mv science.bak backup/.

Type ``ls`` and ``ls backup`` to see if it has worked.

Removing files and directories
------------------------------

**rm (remove), rmdir (remove directory)**

To delete (remove) a file, use the ``rm`` command. As an example, we are going to create a copy of the ``science.txt`` file then delete it.

Inside your ``unixstuff`` directory, type::

  $ cp science.txt tempfile.txt 
  $ ls
  $ rm tempfile.txt
  $ ls

You can use the ``rmdir`` command to remove a directory (make sure it is empty first). Try to remove the ``backup`` directory. You will not be able to since linux will not let you remove a non-empty directory.

Displaying the contents of a file on the screen
-----------------------------------------------

**clear (clear screen)**

Before you start the next section, you may like to clear the terminal window of the previous commands so the output of the following commands can be clearly understood.

At the prompt, type::

  $ clear

This will clear all text and leave you with the ``$`` prompt at the top of the window.

 
**cat (concatenate)**

The command ``cat`` can be used to display the contents of a file on the screen. Type::

  $ cat science.txt

As you can see, the file is longer than than the size of the window. You can scroll back but this is not very useful.


**less**

The command ``less`` writes the contents of a file onto the screen a page at a time. Type::

  $ less science.txt

Press the ``[space-bar]`` if you want to see another page, and type ``[q]`` if you want to quit reading. As you can see, ``less`` is used in preference to ``cat`` for long files.

 
**head**

The ``head`` command writes the first ten lines of a file to the screen.

First clear the screen then type::
  
  $ head science.txt

Then type::

  $ head -5 science.txt

What difference did the ``-5`` do to the head command?

 
**tail**

The tail command writes the last ten lines of a file to the screen.

Clear the screen and type::

  $ tail science.txt

**Exercise**: How can you view the last 15 lines of the file?

Searching the contents of a file
--------------------------------

**Simple searching using ``less``**

Using ``less``, you can search though a text file for a keyword (pattern). For example, to search through ``science.txt`` for the word "science", type:

  $ less science.txt

then, still in ``less``, type a forward slash ``[/]`` followed by the word to search::

  /science

And tape ``[enter]``. Type ``[n]`` to search for the next occurrence of the word.

 
**grep**

``grep`` is one of many standard linux utilities. It searches files for specified words or patterns. First clear the screen, then type::

  $ grep science science.txt

As you can see, ``grep`` has printed out each line containg the word science.

Or has it ????

Try typing::

  $ grep Science science.txt

The ``grep`` command is case sensitive; it distinguishes between Science and science.

To ignore upper/lower case distinctions, use the ``-i`` option, i.e. type::

  $ grep -i science science.txt

To search for a phrase or pattern, you must enclose it in single quotes (the apostrophe symbol). For example to search for spinning top, type::

  $ grep -i 'spinning top' science.txt

Some of the other options of ``grep`` are:
- ``-v`` display those lines that do NOT match
- ``-n`` precede each matching line with the line number
- ``-c`` print only the total count of matched lines

Try some of them and see the different results. Don't forget, you can use more than one option at a time. For example, the number of lines without the words science or Science is::

  $ grep -ivc science science.txt

Edit a file to install python
-----------------------------

There are some *very* powerful text editor systems in the linux command line, but they can be scary at the first sight. Therefore, we will use a normal (graphical) text editor to do the last and most important part of the tutoral: "install" the  python packages on your system.

We will edit a file called ``.bashrc`` in your ``$home`` directory. As you can see, this file starts with a dot (``.``), meaning that this is a system file. So don't mess with it! Open the file in the standard editor by typing::

  $ gedit ~/.bashrc
  
``gedit`` is the name of the editor program (like Window's "Notepad"). At the end of this file, add the following two lines::

  # added for the physics of climate course:
  export PATH="/scratch/c707/c7071047/miniconda3/bin:$PATH"
  
Save the file (``[ctrl+s]`` or click on "Save") and close the editor. See if everything worked fine by typing::

  $ less ~/.bashrc
  
What did we just do? This is a bit complicated but in simple words, we just told linux to look into that folder and look for programs in it. If linux finds a program, it will add it to its "list of programs". For this change to take effect, you should close the terminal window and open a new one. In this new terminal, type::

  $ python

If everything worked fine, you should see the following::

  Python 3.4.3 |Continuum Analytics, Inc.| (default, Oct 19 2015, 21:52:17) 
  [GCC 4.4.7 20120313 (Red Hat 4.4.7-1)] on linux
  Type "help", "copyright", "credits" or "license" for more information.
  >>> 

**If you don't see this, let me know!**

Type ``[ctrl+d]`` to quit the python prompt.


About
-----

:Aknowledgements:
    - Largely inspired from Michael Stonebank's `UNIX tutorial <http://www.ee.surrey.ac.uk/Teaching/Unix/index.html>`_

:Author:
    - Fabien Maussion - fabien.maussion@uibk.ac.at


