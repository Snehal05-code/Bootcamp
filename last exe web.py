import threading

# Fake fetcher data (same as Go version)
fetcher = {
    "https://golang.org/": (
        "The Go Programming Language",
        ["https://golang.org/pkg/", "https://golang.org/cmd/"]
    ),

    "https://golang.org/pkg/": (
        "Packages",
        [
            "https://golang.org/",
            "https://golang.org/cmd/",
            "https://golang.org/pkg/fmt/",
            "https://golang.org/pkg/os/",
        ],
    ),

    "https://golang.org/pkg/fmt/": (
        "Package fmt",
        ["https://golang.org/", "https://golang.org/pkg/"],
    ),

    "https://golang.org/pkg/os/": (
        "Package os",
        ["https://golang.org/", "https://golang.org/pkg/"],
    ),
}


class Fetcher:
    def fetch(self, url):
        if url in fetcher:
            return fetcher[url]
        raise Exception(f"not found: {url}")


# Shared cache + lock (like Go map with mutex)
visited = set()
lock = threading.Lock()


def crawl(url, depth, fetcher):
    if depth <= 0:
        return

    # ---- critical section (map safety) ----
    with lock:
        if url in visited:
            return
        visited.add(url)
    # ---------------------------------------

    try:
        body, urls = fetcher.fetch(url)
        print(f"found: {url} \"{body}\"")
    except Exception as e:
        print(e)
        return

    threads = []

    # launch parallel crawls
    for u in urls:
        t = threading.Thread(target=crawl, args=(u, depth-1, fetcher))
        t.start()
        threads.append(t)

    # wait for all child threads
    for t in threads:
        t.join()


def main():
    f = Fetcher()
    crawl("https://golang.org/", 4, f)


if __name__ == "__main__":
    main()
