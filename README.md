# FLOATS_FileMaker

Steps for running this:

1. Create and activate a conda environment using the environment.yml file by typing the following from the directory containing environment.yml. 
 - conda env create  #automatically creates an environment by reading in the environment.yml file. The environment will be called "st1", and will contain all necessary packages
 - conda activate st1

2. Set up the paths and enter your CCMz user/pass in Generate_FLOATS_Config.py and run it. This creates a file with a default name of FLOATS.yaml that will be read in by GetFLOATS_NoUser.py.
 - (alternative method) Modify the provided FLOATS_example.yaml file to suit your needs directly.
 - Make sure that any of the paths exist for the files in the config file

3. Run GetFLOATS_NoUser.py. This program assumes a config file called FLOATS.yaml exists in the same directory.
