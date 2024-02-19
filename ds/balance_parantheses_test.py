from balance_parathesis import is_valid_nesting

test_cases = [
        ("()()", True),
        ("(())", True),
        ("()()))", False),
        ("(())()", True),
        ("))((", False),
        ("()", True)
        ]

def test(_input, expected_output):
    print("------------------------------")
    print(f"Input Number: {_input}")
    print(f"Is Expecting: {expected_output}")
    result = is_valid_nesting(_input)
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
