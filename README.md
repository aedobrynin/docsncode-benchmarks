# docsncode-benchmarks

This repository contains benchmarks of [DocsnCode project](https://github.com/aedobrynin/docsncode).

## How to benchmark

1. Create new docsncode project or use `docsncode_project_generator.py <path-to-project-dir>`
    to make your project docsncode-compliant. Generator has very limited 
    functionality and may cause the project to stop building. It works only
    with C files and converts not all comments.

    **WARNING: it modifies the project directory**
2. Run `benchmark.py <path-to-project-dir>` to run the benchmarks.
    You can provide cache type as a third positional argument (`none`, `modtime`, `hash`).

## linux-with-docsncode benchmark

Tested on i7-12800H with 32 Gb. RAM.

1. We cloned current [linux kernel](https://github.com/torvalds/linux).

2. Generated docsncode-compliant project with `docnscode_project_generator.py`.

It's output was:
```
total comments processed: 943322
total files processed: 61002
total files: 88857
total directories processed: 5912
```

3. Ran `benchmark.py linux-with-docsncode none` to test it without any caching.

    And got the following result:
    ```
    Execution try finished, execution_time: 12.83767056465149
    Execution try finished, execution_time: 13.177760124206543
    Execution try finished, execution_time: 13.2678804397583
    Execution try finished, execution_time: 13.312976837158203
    Execution try finished, execution_time: 13.945830583572388
    Execution try finished, execution_time: 14.113778114318848
    Execution try finished, execution_time: 14.036697149276733
    Execution try finished, execution_time: 14.482021808624268
    Execution try finished, execution_time: 14.414376735687256
    Execution try finished, execution_time: 14.290595054626465
    Min execution time: 12.8376705647 seconds
    Avg execution time: 13.7879587412 seconds
    Max execution time: 14.4820218086 seconds
    ```

4. Ran `benchmark.py linux-with-docsncode modtime` to test it with modtime cache.

    And got the following result:
    ```
    Execution try finished, execution_time: 13.067859172821045
    Execution try finished, execution_time: 12.793839931488037
    Execution try finished, execution_time: 12.8129301071167
    Execution try finished, execution_time: 13.125548124313354
    Execution try finished, execution_time: 13.958875894546509
    Execution try finished, execution_time: 14.490320920944214
    Execution try finished, execution_time: 13.942127704620361
    Execution try finished, execution_time: 14.407310247421265
    Execution try finished, execution_time: 13.924032211303711
    Execution try finished, execution_time: 14.132335186004639
    Min execution time: 12.7938399315 seconds
    Avg execution time: 13.6655179501 seconds
    Max execution time: 14.4903209209 seconds
    ```

4. Ran `benchmark.py linux-with-docsncode hash` to test it with hash cache.

    And got the following result:
    ```
    Execution try finished, execution_time: 12.769819736480713
    Execution try finished, execution_time: 13.11590576171875
    Execution try finished, execution_time: 13.623903036117554
    Execution try finished, execution_time: 14.870942831039429
    Execution try finished, execution_time: 14.611047506332397
    Execution try finished, execution_time: 15.80657172203064
    Execution try finished, execution_time: 15.571398735046387
    Execution try finished, execution_time: 15.914688348770142
    Execution try finished, execution_time: 15.200995445251465
    Execution try finished, execution_time: 14.959194660186768
    Min execution time: 12.7698197365 seconds
    Avg execution time: 14.6444467783 seconds
    Max execution time: 15.9146883488 seconds
    ```

5. Rebuilt the project with modtime cache, changed one file and ran the build again. The build took TODO sec.

6. Rebuilt the project with hash cache, changed one file and ran the build again. The build took TODO sec.
