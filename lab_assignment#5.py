
# n = int(input("Enter the number of terms: "))
# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)



# print("Fibonacci sequence:")
# for i in range(n):
#     print(fibonacci(i), end=" ")


#Q6

# n = int(input("Enter the number of terms: "))
# total=0

# def sum(n):
#     if(n==0):
#         return 0
#     else:
#        return n + sum(n-1)

# print("Sum of natural numbers is:", sum(n))


#Q7
# import string

# str = ((input("Enter a string: ")).lower()).replace(" ","")
# print(str)
# def palindrome(str):
#     result = ""

#     for char in str:
#         if char not in string.punctuation:
#             result = result + char

#     rev = result[::-1]

#     if(rev == result):
#         return (print("Given string is palindrome"))
#     else:
#         return (print("Given string is not palindrome"))

# palindrome(str)

#Q8

# import string

# str = (input("Enter a sentence: ")).lower()

# def pangramCheck(str):
#     for l in string.ascii_lowercase:
#         if l not in str:
#             return False
        
#     return True

# if pangramCheck(str) == True:
#     print("The sentence is a pangram.")
# else:
#     print("The sentence is not a pangram.")


#Q9

# def overlapping(l1,l2):
#     for n in l1:
#         if n in l2:
#             return "Lists have a common element"
#     return "Lists do not have any common element"


# list1 = [1, 2, 0, 4, 5]
# list2 = [6, 7, 3, 8, 9]

# print(overlapping(list1, list2))

#Q10

# def find_longest_word(list):
#     longest = list[0]
#     for word in list:
#         if len(word) > len(longest):
#             longest = word

#     return longest

# words = ["apple", "banana", "elephant", "cat", "computer"]
# print("Length of the longest word is :", len(find_longest_word(words)))
# print("And longest word is :", find_longest_word(words))


#Q11

def filter_long_words(words, n):
    result = []
    for word in words:
        if len(word) > n:
            result.append(word)
    return result

words = ["apple", "banana", "elephant", "cat", "computer"]
n = int(input("Enter the value of n: "))

print("Words longer than", n, "are:", filter_long_words(words, n))
