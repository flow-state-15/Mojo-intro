from python import Python

# running into snags trying to convert interpreted python into compiled mojo!
# like, list slicing/copying

def complex_matrix(xmin, xmax, ymin, ymax, pixel_density, np ):
    re = np.linspace(xmin, xmax, (xmax - xmin) * pixel_density)
    im = np.linspace(ymin, ymax, (ymin - ymax) * pixel_density)
    return re[np.newaxis, :] + im[:, np.newaxis] * 1j


fn main() raises:
    np = Python.import_module("numpy")
    matplotlib = Python.import_module("matplotlib")
    plt = matplotlib.pyplot
    time = Python.import_module("time")
    matplotlib.use('Agg') # changing backend b/c display issues

    s = time.perf_counter_ns()



    e = time.perf_counter_ns()