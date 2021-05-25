1. Figure out how to conditionally include changelog or otherwise deal with gif in latex
2. Note that updating PDF requires
   1. run make latexpdf in main sphinx folder
   2. run mixtex_portable from programs folder
   3. wait for it to load, then launch a prompt with it from tray icon
   4. Make sure perl is on the PATH in that prompt (C:\StrawberryPerl\perl\bin)
   5. navigate to docs folder\build\latex and run make all-pdf
