#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 09:25:56 2019

@author: salim
"""

from datetime import datetime
from datetime import timedelta
import airflow
import requests
import json
import pysftp
import  time;

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator


default_args = {

	#1. Put your name
    'owner': 'Salim', 
    'retries': 1,
	'start_date': datetime(2019, 10, 19, 7, 00, 00, 000000),
    'retry_delay': timedelta(minutes=5),
}

def download_json_comments():

	#2. Get comments from jsonplaceholder.typicode.com using a REST Call
    req = requests.get("http://jsonplaceholder.typicode.com/comments?postId=1")
    print(req.json())

	#3. Add your name as a Sufix of file name 
    with open("Salim.json", 'w') as json_file:
        json.dump(req.json(), json_file)		
		
        print("Successfully writted on Salim.json")
	


def upload_sftp():

#4. Create a pysftp connection with host="35.223.130.234", username="edemExercise3", password="edemExercise3",cnopts = cnopts


    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None

    srv = pysftp.Connection(host="35.223.130.234", username="edemExercise3", password= "edemExercise3", cnopts = cnopts)
    
    json_remote_file = "Salim."+str(time.time())+".json"


    srv.put('/Users/salim/Desktop/EDEM/Python/Code/Salim.json','/home/edemExercise3/Upload/Salim/'+ json_remote_file)

    srv.close()




#6. Add your name to the DAG name below
with DAG('airflow_sftp_Salim', default_args=default_args, schedule_interval='*/3 * * * *',) as dag:

	
	download_json_task = PythonOperator(task_id='Get_comments', python_callable=download_json_comments)
	
	print_json_ok = BashOperator(task_id='Download_check', bash_command='echo "Json comments file downloaded successfully"')

	upload_json_sftp_task = PythonOperator(task_id='Upload_comments_sftp', python_callable=upload_sftp)
	
	print_upload_ok = BashOperator(task_id='Upload_check', bash_command='echo "Json comments file uploaded successfully"')


#7. Create worflow DAG with following sequence: download_json_task, print_json_ok, upload_json_sftp_task, print_upload_ok
