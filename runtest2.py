import functools

# ฟังก์ชันช่วยคำนวณค่า
def binary_to_char(binary_str):
    return chr(int(binary_str, 2))

def octal_to_char(octal_str):
    return chr(int(octal_str, 8))

def hex_to_char(hex_str):
    return chr(int(hex_str, 16))

def arithmetic_char(value):
    return chr(value)

def prime_sum_char(primes, subtract_value):
    return chr(sum(primes) - subtract_value)

def fibonacci_char(n):
    return chr(functools.reduce(lambda ab, _: (ab[1], ab[0] + ab[1]), range(n), (1, 1))[1])

def digit_sum_char(digits):
    return chr(sum(int(d) for d in digits) + 1)

def manipulate_chars(base_char, target_char, offset):
    return chr((ord(base_char) - ord(target_char)) + offset)

# ค่าต่าง ๆ ที่ใช้ในฟังก์ชัน
result = [
    binary_to_char("1010011"),
    octal_to_char("101"),
    hex_to_char("57"),
    arithmetic_char(10**2 - 35),
    prime_sum_char([2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 51),
    fibonacci_char(9),
    manipulate_chars('A', 'i', 0),  # A + i - i -> A
    digit_sum_char("99999"),
    manipulate_chars('z', 'h', 69)
]

# รวมตัวอักษร
email = "".join(result)
print("Email:", email)
