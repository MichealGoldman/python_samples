"""
month picker simple case implementation in python
"""


class Case(object):
    """
    class to return a month
    """

    def what_month(self, num):
        """
        returns the month

        Arguments:
            num {int} -- month

        Returns:
            string -- month
        """

        method_name = "month_{}".format(num)
        method = getattr(self, method_name, lambda: "Invalid Input")
        return method()

    @staticmethod
    def month_1():
        '''
        jan
        '''
        return "January"

    @staticmethod
    def month_2():
        '''
        feb
        '''
        return "February"

    @staticmethod
    def month_3():
        '''
        mar
        '''
        return "March"

    @staticmethod
    def month_4():
        '''
        apr
        '''
        return "April"

    @staticmethod
    def month_5():
        '''
        may
        '''
        return "May"

    @staticmethod
    def month_6():
        '''
        jun
        '''
        return "June"

    @staticmethod
    def month_7():
        '''
        jul
        '''
        return "July"

    @staticmethod
    def month_8():
        '''
        aug
        '''
        return "August"

    @staticmethod
    def month_9():
        '''
        sep
        '''
        return "Setember"

    @staticmethod
    def month_10():
        '''
        oct
        '''
        return "October"

    @staticmethod
    def month_11():
        '''
        nov
        '''
        return "November"

    @staticmethod
    def month_12():
        '''
        dec
        '''
        return "December"


if __name__ == "__main__":
    MY_MONTH = Case()
    print(MY_MONTH.what_month(input("Please Enter the Month Number: ")))
