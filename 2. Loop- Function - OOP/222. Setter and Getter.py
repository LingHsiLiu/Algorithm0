# 222. Setter and Getter
# Implement a class School, including the following attributes and methods:

# A private attribute name of type string.
# A setter method setName which expect a parameter name of type string.
# A getter method getName which expect no parameter and return the name of the school.

class School:
    '''
     * Declare a setter method `setName` which expect a parameter *name*.
    '''
    # write your code here
    def __init__(self):
        self.__name = ''
        
    def setName(self, name):
        self.__name = name

    '''
     * Declare a getter method `getName` which expect no parameter and return
     * the name of this school
    '''
    # write your code here
    def getName(self):
        return self.__name
