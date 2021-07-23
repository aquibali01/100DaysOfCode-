#Write your code below this line 👇

def prime_checker(number):
  is_prime = True
  if number > 0:

    for i in range(2, number):
      if number % i == 0:
        print("It is not a prime number.")
        is_prime = False
        break
    if is_prime:
      print("It is a prime number")
  else:
    print("Its not a prime number")

    


#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



