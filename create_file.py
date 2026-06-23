# from the help of the function we can create or over write a file.
#r = open("Demofile.txt",'w')   #create the demo file
r = open("Demofile.txt",'a') # it append the new line
r.write("Hello I'm Rahul and I'm writing inside the demo file") #This string automatically add this on the txt file
r.write("Now I append new line in the txt file")
r.close() # always close the file

# now if I write something inside the file 'w' overwrite the line
# For that reason we use 'a' append 