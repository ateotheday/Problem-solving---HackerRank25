'''
Problem Statement – The principal has a problem with repetitions. Everytime someone sends the same email twice he becomes angry and starts yelling. His personal assistant filters the mails so that all the unique mails are sent only once, and if there is someone sending the same mail again and again, he deletes them. Write a program which will see the list of roll numbers of the student and find how many emails are to be deleted.

Sample Input:
6
1
3
3
4
3
3
Sample Output:
3

SOLUTION
Here, as you can see, we have to print the repeating elements.
One of the most optimal solution would be to use a set.
Add elements into the set if they are not already present otherwise, if the element exists in the set, increment a variable (here delete).
The delete variable now holds the count of elements that have to be deleted, as sets cannot contain  duplicate values.
'''


n=int(input())
rollist=set()
delete=0
for i in range(n):
    roll=int(input())
    if roll in rollist:
     delete+=1
    else:
        rollist.add(roll)
print(delete)