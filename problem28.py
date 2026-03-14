# WAF that replaces all occurances of ananya with priyanshi in ananya.txt file 

with open("ananya.txt", "r")as f:
    data = f.read()

new_data= data.replace("ananya", "priyanshi")
print(new_data)

with open("ananya.txt", "w" )as f:
    f.write(new_data)