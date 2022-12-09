from house_info import HouseInfo
from datetime import date

class EnergyData(HouseInfo):

    ENERGY_PER_BULB = 0.2
    ENERGY_BITS = 0x0F0

    """def __get_energy(self,rec):
        energy = int(rec, base=16)
        z = energy << 4 and energy >>4
        return z"""

    def __get_energy(self, rec):
        energy = int(rec, base=16)
        energy = energy & self.ENERGY_BITS  # mask ENERGY bits
        energy = energy >> 4  # shift right
        return energy


    def __convert_data(self,data):
        recs = []
        for rec in data:
            recs.append(self.__get_energy(rec))
        return recs

    def get_data_by_area(self, rec_area=0):
        recs = super().get_data_by_area("energy_usage", rec_area)
        return self.__convert_data(recs)

    def get_data_by_date(self, rec_date=date.today()):
        recs = super().get_data_by_date("energy_usage", rec_date)
        return self.__convert_data(recs)

    def calculate_energy_usage(self,data):
        total_energy = sum([x * self.ENERGY_PER_BULB for x in data])
        return total_energy