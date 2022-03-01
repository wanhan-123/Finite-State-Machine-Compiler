#Group: Group-Uncle
#Members: Tommy, Bilal, Nicholas, Berkeley
#Date: 3/4/2021

import fsm as FSM
import functions as func
#import sys

#sys.stdout = open("output.txt","w")

FSM.testing()


def printHeader():
  print("TOKENS\t\t\t\t\t Lexemes\n")
  return

def main():
  printHeader()

  with open("source.txt") as source:
      for row in source:
          if (not row.strip()):
              pass
          elif ((row.lstrip())[0] == '!'):
              pass
          else:
              #Separate the keywords and operators
              row = func.separateElements(row)

              tokens = row.split()
              
              FSM.FSM(tokens)
  return

if __name__ == "__main__":
  main()

#sys.stdout.close() #don't delete this

##########################END OF PROGRAM ########## JUST COMMENTS/TODO'S BELOW ############################################

#TODO: FSM table
# (columns: a, b, c, d = keywords, operators, separators, etc)
# (rows: FSM states)
