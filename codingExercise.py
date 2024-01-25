
#Triangular numbers generator
def triangular_number(n):
    return (n * (n + 1)) // 2

def generate_triangular_numbers(count):
    return [triangular_number(i) for i in range(1, count + 1)] 

triangularNumb = generate_triangular_numbers(100)
strNumb = [str(x) for x in triangularNumb]


#Define File Path
filePath = 'coding_qual_input.txt' 

#Decode Function
def decode(message_file):
    try:
     with open(filePath, 'r') as file:
       dictionary = {}
          
       for line in file:
           #Get First Numbers in File
           num = line.split(' ',1)[0]
           if num in strNumb:
              dictionary[int(num)]=line[len(num):-1] 
       
       sortedDictionary = sorted(dictionary)
            
       for key in sortedDictionary:
                print(dictionary[key], end='')

    except FileNotFoundError:
        print(f"File not found: {filePath}")
    except Exception as e:
        print(f"An error ocurred: {e}")


#Calling function
decode(filePath)