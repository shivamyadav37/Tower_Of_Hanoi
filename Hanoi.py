#Python Program for the Game Tower of Hanoi 
#Author --> Shivam Yadav
def Tower(n , source, dest, extra): 
    if n == 1: 
        print ("Move disk 1 from rod",source,"to rod",dest) 
        return
    Tower(n-1, source, extra, dest) 
    print ("Move disk",n,"from rod",source,"to rod",dest)
    Tower(n-1, extra, dest, source) 
          

n = int(input("Number Of Disks\n"))
TowerOf(n, 'A', 'C', 'B')  
