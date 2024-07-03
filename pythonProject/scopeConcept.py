def checkScope():
    def doLocal():
        test="Local test"
    def doNonLocal():
        nonlocal test
        test="Non local test"
    def doGlobal():
        global test
        test="Global test"

    test="default"
    doLocal()
    print("Test value after do local test:"+test)
    doNonLocal()
    print("Test value after do non local test:" + test)
    doGlobal()
    print("Test value after global test:" + test)
checkScope()