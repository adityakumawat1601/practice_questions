class Time:
    "class Time takes 24 hour input . it  adds and display time"
    def __init__(self,hours:int,minutes:int):
        try:
            if hours>23 or minutes>59:
                raise ValueError
        except ValueError:
                print("invalid hour or minutes given try again with valid time.")
        else:
            self.hours = hours
            self.minutes = minutes
    def add_time(self,other1,other2):
        total = [other1.hours+other2.hours,other1.minutes+other2.minutes]
        return f"{total[0]} hour and {total[1]} min"
    def display_time(self):
        return f"current time is {self.hours} hour and {self.minutes} min"
    def display_minutes(self):
        total_min = self.hours*60+self.minutes
        return f"{total_min} minutes"
    def __str__(self):
        print(f"Time({self.hour}h{self.min}m) ")
    #def __del__(self):
    #    print(f"deleting {self.hours}h and {self.minutes}m ......")
    #    del self
    

    
if __name__ == "__main__":
    hour,minute = int(input()),int((input()))
    t1 = Time(23,8)
    t2 = Time(5,45)
    t3 = Time(hour,minute)
    print(t3.add_time(t1,t2))
    print(t3.display_minutes())
    print(t3.display_time()) 


