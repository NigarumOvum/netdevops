def textdemo(filename,msg):       
      path="/root/" 
      full_path=path + str(filename) + ".txt" 
      file = open(full_path,'w') 
      file.write(msg) 
      file.close() 
      print('success')

for i in range(1,11):
   textdemo(i,'OK')

