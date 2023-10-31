# Loop through a list of numbers from 1-20 and print out the even numbers and any numbers divisible
# by 5.
for num in range(1, 21):
    if num %2==0 or num %5 ==0:
        print(num)