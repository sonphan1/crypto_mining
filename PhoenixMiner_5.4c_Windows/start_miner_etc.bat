REM
REM Example bat file for starting PhoenixMiner.exe to mine ETC
REM

setx GPU_FORCE_64BIT_PTR 0
setx GPU_MAX_HEAP_SIZE 60
setx GPU_USE_SYNC_OBJECTS 1
setx GPU_MAX_ALLOC_PERCENT 60
setx GPU_SINGLE_ALLOC_PERCENT 60

REM IMPORTANT: Replace the ETC address with your own ETC wallet address in the -wal option (Rig001 is the name of the rig)
PhoenixMiner.exe -pool eu1.ethermine.org:4444 -pool2 us1.ethermine.org:4444 -wal 0x0620d26d5dde3ec053aa0ac49404efcc8555a4a3.lance-pc
pause

