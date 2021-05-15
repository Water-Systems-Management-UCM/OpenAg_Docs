
# install miniconda

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

# download release of stormchaser

# redirect logging in waterspout

# rename local_settings_template and databases_template

# fill in values for local_settings

# run waterspout setup commands

# set up runprocessor as some kind of automatic service

# set up fastcgi application in IIS
 -- needs more variables set up, including PATH, with
        C:\Users\IEUser\.conda\envs\washington\Library\bin;C:\Users\IEUser\.conda\envs\washington;C:\Users\IEUser\.conda\envs\washington\bin;

# Need multiple paths in IIS routed to fastcgi

# set IIS document root to the stormchaser build folder
