#Input Format
#The first line contains an integer, n, denoting the number of commands.
#Each line i of the n subsequent lines contains one of the commands described above.

#Constraints
#The elements added to the list must be integers.

#Output Format
#For each command of type print, print the list on a new line.

lst=[]
n = int(input())
for i in range (n) :
    cmd=input().split()
    if cmd[0]=='insert' :
        lst.insert(int(cmd[1]), int(cmd[2]))
    elif cmd[0]=='print' :
        print(lst)
    elif cmd[0]=='remove' :
        lst.remove(int(cmd[1]))
    elif cmd[0]=='append' :
        lst.append(int(cmd[1]))
    elif cmd[0]=='sort' :
        lst.sort()
    elif cmd[0]=='pop' :
        lst.pop()
    else :
        lst.reverse()
