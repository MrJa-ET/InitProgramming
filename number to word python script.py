ef convert(num):
    units = ("", "አንድ", "ሁለት", "ሶስት", "አራት", "አምስት", "ስድስት", "ሰባት", "ስምንት", "ዘጠኝ", "", "አስራ")
    tens =("", "", " ሃያ ", " ሰላሳ ", " አርባ ", " ሃምሳ", " ስልሳ", " ሰባ", " ሰማንያ", "ዘጠና")
    
    if (num < 0):
        return "-"+convert(-num)

    if (num<20):
        return  units[num] 

    if (num<100):
        return  tens[num // 10]  +units[int(num % 10)] 

    if (num<1000):
        return units[num // 100]  +" መቶ " +convert(int(num % 100))

    if (num<1000000): 
        return  convert(num // 1000) + " ሺ " + convert(int(num % 1000))

    if (num < 1000000000):    
        return convert(num // 1000000) + " ሚሊዮን " + convert(int(num % 1000000))
    
    if (num < 1000000000000):
        return convert(num // 1000000000)+ " ቢሊዮን "+ convert(int(num % 1000000000))
    
    if (num < 1000000000000):
        return convert(num // 1000000000)+ " ቢሊዮን "+ convert(int(num % 1000000000))
        
    elif (num > 1000000000000):
        print("Only supports upto billion")

    else:
        print("Please Enter a valid input")

input=int(input("Please enter a number : "))
output = convert(input)
print(output)
