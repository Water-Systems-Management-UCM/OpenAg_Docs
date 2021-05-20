Deploying OpenAg on Windows with IIS
=====================================

OpenAg is designed to run in a Linux virtual machine, but can also be deployed on Windows using IIS and FastCGI. This
document describes setting up OpenAg to run on Windows with IIS.

Installing the Python Environment
-------------------------------------
OpenAg requires access to a binary executable of the ipopt solver via Python. The simplest way to install :code:`ipopt` is
by using Anaconda Python and installing a prebuilt package. As of May 2021, that package needs to be pinned to a
specific version because newer versions are missing required files (more on this below).

The steps to set up the Python environment are roughtly:

1. Install Miniconda, a lightweight distribution of anaconda Python
2. Create a new conda environment to isolate packages from others on the system
3. Install the correct version of :code:`ipopt` into that environment
4. Install other dependencies

Installing Miniconda
______________________
To start with, `download and install the 64 bit version of Miniconda for Python 3.8 <https://docs.conda.io/en/latest/miniconda.html>`_.
You may also use newer versions if you wish, but we recommend staying one version back from the newest release version of Python
for stability reasons. You may also use other Anaconda distributions if you already have them installed and available -
we use miniconda for convenience. You can also use another Python distribution if you prefer, but you will be responsible
for getting a compatible copy of ipopt installed as the following guide relies on Anaconda.

.. seealso::
    `Conda installation guide <https://conda.io/projects/conda/en/latest/user-guide/install/index.html>`_


Creating a New Python Environment
____________________________________
After installation, you will need to create a new conda environment, basically an isolated copy of Python, that the
application will use. When we create it, we should pay attention to the location that it is created, because we will
need to give IIS permissions to access this location to execute Python later. By default, conda will put environments
in a folder in the current user's account, so either log in as the user that IIS will execute Python code as before
creating the environment, or create the environment in a location that could be accessible to multiple users and then
assign permissions for the IIS user to read and execute in that folder, subfolders, and files. We will take the latter
approach in this guide.

Let's assume that the shared location you want to create the python environment in will be in C:\Python\environments (you
could also use something like the C:\ProgramData where conda stores other information). To set up our environment there,
we would:

1. Go to the start menu and open up :code:`Anaconda Prompt` - while you can use CMD or Powershell, etc, the Anaconda Prompt is the fastest way to get the :code:`conda` command that we'll need to be available.
2. Run the following command to create the new environment: :code:`conda create --name openag python=3.8 --path C:\Python\environments`

.. seealso::
    * `Conda Documentation: Managing Environments <https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html>`_
    * `Conda Documentation: The Conda Create Command <https://docs.conda.io/projects/conda/en/latest/commands/create.html>`_

# create new python environment in an accessible location for web server user

# numpy and pandas should come from conda

# install wfastcgi

# Add conda-forge as a channel or conda install -c conda-forge ipopt=3.11.1

# Ipopt Version pinned to 3.11.1
https://github.com/conda-forge/ipopt-feedstock/issues/55
# install ipopt

# Set up front end and back end in a directory with controllable permissions
# clone Waterspout

# get_dapper.py

# install Waterspout requirements

# redirect logging in waterspout

# rename local_settings_template and databases_template

# fill in values for local_settings

# run waterspout setup commands

# download release of stormchaser

# set up runprocessor as some kind of automatic service

# set up fastcgi application in IIS
 -- needs more variables set up, including PATH, with
        C:\Users\IEUser\.conda\envs\washington\Library\bin;C:\Users\IEUser\.conda\envs\washington;C:\Users\IEUser\.conda\envs\washington\bin;

# Need multiple paths in IIS routed to fastcgi

# set IIS document root to the stormchaser build folder
