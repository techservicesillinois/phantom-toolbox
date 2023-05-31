*** Settings ***
Resource  help.resource
Variables  vars.py


*** Test Cases ***
Test all scripts with --help
    Log To Console    \n
    FOR  ${cmd}  IN  @{ALL_COMMANDS}
        Log to Console    					\t$phantom {cmd}
        Test --help  						${cmd}
    END