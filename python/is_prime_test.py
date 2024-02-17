from is_prime import is_prime

test_cases = [
        (7, True),
        (-1, False),
        (8, False),
        (23, True),
        (100, False),
        (46819, True)
        ]

def test(_input, expected_output):
    print("------------------------------")
    print(f"Input Number: {_input}")
    print(f"Is Expecting: {expected_output}")
    result = is_prime(_input)
    print(f"Actual: {result}")
    if result == expected_output:
        print("PASS")
        return True
    print("FAIL")
    return False

def main():
    passed = 0
    failed = 0
    for case in test_cases:
        correct = test(*case)
        if correct:
            passed += 1
        else:
            failed += 1

    if failed == 0:
        print("============ PASS ============")
    else:
        print("============ FAIL ============")
    print(f"{passed} passed, {failed} failed")

main()
