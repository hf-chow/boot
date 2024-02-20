from potion_stack import *

test_cases = [
    ("Mana Potion", ["Mana Potion"]),
    ("Health Potion", ["Mana Potion", "Health Potion"]),
    ("Health Potion", ["Mana Potion", "Health Potion"]),
    ("Health Potion", ["Mana Potion", "Health Potion"]),
    ("Invisibility Potion", ["Mana Potion", "Health Potion", "Invisibility Potion"]),
]

def test(stack, input, expected_output):
    print("------------------------------")
    print(f"Input:")
    print(f" * Potion: {input}")
    print(f"Expecting: {expected_output}")
    stack.push(input)
    result = stack.items
    print(f"Actual: {result}")
    if result == expected_output:
        print("PASS")
        return True
    print("FAIL")
    return False

def main():
    stack = PotionStack()
    passed = 0
    failed = 0
    for case in test_cases:
        correct = test(stack, *case)
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
