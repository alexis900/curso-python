from mimetypes import init


palindrome = lambda string: string == string[::-1]
print(palindrome('ana'))