def isPalindrome(source):
    is_palindrome = True
    if len(source) >= 2:
        count_odd = 0
        unique_str = set(source)
        for item in unique_str:
            if source.count(item) % 2 == 1:
                count_odd += 1
        if count_odd > 1:
            is_palindrome = False

    return is_palindrome
