#!/usr/bin/env pwsh
$ErrorActionPreference = "Stop"
$env:PATH="$(Get-Location)/.tox/wheel/Scripts:$env:PATH" 
Write-Output "Path is " + $env:PATH
which phantom
phantom --help
Write-Output "************* End of Debug for Win Accept Test ***********************"
robot tests/robot
