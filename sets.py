# accesing an element in sets 
s={15,3,5,6,7,8,9,10,11,12}
print (s)


# how to acces sets element through for loop 
for i in s:
    print (i)

# basci sets opetatoins 
#  add 
s={15,3,5,6,7,8,9,10,11,12}
s.add(101)
print (s)

#  lenth
s={15,3,5,6,7,8,9,10,11,12}
len = len(s)
print (len)

# Max 
s={15,3,5,6,7,8,9,10,11,12,101}
max = max(s)
print (max)

#  min 
s={15,3,5,6,7,8,9,10,11,12}
min = min(s)
print(min)

# all (return true if all element in set s)
s={15,3,5,6,7,8,9,10,11,12}
print(all(s))


#  update (create a new set s )
s={15,3,'d','f','g'}
t={'a','s','d',1,2,5,}
s.update(t)
print (s)


#  remove (it returns error if elment is not found)
s={15,3,'d','f','g'}
t={'a','s','d',1,2,5,}
s.remove(15)
t.remove('d')
print (s)
print(t)

# discard (is not give an error)
s={15,3,'d','f','g'}
t={'a','s','d',1,2,5,}
s.discard(15)
t.discard('k')
print(s)

# clear (it clear data not set )
s={15,3,'d','f','g'}
s.clear()
print (s)

# copy (it copy data)
s={15,3,'d','f','g'}
t=s.copy()
print (t)

# delete (it delete set )
# s={15,3,'d','f','g'}
# s.delete()
# pritn (s)

# issubset if first set elemnent have in second set 
s={'a','s','d'}
t={'a','s','d',1,2,5,} 
print(s.issubset(t))

# issupperset if all element have in both  set
s={15,3,'d','f','g'}
t={'a','s','d',1,2,5,}
print(s.issuperset(t))


