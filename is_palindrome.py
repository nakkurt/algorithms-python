def is_palindrome(w):
  w = w.replace(' ','').lower() 
  return w[::-1] == w