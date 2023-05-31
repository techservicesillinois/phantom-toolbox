*** Settings ***
Library  Process

*** Keywords ***
Test --help
   [Arguments]    ${arg}

   ${result} =  Run Process    phantom    ${arg}  --help
   Should Not Contain  ${result.stderr}  error  ignore_case=True
   Should Not Contain  ${result.stderr}  traceback  ignore_case=True
   Should Be Equal As Integers    ${result.rc}    0
   Should Contain  ${result.stdout}  description:
   Should Contain  ${result.stdout}  --help
