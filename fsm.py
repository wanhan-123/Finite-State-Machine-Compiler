
# Define keywords / separators / operators

SEPARATORS = ["(", ")", "{", "}", "[", "]", ",", ".", ":", ";"]
OPERATORS = ["*", "+", "-", "=", "/", ">", "<", "%"]
#DOUBLEOPERATORS = ['==', '++', '--', '+=', '-=', '>=', '&&', '||', '!=']
KEYWORDS = [
    "int", "float", "bool", "True", "False", "if", "else", "then", "endif",
    "endelse", "while", "whileend", "do", "enddo", "for", "endfor", "STDinput",
    "STDoutput", "and", "or", "not"
]

def testing():
  print("test")
  return



def id_FSM(token):
  if not token[0].isalpha:
    print("UNKNOWN\t\t\t\t=\t\t", token)
  else:
    id = ""
    for i in token:
      if i.isalpha or i == '_':
        id += i
    if id in KEYWORDS:
      print("KEYWORD\t\t\t\t=\t\t", id)
    else:
      print("IDENTIFER\t\t\t=\t\t", id)  
  return   

def num_FSM(token):  #goes till the end of the line and remembers the number
    #num = ""
  decimal = False
  one_decimal = False
  for i in token:
        if not i.isdigit():
          if i == "." and one_decimal == False:
            decimal = True
            one_decimal = True
          else:
            return print("UNKNOWN\t\t\t\t=\t\t", token)
            # break
  if decimal == False:
    print("INTEGER\t\t\t\t=\t\t", token)
  else:
    print("REAL\t\t\t\t=\t\t", token)
  return

def FSM(listofwords): #tokens are being split, doesn't register "2.0" as a full token, passes each char individually "2",".","0"
  for word in listofwords:
  #   print(word)
    if word in OPERATORS: 
      print("OPERATOR\t\t\t=\t\t", word)
    elif word[0].isdigit():
      num_FSM(word)
    elif word in SEPARATORS: 
      print("SEPARATOR\t\t\t=\t\t", word)
    else:
       id_FSM(word) #pass to function
       # same goes here...
    #   # i.e. we need to be able to identify "_"...
  return
