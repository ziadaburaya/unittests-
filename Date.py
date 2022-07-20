from datetime import timedelta

class Date:
    def __init__(self,day:int,month:int,year:int):
            self._year = year
            self._month = month
            self._day=day
    def check(self):
        """
        :return: 0 if the date not valid and  non if this valid
        """
        date = self._year, self._month, self._day
        if len(date) == 3 and self:
            if self._year < 1000 or self._year > 9999:
                return 0

            elif self._month <= 0 or self._month > 12:
                return 0

            elif self._month == 1 or self._month == 3 or self._month == 5 or self._month == 7 or self._month == 8 or self._month == 10 or self._month == 12:
                if self._day <= 0 or self._day > 31:
                    return 0
            elif self._month == 4 or self._month == 6 or self._month == 9 or self._month == 10:
                if self._day <= 0 or self._day > 30:
                    return 0
            elif self._month == 2:
                if self._year % 4 == 0:
                    if self._day <= 0 or self._day > 29:
                        return 0
                else:
                    if self._day <= 0 or self._day > 28:
                        return 0




    def isvalid(self):
      valid=self.check()
      if valid==0:
          return "is not valid date"
      else: return "is  valid date "
    def getNextDay(self):
        """
        :return: the next date if the date valid, if not valid return TypeError
        """
        if self.check()!=0:
            if self._month==12 and self._day==31:
             self._year=self._year+1
             self._month = 1
             self._day=0
            if self._month==12 and self._day<31:
                self._day=self._day+1
            next=1
            if self._month == 1 or self._month == 3 or self._month == 5 or self._month == 7 or self._month == 8 or self._month == 10 :
                if self._day==31:
                   self._month=self._month+next
                   self._day=next
                else: self._day=self._day+next
            if self._month == 4 or self._month == 6 or self._month == 9 or self._month == 11:
                if self._day == 30:
                    self._day = next
                    self._month=self._month+next
                else:
                    self._day = self._day + next
            if self._month == 2:
                if self._year % 4 == 0:
                    if  self._day == 29:
                        self._month = self._month + next
                        self._day = next
                    else:
                       self._day = self._day + next
                else:
                    if self._day==28:
                        self._day = next
                        self._month = self._month + next
                    else:
                        self._day = self._day + next
            return ("the next date is :",Date.__str__(self))
        else: raise TypeError( " can't to get next date ")
    def getNextDays(self,daysToAdd) :
        if self.check() != 0:
            dif= self._day+daysToAdd
            if self._month == 12 and self._day == 31:
                self._year = self._year + 1
                self._month = 1
                self._day = 0
            if self._month == 12 and self._day < 31:
                if dif>31:
                 self._year = self._year + 1
                 self._month = 1
                 self._day = 0+ daysToAdd
            if self._month == 1 or self._month == 3 or self._month == 5 or self._month == 7 or self._month == 8 or self._month == 10:
                if self._day == 31:
                    self._month = self._month + 1
                    self._day = 0+daysToAdd
                else:
                    self._day = self._day + daysToAdd
            if self._month == 4 or self._month == 6 or self._month == 9 or self._month == 11:
                if self._day == 30:
                    self._month = self._month + 1
                    self._day = 0 + daysToAdd
                else:
                    self._day = self._day + daysToAdd
            if self._month == 2:
                if self._year % 4 == 0:
                    if self._day == 29:
                        self._month = self._month + 1
                        self._day = 0+daysToAdd
                    else:
                        self._day = self._day + daysToAdd
                else:
                    if self._day == 28:
                        self._day = 0+daysToAdd
                        self._month = self._month + 1
                    else:
                        self._day = self._day + daysToAdd
            return ( Date.__str__(self))
    def __eq__(self, sdate):
        if sdate._year==self._year and sdate._month==self._month and sdate._day==self._day:
            return True
        else: return False
    def it(self,sdate):
        if sdate._year==self._year and sdate._month==self._month:
            if sdate._day>self._day:
                return sdate._day,sdate._month,sdate._year," true "
        elif sdate._year==self._year :
            if sdate._month > self._month:
                return sdate._day,sdate._month,sdate._year," true"
        elif sdate._year>self._year:
            return sdate._day,sdate._month,sdate._year," true "
        else:return  self._day, self._month, self._year,"false"

    def __gt__(self, sdate):
        if sdate._year == self._year and sdate._month == self._month:
            if sdate._day < self._day:
                return sdate._day, sdate._month, sdate._year, " true "
        elif sdate._year == self._year:
            if sdate._month < self._month:
                return sdate._day, sdate._month, sdate._year, " true"
        elif sdate._year < self._year:
            return sdate._day, sdate._month, sdate._year, " true "
        else:
            return self._day, self._month, self._year, "false"

    def __sub__(self, sdate):
        if sdate._year == self._year and sdate._month == self._month:
            if sdate._day > self._day:
                return sdate._day-self._day
            else:self._day-sdate._day
        elif sdate._year == self._year:
            if sdate._month > self._month :
                sub_month = (sdate._month - self._month) * 30
                if sdate._day> self._day:
                 sub_day=(sdate._day-self._day)
                else: sub_day=(self._day-sdate._day)
                return sub_day + sub_month
            else:
                sub_month = (self._month - sdate._month) * 30
                if sdate._day> self._day:
                     sub_day=(sdate._day-self._day)
                else: sub_day=(self._day-sdate._day)
                return sub_day + sub_month

        elif sdate._year > self._year:
            sup_year=(sdate._year-self._year)*365
            if sdate._month > self._month:
                sub_month = (sdate._month - self._month) * 30
                if sdate._day > self._day:
                    sub_day = (sdate._day - self._day)
                else:
                    sub_day = (self._day - sdate._day)
                    return sub_day + sub_month+ sup_year
            else:
                sub_month = (self._month - sdate._month) * 30
                if sdate._day > self._day:
                    sub_day = (sdate._day - self._day)
                else:
                 sub_day = (self._day - sdate._day)
                return sub_day + sub_month+ sup_year

        else:
            sup_year = (self._year - sdate._year) * 365
            sub_month = (self._month - sdate._month) * 30
            if sdate._month > self._month:
                sub_month = (sdate._month - self._month) * 30
                if sdate._day > self._day:
                    sub_day = (sdate._day - self._day)
                else:
                    sub_day = (self._day - sdate._day)
                    return sub_day + sub_month + sup_year
            else:
                sub_month = (self._month - sdate._month) * 30
                if sdate._day > self._day:
                    sub_day = (sdate._day - self._day)
                else:
                    sub_day = (self._day - sdate._day)
                return sub_day + sub_month + sup_year





    def __str__(self):
        the_date= self._day,self._month,self._year
        return f"{the_date}"






d1=Date(5,12,2020)
d2=Date(15,12,2023)
print(d1.getNextDay())
print("if",d1 ,"equals",d2)
print(d1.__eq__(d2))
print("if",d2,"biger than",d1)
print(d1.it(d2))
print("if",d2,"smallest than",d1)
print(d1.__gt__(d2))
print("the difference days")
print(d1.__sub__(d2))



