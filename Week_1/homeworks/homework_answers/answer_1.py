# Data types
# string -> Holds textual expressions.
# int -> Holds integer numbers.
# float -> Holds decimal numbers.
# list -> We use it to hold multiple data. It can be used with other data types
# bool -> Holds True (1) or False (0).


# Sampling Application: Login to a government-supported application
# (E-Government/E-Government)

sys_identification_number = "12345678902"
sys_password = "12345"
is_authenticated = False


id_input = input("Please Write Your Identification Number: ")
password_input = input("Please Write Your Password: ")

if id_input == sys_identification_number and password_input == sys_password:
    print("Login Process Successful")
    isAuthenticated = True
else:
    print("Login Failed!")
    isAuthenticated = False

if isAuthenticated:
    print("You can view your registered courses.")
else:
    print("You are not authorized to view this screen!")
