nums=[1,2,2,3,4,3,5,1]
#unique_nums=list(set(nums))
#print(unique_nums)
unique_nums = []
# Find duplicates
for n in nums :
    if n not in unique_nums :
        unique_nums.append(n)
print(unique_nums)

