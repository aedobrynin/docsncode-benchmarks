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
    total comments processed: 943071
    total files processed: 61002
    total files: 88857
    total directories processed: 5912
    ```

3. Ran `benchmark.py linux-with-docsncode none` to test it without any caching.

    And got the following result:
    ```
    Execution try finished, execution_time: 9.342565536499023 s.
    Execution try finished, execution_time: 9.515044927597046 s.
    Execution try finished, execution_time: 9.465934038162231 s.
    Execution try finished, execution_time: 9.655285358428955 s.
    Execution try finished, execution_time: 10.332965850830078 s.
    Execution try finished, execution_time: 10.173842906951904 s.
    Execution try finished, execution_time: 10.119024753570557 s.
    Execution try finished, execution_time: 10.268062353134155 s.
    Execution try finished, execution_time: 11.203366756439209 s.
    Execution try finished, execution_time: 10.982413291931152 s.
    Min execution time: 9.3425655365 seconds
    Avg execution time: 10.1058505774 seconds
    Max execution time: 11.2033667564 seconds
    ```

4. Ran `benchmark.py linux-with-docsncode modtime` to test it with modtime cache.

    And got the following result:
    ```
    Execution try finished, execution_time: 9.161744356155396 s.
    Execution try finished, execution_time: 10.260641098022461 s.
    Execution try finished, execution_time: 10.191008806228638 s.
    Execution try finished, execution_time: 10.235474348068237 s.
    Execution try finished, execution_time: 10.352956295013428 s.
    Execution try finished, execution_time: 10.542083740234375 s.
    Execution try finished, execution_time: 10.4089515209198 s.
    Execution try finished, execution_time: 10.308413982391357 s.
    Execution try finished, execution_time: 10.23032522201538 s.
    Execution try finished, execution_time: 10.30897068977356 s.
    Min execution time: 9.1617443562 seconds
    Avg execution time: 10.2000570059 seconds
    Max execution time: 10.5420837402 seconds
    ```

4. Ran `benchmark.py linux-with-docsncode hash` to test it with hash cache.

    And got the following result:
    ```
    Execution try finished, execution_time: 9.458965063095093 s.
    Execution try finished, execution_time: 9.354227542877197 s.
    Execution try finished, execution_time: 10.460801362991333 s.
    Execution try finished, execution_time: 10.596291780471802 s.
    Execution try finished, execution_time: 10.553105354309082 s.
    Execution try finished, execution_time: 10.640692710876465 s.
    Execution try finished, execution_time: 11.283113479614258 s.
    Execution try finished, execution_time: 10.927942276000977 s.
    Execution try finished, execution_time: 10.51029372215271 s.
    Execution try finished, execution_time: 10.544775485992432 s.
    Min execution time: 9.3542275429 seconds
    Avg execution time: 10.4330208778 seconds
    Max execution time: 11.2831134796 seconds
    ```

5. Rebuilt the project with modtime cache, changed one file and ran the build again. The build took 0.795 s. on average.

6. Rebuilt the project with hash cache, changed one file and ran the build again. The build took 1.734 s. on average.
