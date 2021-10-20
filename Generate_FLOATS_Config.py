#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 13:40:55 2021

@author: sdavis
"""

import yaml

#The path to the output yaml file
yamlfilename='/Users/sdavis/sd-data/projects/strateole2/C1/code/FLOATS_FileMaker/FLOATS.yaml'


config = {}

#CCMz parameters
config['ccmz_user']="myusername" # Your login on the CCMz
config['ccmz_pass']='mypassword' # Your password on the CCMz
config['local_target_dir']="/Users/sdavis/sd-data/projects/strateole2/C1/CCMZ_Mirror" # directory where to store mirrored data on your local machine


floatsc151= {}
FLOATS_csv_dir = "/Users/sdavis/sd-data/projects/strateole2/C1/ST2_C1_01_TTL5" # dir where to put processesed csv files 
floatsc151['singlescan_dir'] = FLOATS_csv_dir+"/Single_FTR"
floatsc151['FLOATS_log_file'] = FLOATS_csv_dir+"/FLOATS_Log.txt" #file to save log of XML messages
floatsc151['ftr_file_name'] = FLOATS_csv_dir+"/FLOATS_Raman_Master.csv"
floatsc151['HK_file_name'] = FLOATS_csv_dir+"/FLOATS_HK_Master.csv"
floatsc151['EFU_file_name'] = FLOATS_csv_dir+"/FLOATS_EFU_TSEN.csv"
floatsc151['EFU_HK_name'] = FLOATS_csv_dir+"/FLOATS_EFU_HK.csv"

floatsc151['flight_or_test']='Flight'
floatsc151['instrument'] = 'FLOATS'
floatsc151['FlightID'] = 'ST2_C1_01_TTL5'

# floatsc152= {}
# FLOATS_csv_dir = "/Users/sdavis/sd-data/projects/strateole2/C1/FLOATS_C1_52" # dir where to put processesed csv files 
# floatsc152['singlescan_dir'] = FLOATS_csv_dir+"/Single_FTR"
# floatsc152['FLOATS_log_file'] = FLOATS_csv_dir+"/FLOATS_Log.txt" #file to save log of XML messages
# floatsc152['ftr_file_name'] = FLOATS_csv_dir+"/FLOATS_Raman_Master.csv"
# floatsc152['HK_file_name'] = FLOATS_csv_dir+"/FLOATS_HK_Master.csv"
# floatsc152['EFU_file_name'] = FLOATS_csv_dir+"/FLOATS_EFU_TSEN.csv"
# floatsc152['EFU_HK_name'] = FLOATS_csv_dir+"/FLOATS_EFU_HK.csv"
# floatsc152['flight_or_test']='AIT'
# floatsc152['FlightID'] = 'ST2_C1_52_TTL5'

#FIpairs is a list of dictionaries containing information on a specific flight/instrument pairing
config['FIpairs'] = [floatsc151]

#Example of how to do two flight/instrument pairs
# config['FIpairs'] = [floatsc151,floatsc152]

with open(yamlfilename, 'w') as yamlfile:
    data = yaml.dump(config, yamlfile)
    print("Write successful")
    
#Here is an example of how to read in the configuration file that was just created
# with open(yamlfilename, "r") as yamlfile:
#     data2 = yaml.load(yamlfile, Loader=yaml.FullLoader)
#     print("Read successful")