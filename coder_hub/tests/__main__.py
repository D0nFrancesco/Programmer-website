from tests import test_001, test_002

LOG_FILE_NAME = "tests/test.log"
LOG_FILE = open(LOG_FILE_NAME, "w")

COLORS = {
    "white": "\u001b[0;0;0m",
    "red": "\u001b[31m",
    "green": "\u001b[32m"
}


def log(text, verbose_item=False, color="white"):
    """
    Log text to console if verbose_item. And always to file.
    """
    if verbose_item:
        print(f"{COLORS[color]}{text}{COLORS['white']}")
    LOG_FILE.write(f"{text}\n")


TESTS = {
    "test_001": test_001,
    "test_002": test_002,
}
fails = 0

log(f"Running {len(TESTS)} test(s)", verbose_item=True)
log("", verbose_item=True)

for test_name in TESTS:
    test = TESTS[test_name]
    status_code, content = test()

    if status_code != 200:
        log(f"❌ Test '{test_name}' failed...", verbose_item=True, color='red')
        log(f"\tstatus_code: {status_code}, server response:\n\t\t{content}")

        if status_code == 404:
            log(f"\tStatus code is: {status_code}, either the URL doesn't work, or there is no object with that ID.")

        fails += 1
    else:
        log(f"✅ Test '{test_name}' succeeded", verbose_item=True, color='green')
        log(f"\tstatus_code: {status_code}, server response:\n\t\t{content}")

    log("")

log("", verbose_item=True)
if fails == 0:
    log("All tests succeeded, ready for launch 🚀", verbose_item=True, color='green')
else:
    log("Not all tests succeeded 😭... Back to work 👨‍💻", verbose_item=True, color='red')
    log("For a more detailed view of why tests failed see: 'tests/test.log'", verbose_item=True)
