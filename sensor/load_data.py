import os
import glob
import csv

def load_sensor_data():
    sensor_data=[]
    path = 'C:/Users/AZAWADA/OneDrive - Capgemini/Desktop/python_projects/sensor_data/sensor'
    sensor_files = glob.glob(os.path.join(path,'datasets','*.csv'))

    for sensor_file in sensor_files:
        with open(sensor_file) as data_file:
            data_reader = csv.DictReader(data_file,delimiter=',')
            for row in data_reader:
                sensor_data.append(row)

    return sensor_data

