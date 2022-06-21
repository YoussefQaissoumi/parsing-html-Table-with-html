import csv
path="C:\\Users\\youqai9m\\Desktop\\intmetrics\\inMetrics.txt"

def extract_name(s):
   start=0 
   finish=0
   for i in range(1,len(s)-1):
      if s[i]==">" :
         start=i+1
      if  s[i]=="<" :
         finish=i-1
   return s[start:finish+1]


      


def test(path):
    j=0
    csv_data=[]
    l=[]
   #path of the csv file you want to display with aggrid

    with open(path, 'r') as file_obj:
      reader_obj = csv.reader(file_obj)
      for i in reader_obj:
         #filling csv_data with all csv data (row by row)
         csv_data.append(i)
         if "</tr>" in i[0]:
            #csv_data.append([])
            #j=j+1
            if ("int" in csv_data[4][0]) or ("float" in csv_data[4][0]):
               a=csv_data[2][0]
               s=extract_name(a)
               
               l.append(s)
            if ("int" in csv_data[3][0]) or ("float" in csv_data[3][0]):
               a=csv_data[1][0]
               s=extract_name(a)
               
               l.append(s)
            csv_data=[]



    return l

    
a=test(path)
print(a)
print(len(a))
b="   </td>"
if "<d" in b:
    print("yes hh")