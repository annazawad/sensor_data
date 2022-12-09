from house_info import HouseInfo
from datetime import datetime,date

class TemperatureData(HouseInfo):

    def __convert_data(self,data):
        recs=list()
        for rec in data:
            recs.append(int(rec, base=10))
        return recs

    def get_data_by_area(self,rec_area=0):
        recs = super().get_data_by_area('temperature',rec_area)
        #super().get_data_by_area('temperature',rec_area)
        return self.__convert_data(recs)

    def get_data_by_date(self,rec_date = datetime.now()):
        recs = super().get_data_by_date('temperature',rec_date)
        #super().get_data_by_date('temperature', rec_date)
        return self.__convert_data(recs)
