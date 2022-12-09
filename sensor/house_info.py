from datetime import datetime,date

class HouseInfo:
    def __init__(self,data):
        self.data = data

    def get_data_by_area(self, field,rec_area=0):
        self.field = field
        self.rec_area=rec_area
        field_data = list()
        for record in self.data: #this is list of dictionaries
            if rec_area == 0:
                field_data.append(record[field]) #values for key=field (column)
            elif rec_area == int(record['area']):
                field_data.append(record[field])
        return field_data

    def get_data_by_date(self,field, rec_date = datetime.now()):
        field_data = list()
        for record in self.data:
            if rec_date.strftime('%m/%d/%y') == record['date']:
                field_data.append(record[field])
        return field_data