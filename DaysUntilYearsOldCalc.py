import datetime
from datetime import timedelta


class DaysUntil:
    def __init__(self, years_old, bday):
        """
        Calcuates the days until you turn a certain age.
        Args:
            years_old: Integer number of years old used to calculate the days until
            bday: Array of three integers, birthday month, birthday day, birthday year

        Attributes:
            self.years = Target year, set by self.caclulate method
            self.timedelta = Days from today until target year self.calculate method
        """

        self.years_old = years_old
        self.bday_month, self.bday_day, self.bday_year = bday
        self.years = None
        self.timedelta = None


    def calculate(self, show=True):
        """
        Runs the calculation and prints the output
        Args:
            show: boolean flag whether to print the output
        """

        today = datetime.datetime.today()
        self.years = datetime.datetime(self.years_old + self.bday_year, self.bday_month, self.bday_day)
        self.timedelta = years - today

        if show:
            print('Target year: ', self.years)
            print('Days until: ', self.timedelta)


if __name__ == '__main__':
    yo = int(input('Target age: '))
    bd = [int(d) for d in input('Date of birth mm/dd/yyyy: ').split('/')]
    
    d = DaysUntil(yo, bd)
    d.calculate()
