#print("I\'m a student")
# print('I\'m a student')

#print("He said \"I'm fine!\"")
# print('He said "I\'m fine"')

#print('He said "T\'m fine!"')
# print('Happy? \o__o/' )

#tripple double quotes, or HEREDOC
# print("""
# One botton on the table
#     I am fine
#         Two bottles on the table
#             I am cry""")
#
# s = "Student"
# print("charactor is order 3: ",s[3])
#
# name = "Nitipat C"
# medication1 = "Ciprofoxasin"
# medication2 = "Paracetamol"
# timing = "bid"
#
# """
# Mediacation for Nitipat C
# Ciprofoxasin : per Oral
# Timing : bid
# """

# print("""
# Medication for {name}
# 1   {medication1}   : per Oral
#     Timimg         : {timing}
#
# 2   {medication2}   : per Oral
#     Timing        : {timing}
# """.format(name = "Nitipat C", medication1 = "Ciprofoxasin",medication2 = "Paracetamol", timing = "bid"))

# print(f"""
# Medication for {name}
# 1   {medication1}   :per Oral
#     Timimg        : {timing}
#
# 2   {medication2}   : per Oral
#     Timing        : {timing}
# """)

input_data = input("Enter some data: ")
print("Hello, " + input_data.upper())