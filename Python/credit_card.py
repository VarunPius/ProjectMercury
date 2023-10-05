'''
Verhoeff-Gumm Check Digit Algorithm
The Verhoeff algorithm is a checksum for error detection.
It was the first decimal check digit algorithm which detects all single-digit errors, and all transposition errors involving two adjacent digits.

Best use case of the algorithm would be to check whether the credit card number is correct or not.
This is instrumental for implementing credit card check in client side (or vendor server side) rather than sending incorrect details to bank.

This is a simplication of the actual implementation. In real world, more security is embedded (which includes CVV or expiry date and such)

Let's take an example:
Card:   6524 1423 8324 9084
We now double every other digit:
    12 5 4 4 2 4 4 3 16 3 4 4 18 0 16 4
Finally we simply add each and every digit. Double digit numbers are split and added.
    1 + 2 + 5 + 4 + 4 + 2 + 4 + 4 + 3 + 1 + 6 + 3 + 4 + 4 + 1 + 8 + 0 + 1 + 6 + 4
Divide the final output by 10. If it's divisible by 10, then the number is correct.
Here, the output is 67. Hence the number is invalid.

The customer realizes his mistake in his card number. Let's change the card number:
Card:   6524 7423 8324 9084
             ^ 1 is replaced by 7
Now double every other digit:
    12 5 4 4 14 4 4 3 16 3 4 4 18 0 16 4
Add the digit:
The output is 70, which is divisible by 10. Hence, the card number is correct.
'''


def check_card(card_number):
    target = 0
    for i, n in enumerate(card_number):
        n = int(n)
        if i%2 == 0:
            n = n*2
        
        carry, div = n//10, n%10
        target+= carry + div

    return not(target%10)


if __name__ == '__main__':
    card_number = "6524142383249084"     # since number is huge, let's consider string
    flag = check_card(card_number)
    print(flag)

    card_number = "6524742383249084"     # since number is huge, let's consider string
    flag = check_card(card_number)
    print(flag)

