
#read any file
f = open("hello.txt"); #by default read mode "r"
data = f.read();
print(data);
f.close();

#write any file
str = "i am a good boy";
s = open("myfile.txt", "w");   #automatically create file 
s.write(str);  #and write the content
s.close();

#read line by line
readFile = open("hello.txt");
lines = readFile.readlines(); #return a list
print(lines, type(lines));
readFile.close();