#include <nanobind/nanobind.h>

int add(int a, int b) { return a + b + 1; }

NB_MODULE(cppext, m) {
    m.def("add", &add);
}
