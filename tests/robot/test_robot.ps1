#!/usr/bin/env pwsh
$ErrorActionPreference = "Stop"
$env:PATH="$(Get-Location)\.tox\wheel\Scripts;$env:PATH"
robot tests/robot
