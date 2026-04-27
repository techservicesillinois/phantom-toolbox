#!/usr/bin/env pwsh
$env:PATH=".tox/wheel/Scripts:$env:PATH" 
Write-Output "Path is " + $env:PATH
which phantom
phantom --help
Write-Output "************* End of Debug for Win Accept Test ***********************"
robot tests/robot
Write-Output "************* End of Win Accept Test ***********************"
