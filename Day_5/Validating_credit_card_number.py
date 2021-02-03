import re
for i in range(int(input())):
    num = input()

    ok1 = bool(re.match(r"^[456]\d{15}$", num))
    ok2 = bool(re.match(r"^[456]\d{3}\-\d{4}\-\d{4}\-\d{4}$", num))
    num = num.replace("-", "")
    ok3 = bool(re.match(r"(?!.*(\d)(-?\1){3})", num))
    if (ok1 or ok2) and ok3:
        print("Valid")
    else:
        print("Invalid")

# import re
# for i in range(int(input())):
#     S = input().strip()
#     pre_match = re.search(r'^[456]\d{3}(-?)\d{4}\1\d{4}\1\d{4}$',S)
#     if pre_match:
#         processed_string = "".join(pre_match.group(0).split('-'))
#         final_match = re.search(r'(\d)\1{3,}',processed_string)
#         print ('Invalid') if final_match else 'Valid'
#     else:
#         print ('Invalid')
