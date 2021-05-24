import os

test_file = open("byme.py", "w", encoding="utf8")
test_file.write("print(\"파일을 생성합니다\")")
test_file.write("\ndef test():")
test_file.write("\n\tprint(\"함수를 생성하였습니다\")")
test_file.close()

test_file = open("byme.py", "r", encoding="utf8")
while True:
    line = test_file.readline()
    if not line:
        break
    print(line)
test_file.close()

import byme
if os.path.isfile("byme.py"):
    print("파일이 있습니다")
    byme.test()
    # print("파일을 삭제합니다")
    # os.remove("byme.py")

