import re
import os


def function_to_print():
    print("Hello World!")
    print("Let's try to learn GIT in details")
    return 0


def function_to_verify():
    if not function_to_print():
        print("This test has pass!!")


if __name__ == "__main__":
    function_to_verify()


@echo off
setlocal
for / F "tokens=2 delims=|" % %a in ('findstr /I "LastLogedUser=" something.txt') do set "uniuser=%%a"
echo User is : % uniuser%
copy fpr_log.txt "c:\fpr_log%uniuser%.txt"
endlocal
