#!/bin/bash
#set a job name  
#SBATCH --job-name=timer25
#################
#a file for job output, you can check job progress
#SBATCH --output=timer25.out
#################
# a file for errors from the job
#SBATCH --error=timer25.err
#################
#time you think you need; default is one day
#in minutes in this case, hh:mm:ss
#SBATCH --time=24:00:00
#################
#number of tasks you are requesting, N for all cores
#SBATCH -n 25
#################
#partition to use
#SBATCH --partition=ser-par-10g-4
#################
#number of nodes to distribute n tasks across
#################

python inceptionV3_script.py