# Pass a tuple to the divmod() function and obtain the quotient and the remainder
def divmod(dividend, divisor):
    return (dividend // divisor, dividend % divisor)

dividend = float(input('Enter the dividend: '))
divisor = float(input('Enter the divisor: '))

quotient, remainder = divmod(dividend, divisor)

print(f'Quotient: {quotient}, Remainder: {remainder}')
