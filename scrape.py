# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pdx_job_scrape as gs 
import pandas as pd 

path = "C:/Users/aaron/Documents/GitHub/chromedriver"

df = gs.get_jobs(265, False, path, 15)

df.to_csv('glassdoor.csv')
