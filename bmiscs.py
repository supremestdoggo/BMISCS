codec = ' etaoinshrdlcumwfgypbvkjxqz.?!'

def convert_to_base(decimal_number, base, digits):
    remainder_stack = []
    while decimal_number > 0:
        remainder = decimal_number % base
        remainder_stack.append(remainder)
        decimal_number = decimal_number // base
    new_digits = []
    while remainder_stack:
        new_digits.append(digits[remainder_stack.pop()])
    return ''.join(new_digits)
  
def base_to_dec(string,base,digits):
    num_str = string[::-1]
    num = 0
    for k in range(len(num_str)):
        dig = num_str[k]
        if dig.isdigit():
            dig = int(dig)
        else:
            dig = digits.index(dig.lower())-digits.index('a')+10
        num += dig*(base**k)
    return int(num)

def filter(string,allowed_characters):
  output_string = ''
  for x in list(string):
    if x in allowed_characters:
      output_string = output_string + x
  return output_string

def bmiscs_encode(string):
  output_string = filter(string,codec)
  output_int = base_to_dec(output_string,len(codec),codec)
  return output_int

def bmiscs_decode(number):
  output_string = convert_to_base(number,len(codec),codec)
  return output_string