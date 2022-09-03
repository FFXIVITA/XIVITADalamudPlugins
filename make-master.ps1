$ErrorActionPreference = 'SilentlyContinue'
$output = New-Object Collections.Generic.List[object]
$notInclude = "sdgfdsgfgdfs", "sdfgdfg", "XIVStats", "bffbbf", "VoidList", "asdfsad", "sdfgdfsg", "vrgnddgv";
$counts = Get-Content "downloadcounts.json" | ConvertFrom-Json
$categoryFallbacksMap = Get-Content "categoryfallbacks.json" | ConvertFrom-Json
$wc = New-Object system.Net.WebClient
$dlTemplateInstall = "https://ffxivita.github.io/XIVITADalamudPlugins/dist/stable"