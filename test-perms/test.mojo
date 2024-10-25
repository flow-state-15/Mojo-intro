fn main() raises:
    from python import Python
    # try:
        # plt = Python.import_module("matplotlib.pyplot")
    # except:
    #     print("Import Error")
    
    time = Python.import_module("time")
    s = time.time()
    print("Hello World")
    e = time.time()
    print("Done in ", e-s, " seconds")
