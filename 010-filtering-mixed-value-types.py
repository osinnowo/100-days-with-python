numbers = ['1', 2, 3, 'four', None, '6']
items = [int(num) for num in numbers if isinstance(num, int) or isinstance(num, str) and num.isdigit()]

# Testing
print(items) #[1, 2, 3, 6]
