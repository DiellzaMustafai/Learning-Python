#Write a Python program to find the XOR of two given strings interpreted as binary numbers.
#License: https://bit.ly/3oLErEI
def test(nums):
    return bin(int(nums[0],2) ^ int(nums[1],2))
nums =  ["0001", "1011"]
print("Original strings:")
print(nums)
print("XOR of two said strings interpreted as binary numbers:")
print(test(nums))
nums =  ["100011101100001", "100101100101110"]
print("\nOriginal strings:")
print(nums)
print("XOR of two said strings interpreted as binary numbers:")
print(test(nums))


#Write a Python program to find all even palindromes up to n.
#License: https://bit.ly/3oLErEI

def test(n):
    return [i for i in range(0,n,2) if str(i) == str(i)[::-1]] 
n = 50
print("\nEven palindromes up to",n,"-")
print(test(n))
n = 100
print("\nEven palindromes up to",n,"-")
print(test(n))
n = 500
print("\nEven palindromes up to",n,"-")
print(test(n))
n = 2000
print("\nEven palindromes up to",n,"-")
print(test(n))



#Write a Python program to create a list of True/False that determine whether candidate filename is valid or not.
def test(file_names):
         return ["Yes" if
            f.split(".")[1:] in [['txt'], ['png'], ['dll'], ['exe'], ['jpg']] and f[0].isalpha() and sum(c.isdigit() for c in f) < 4
            else "No"
            for f in file_names]
 
file_names = ['abc.txt', 'windows.dll', 'tiger.png', 'rose.jpg', 'test.py', 'win32.exe']
print("Original list of files:")
print(file_names)
print("Valid filenames:")
print(test(file_names))
file_names = ['.txt', 'windows.exe', 'tiger.jpeg', 'rose.c', 'test.java']
print("\nOriginal list of files:")
print(file_names)
print("Valid filenames:")
print(test(file_names))
