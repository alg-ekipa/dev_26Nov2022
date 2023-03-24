from datetime import datetime

class DateTimeManager:    
    @classmethod
    def format_time(cls, event_date):
        d = datetime.strptime(event_date, '%Y.%m.%d %H:%M:%S')
        d_format = d.strftime('%d.%m.%Y %H:%M:%S')
        return d_format
    
    

    #def get_date(): 
    # def format_time(self, event_date):
    # d = datetime.strptime(event_date, '%d.%m.%Y %H:%M:%S')
    # d_format = d.strftime('%d.%m.%Y %H:%M:%S')
    # return d_format