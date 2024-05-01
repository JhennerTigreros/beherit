#pragma once

#include <string>
#include <vector>

class Device {
    public:
        Device();
        const std::vector<Device> &devices();
        Device &get_device(const std::string &name);
    private:
        std::string platform;
        std::string version;
        std::string sdk_path;
        std::vector<Device> _devices;
};
