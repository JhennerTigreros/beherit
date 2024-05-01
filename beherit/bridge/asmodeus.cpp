#include "device.h"
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace py = pybind11;

PYBIND11_MODULE(beherit, m) {
  m.doc() = "Module definition to communicate with low level hardware "
            "instructions and optimizations.";

  py::class_<Device>(m, "Device")
      .def(py::init<>())
      .def("devices", &Device::devices)
      .def("get_devices", &Device::get_device);
}
