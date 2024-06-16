dice_result = [5,6,4,2,5,4,4,5,3,3,2,6,1,2,1,1,6,5]
#How many times have you got 4s two times in a row?

dice_result = [5, 6, 4, 4, 5, 4, 4, 5, 3, 3, 2, 6, 1, 2, 1, 1, 6, 5]

count = 0
for i in range(len(dice_result) - 1):  # Iterate up to second-to-last element
    if dice_result[i] == 4 and dice_result[i+1] == 4:  # Check if current and next elements are both 4
        count += 1

print(count)
