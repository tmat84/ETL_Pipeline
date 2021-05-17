[![Build Status](https://travis-ci.com/tmat84/ETL_Pipeline.svg?branch=main)](https://travis-ci.com/tmat84/ETL_Pipeline)
[![codecov](https://codecov.io/gh/tmat84/ETL_Pipeline/branch/main/graph/badge.svg)](https://codecov.io/gh/tmat84/ETL_Pipeline)

The small ETL project inspired by [Karolina Sowinska](https://www.youtube.com/channel/UCAxnMry1lETl47xQWABvH7g)

This is a simple data pipeline that downloads holiday data from https://calendarific.com website on a defined month and country and saves that data in a postgress database.

The pipeline will be scheduled to run monthly using Airflow.

The postgreDB and Airflow are installed locally using docker.
 
Generate your access token here: https://calendarific.com  
Set up postgres database using docker here: https://www.youtube.com/watch?v=aHbE3pTyG-Q&t=177s  
Set network for postgres inside docker here: https://www.youtube.com/watch?v=lNsJRM9ga-s&t=750s  
Set airflow using docker here: https://www.youtube.com/watch?v=aTaytcxy2Ck
