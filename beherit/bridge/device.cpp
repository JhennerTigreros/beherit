#include "device.h"
#include <vector>
#include <string>

using namespace std;

Device::Device() {
    platform = "macos";
    version = "v1.0.1";
    sdk_path = "./here";
    _devices = std::vector<Device>();
}

const std::vector<Device> &Device::devices() {
    return _devices;
}

Device &Device::get_device(const std::string &name) {
    if (_devices.size() > 0) {
        return _devices[0];
    }
}