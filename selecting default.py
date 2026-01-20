import time

def main():
    start = time.time()

    tick_interval = 0.1      # 100 ms
    boom_time = 0.5          # 500 ms
    sleep_default = 0.05     # 50 ms

    next_tick = start + tick_interval
    boom = start + boom_time

    def elapsed():
        return round((time.time() - start) * 1000)

    while True:
        now = time.time()

        # case <-tick
        if now >= next_tick:
            print(f"[{elapsed():6} ms] tick.")
            next_tick += tick_interval

        # case <-boom
        elif now >= boom:
            print(f"[{elapsed():6} ms] BOOM!")
            return

        # default
        else:
            print(f"[{elapsed():6} ms]     .")
            time.sleep(sleep_default)


if __name__ == "__main__":
    main()
