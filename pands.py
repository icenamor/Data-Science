# Add sharemen column

recent_grads['sharemen'] = (recent_grads['men'] / recent_grads['total'])


# Find the maximum percentage value of men
max_men = np.max(recent_grads['sharemen'])
 
# Output the row with the highest percentage of men
print(recent_grads['sharemen'][recent_grads['sharemen']== max_men])

# Find the maximum percentage value of men
max_men = np.max(recent_grads['sharemen'])
 
# Output the row with the highest percentage of men
print(recent_grads[recent_grads['sharemen'] == max_men])


# Make all gender difference values positive
recent_grads['gender_diff'] = np.abs(recent_grads['gender_diff'])

# Find the 5 rows with lowest gender rate difference
print(recent_grads.nsmallest(5, 'gender_diff'))


# Rows where gender rate difference is greater than .30 
diff_30 = recent_grads.gender_diff > .30

# Rows with more men
more_men = recent_grads.men > recent_grads.women

# Combine more_men and diff_30
more_men_and_diff_30 = np.logical_and(more_men,diff_30)

# Find rows with more men and and gender rate difference greater than .30
fewer_women = recent_grads[more_men_and_diff_30 >.30]

# Group by major category and count
print(recent_grads.groupby(['major_category']).major_category.count())
print(fewer_women.groupby(['major_category']).major_category.count())

# Report average gender difference by major category
print(recent_grads.groupby(['major_category']).gender_diff.mean())
