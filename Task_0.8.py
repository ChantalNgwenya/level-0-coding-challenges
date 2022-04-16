# Convert any number to hour/s and minute/s
# also handles plurals and singulars
def convert(sec):
    # 1 hour = 60 min

    hour = sec // 60
    sec %= 60
    # 1 min = 60 sec
    minutes = sec 
    
    print(hour, "hour/s", minutes, "minute/s")
    
sec = int(input("Enter the number: "))
convert(sec)
