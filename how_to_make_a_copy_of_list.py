ld = ["ad","dsf","fsfas"]
lds = ld[:]  #copy using slicing
ld.append("ho")
print(f"{ld}\n{lds}")
ldsn = lds.copy() #copy using copy method
ld.remove("ad")
print(ld,"\n",ldsn)

#you cannot copy like "lds = ld" because list
#are mutable , here we are just making
# a new variable for same data. changing in ld will result in lds also.
