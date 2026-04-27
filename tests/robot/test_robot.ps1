#!/usr/bin/env pwsh
$ErrorActionPreference = "Stop"
ls -r "$(Get-Location)/.tox/wheel/"
ls -r "$(Get-Location)/.tox/wheel/bin"
$env:PATH="$(Get-Location)/.tox/wheel/bin:$env:PATH" 
Write-Output "Path is " + $env:PATH
Get-Command phantom
phantom --help
Write-Output "************* End of Debug for Win Accept Test ***********************"
robot tests/robot
