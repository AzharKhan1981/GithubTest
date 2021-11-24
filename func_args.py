'''def user_info(name, age, city):
    #This function prints name, age, and city from an argument provided to the function.
    print("{} is {} year old, from {}" .format(name, age, city) )
user_info(40, "Lahore")
'''


'''def user_info(name, age=0, city="Pindi"):

    print("{} is {} year old, from {}" .format(name, age, city) )

user_info("Azhar")
user_info(45, "kami")'''

# *args and **kwargs

def application(fname, lname, email, company, *args, **kwargs):
    print("{} {} weorks at {}. His email is {}.".format(fname,lname,company,email))

application("Azhar", "Khan", "mazhar@powersoft19.com", 5000, hire_date = "May 2006")


