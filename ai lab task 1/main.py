
test_cases = [
    [85, True, True, True],   
    [85, True, False, True],  
    [85, True, True, False],  
    [70, True, True, True]    
]
for score, documents, residency, deadline in test_cases:
    if score >= 70 and documents and residency and deadline:
        print("PASS")
    else:
        print("FAIL")
