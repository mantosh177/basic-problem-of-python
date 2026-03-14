# ques - WAF to find in which line of the file does the word "learning " occur in the first

def check_for_line():
    word= "learning "
    data= True 
    Line_no=0
    with open("ananya.txt ","r")as f :
        while data:
            data=f.readline()
            if(word in data):
                print(Line_no)
                return
            Line_no +=1
    return -1   
check_for_line()