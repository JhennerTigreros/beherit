# include <pybind11/pybind11.h>

namespace py = pybind11;

PYBIND11_MODULE(example, m) {
    m.doc() = "Module definition to communicate with low level hardware instructions and optimizations.";
}