total_sec = input("please type the number of secends\n")
hours = int(total_sec) // 3600 
minutes =  (int(total_sec) % 3600) // 60
seconds = (int(total_sec) % 3600) % 60
print("This equals: " + str(hours) + " hours " + str(minutes) + " minutes " + str(seconds) +" seconds.")
