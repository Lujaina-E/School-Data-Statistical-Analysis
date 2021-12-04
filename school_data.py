# school_data.py
# LUJAINA ELDELEBSHANY, ENDG 233 F21
# A terminal-based application to process and plot data based on given user input and provided csv files.
# You may only import numpy, matplotlib, and math. 
# No other modules may be imported. Only built-in functions that support compound data structures, user entry, or casting may be used.
# Remember to include docstrings for any functions/classes, and comments throughout your code.

import numpy as np
import matplotlib.pyplot as plt

class School:
    """A class used to create a School object.

        Attributes:
            name (str): String that represents the school's name
            code (int): Integer that represents the school's code
    """

    #constructor
    def __init__(self, name, code):
        self.name = name 
        self.code = code

    def print_all_stats(self):
        """A function that prints the name and code of the school instance.
        Parameters: None
        Return: None
        """
        print("School Name: {0}, School Code: {1}".format(self.name, self.code))

# Data imports
data19 = np.genfromtxt('SchoolData_2018-2019.csv', delimiter="," , skip_header=True)
data20 = np.genfromtxt('SchoolData_2019-2020.csv', delimiter="," , skip_header=True)
data21 = np.genfromtxt('SchoolData_2020-2021.csv', delimiter="," , skip_header=True)

#list of searchable school codes or names  
school_name_list = ['Centennial High School', 'Robert Thirsk School', 'Louise Dean School', 'Queen Elizabeth High School', 'Forest Lawn High School', 'Crescent Heights High School', 'Western Canada High School', 'Central Memorial High School', 'James Fowler High School', 'Ernest Manning High School', 'William Aberhart High School','National Sport School','Henry Wise Wood High School','Bowness High School','Lord Beaverbrook High School','Jack James High School','Sir Winston Churchill High School','Dr. E. P. Scarlett High School','John G Diefenbaker High School', 'Lester B. Pearson High School']
school_code_list = [1224,1679,9626,9806,9813,9815,9816,9823,9825,9826,9829,9830,9836,9847,9850,9856,9857,9858,9860,9865]
#dictionaries linking school codes to names, vice versa
school_name_code_dict = {school_name_list[i]: school_code_list[i] for i in range(len(school_code_list))} 
school_code_name_dict = {school_code_list[i]: school_name_list[i] for i in range(len(school_code_list))} 

# Add your code within the main function. A docstring is not required for this function.
def main():
    reference_code = ''
    reference_name = ''

    #printing array data
    print("ENDG 233 School Enrollment Statistics\n")
    print('Array data for 2020 - 2021')
    print(data21)
    print('\n')

    print('Array data for 2019 - 2020')
    print(data20)
    print('\n')

    print('Array data for 2018 - 2019')
    print(data19)

    # Request for user input
    user_search_input = input('Please enter the high school name or school code: ')
    
    #invalid entry check for numerical input
    if user_search_input.isdigit():
        while int(user_search_input) not in school_code_list :
            print("Your must enter a valid school name or code.")
            user_search_input = input('Please enter the high school name or school code: ')
    
    #invalid entry check for alphabetical input
    else:
        while (user_search_input not in school_name_list):
            print("Your must enter a valid school name or code.")
            user_search_input = input('Please enter the high school name or school code: ')
    
    #if user input is school name, find code
    if user_search_input in school_name_list:
        reference_name = user_search_input
        reference_code = school_name_code_dict[user_search_input]

    #if user input is school code, find name
    else:
        reference_code = int(user_search_input)
        reference_name = school_code_name_dict[int(user_search_input)]

    # Print school name and code using School class
    searched_school = School(reference_name, reference_code)
    searched_school.print_all_stats() 
    
    print("\n***Requested School Statistics***\n")

    #variable initialization
    average_enroll_g10 = 0
    average_enroll_g11 = 0
    average_enroll_g12 = 0
    totalgraduates_3years = 0
    g10_19 = 0
    g10_20 = 0
    g10_21 = 0
    g11_19 = 0
    g11_20 = 0
    g11_21 = 0
    g12_19 = 0
    g12_20 = 0
    g12_21 = 0
    #localizes each grade's enrollment data for each year into variables, then calculates
    #average enrollments for each grade and graduates for the 3 years
    for i in range(len(school_code_list)):
        if data19[i][0] == reference_code:
            g10_19 = data19[i][1]
            g10_20 = data20[i][1]
            g10_21 = data21[i][1]
            g11_19 = data19[i][2]
            g11_20 = data20[i][2]
            g11_21 = data21[i][2]
            g12_19 = data19[i][3]
            g12_20 = data20[i][3]
            g12_21 = data21[i][3]
            average_enroll_g10 = (g10_19 + g10_20 + g10_21) // 3
            average_enroll_g11 = (g11_19 + g11_20 + g11_21) // 3
            average_enroll_g12 = (g12_19 + g12_20 + g12_21) // 3
            totalgraduates_3years = g12_19 + g12_20 + g12_21
            break

    #printing values calculated above
    print('School name: ' + reference_name + ', School Code: ' + str(reference_code))
    print('Mean enrollment for Grade 10: ' + str(int(average_enroll_g10)))
    print('Mean enrollment for Grade 11: ' + str(int(average_enroll_g11)))
    print('Mean enrollment for Grade 12: ' + str(int(average_enroll_g12)))
    print('Total number of students who graduated from 2019-2021: ' + str(int(totalgraduates_3years)))
   
    # Add data processing and plotting here
    #plotting scatter plot
    plt.scatter([10,11,12], [g10_21, g11_21, g12_21],c = 'blue', label = '2021 Enrollment')
    plt.scatter([10,11,12], [g10_20, g11_20, g12_20], c = 'green', label = '2020 Enrollment')
    plt.scatter([10,11,12], [g10_19, g11_19, g12_19], c = 'red', label = '2019 Enrollment')
    #scatter plot axes titles and format
    plt.title('Grade Enrollment by Year')
    plt.xlabel('Grade Level')
    plt.ylabel('Number of Students')
    plt.xticks([10,11,12])
    plt.legend(shadow = True, loc='upper left')
    plt.show()

    #Annual plotting by grade 
    fig, axs = plt.subplots(3)
    fig.suptitle('Enrollment by Grade')
    years = [2019, 2020, 2021]
    #top subplot
    axs[0].plot(years, [g10_19, g10_20, g10_21], c = 'yellow', linestyle='dashed', label = 'Grade 10')
    axs[0].set_ylabel('Number of Students')
    axs[0].legend(shadow = True, loc ='upper right')
    axs[0].set_xticks(years)

    #middle subplot
    axs[1].plot(years, [g11_19, g11_20, g11_21], c = 'magenta', linestyle = 'dashed', label = 'Grade 11')
    axs[1].set_ylabel('Number of Students')    
    axs[1].legend(shadow = True, loc ='upper right')
    axs[1].set_xticks(years)

    #bottom subplot
    axs[2].plot(years, [g12_19, g12_20, g12_21], c = 'cyan', linestyle = 'dashed', label = 'Grade 12')
    axs[2].set_ylabel('Number of Students')
    axs[2].legend(shadow = True, loc ='upper right')
    axs[2].set_xticks(years)

    #total figure labels
    plt.xlabel('Enrollment Year')
    plt.show()

# Do not modify the code below
if __name__ == '__main__':
    main()