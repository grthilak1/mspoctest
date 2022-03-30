*** Settings ***
Library           Process
#Suite Teardown    Terminate All Processes    kill=True

*** Test Cases ***
Test1
    Run Process    python3    -c    print('Hello, world!')

Test2
    ${result} =    Run Process    ansible    --version
    Should Be Equal    ${result.rc}    ${0}
    log    stdout: ${result.stdout}

Test3
    ${result} =    Run Process    ansible-playbook    getarp.yml
    Should Be Equal    ${result.rc}    ${0}
    log    stdout: ${result.stdout}

Test4
    ${result} =    Run Process    python3    git_push.py
    Should Be Equal    ${result.rc}    ${0}
    log    stdout: ${result.stdout}

