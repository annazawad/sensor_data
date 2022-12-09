from load_data import load_sensor_data
from house_info import HouseInfo
from datetime import date, datetime
from temperature_info import TemperatureData
from humidity_info import HumidityData
from statistics import mean
from particle_count_info import ParticleData
from energy_info import EnergyData

data = []
print('Sensor Data App')

data = load_sensor_data()
print('Loaded records: {}'.format(len(data)))


house_info = HouseInfo(data)
test_area = 1
recs = house_info.get_data_by_area("id",rec_area=test_area)
print(f'House sensor records for area {test_area} = {len(recs)}')

test_date = datetime(2020,5,9)
recs = house_info.get_data_by_date('id',rec_date=test_date)
print('House sensor records for date {} = {}'.format(datetime.strftime(test_date,'%m/%d/%y'),len(recs)))

temperature_data = TemperatureData(data)
recs = temperature_data.get_data_by_area(rec_area=test_area)
print(f'\n House Temperature sensor records for area {test_area} = {len(recs)}')
print('\t Maximum: {0}, Minimum: {1}'.format(max(recs),min(recs)))

recs = temperature_data.get_data_by_date(rec_date=test_date)
print('House sensor Temperature records for date {} = {}'.format(datetime.strftime(test_date,'%m/%d/%y'),len(recs)))
print('\t Maximum: {0}, Minimum: {1}'.format(max(recs),min(recs)))

humidity_data = HumidityData(data)
recs = humidity_data.get_data_by_area(rec_area=test_area)
print(f'\n House Humidity sensor records for area {test_area} = {len(recs)}')
print('\t Maximum: {0}, Minimum: {1}, Average: {2}'.format(max(recs),min(recs), mean(recs)))

recs = humidity_data.get_data_by_date(rec_date=test_date)
print('House sensor Humidity records for date {} = {}'.format(datetime.strftime(test_date,'%m/%d/%y'),len(recs)))
print('\t Maximum: {0}, Minimum: {1}, Average: {2}'.format(max(recs),min(recs), mean(recs)))

particle_data = ParticleData(data)
recs = particle_data.get_data_by_area(rec_area=test_area)
print("\n House Particle sensor records for area {} = {}".format(test_area, len(recs)))

concentration = particle_data.get_data_contrentation(recs)
print("\tGood Air Quality Recs: {}".format(concentration["good"]))
print("\tModerate Air Quality Recs: {}".format(concentration["moderate"]))
print("\tBad Air Quality Recs: {}".format(concentration["bad"]))

recs = particle_data.get_data_by_date(rec_date=test_date)
print("\nHouse Particle sensor records for date: {} = {}".format( test_date.strftime("%m/%d/%y"), len(recs)))

concentration = particle_data.get_data_contrentation(recs)
print("\tGood Air Quality Recs: {}".format(concentration["good"]))
print("\tModerate Air Quality Recs: {}".format(concentration["moderate"]))
print("\tBad Air Quality Recs: {}".format(concentration["bad"]))

energy_data = EnergyData(data)
recs = energy_data.get_data_by_area(rec_area=test_area)
print("\nHouse Energy sensor records for area {} = {}".format(test_area, len(recs)))

total_energy = energy_data.calculate_energy_usage(recs)
print("\tEnergy Usage: {:2.2} Watts".format(total_energy))

recs= energy_data.get_data_by_date(rec_date=test_date)
print("House Energy sensor records for date: {} = {}".format(test_date.strftime("%m/%d/%y"), len(recs)))
total_energy = energy_data.calculate_energy_usage(recs)
print("\tEnergy Usage: {:2.2} Watts".format(total_energy))

