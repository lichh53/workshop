# Pybind11 绑定方式总结

在 **Pybind11** 中，除了使用 `.def_readwrite` 来暴露类的属性，和使用 `.def` 来暴露函数或方法外，还有其他一些常用的绑定方式和功能。以下是常见的绑定方式及其用途：

## 1. `.def_readonly` 和 `.def_readwrite`
- **`.def_readonly`**：将类的属性暴露为只读属性，Python 端只能读取该属性。
    ```cpp
    .def_readonly("name", &ClassName::member_variable)
    ```
- **`.def_readwrite`**：将类的属性暴露为可读写属性，Python 端可以读取和修改该属性。
    ```cpp
    .def_readwrite("name", &ClassName::member_variable)
    ```

## 2. `.def_property` 和 `.def_property_readonly`
- **`.def_property`**：通过 getter 和 setter 方法暴露类的属性，控制属性的读取和写入行为。
    ```cpp
    .def_property("property_name", &ClassName::get_property, &ClassName::set_property)
    ```
- **`.def_property_readonly`**：暴露只读属性，只定义 getter，防止 Python 端修改属性。
    ```cpp
    .def_property_readonly("property_name", &ClassName::get_property)
    ```

## 3. `.def_static` 和 `.def_static_readonly`
- **`.def_static`**：暴露静态方法，不依赖于类的实例。
    ```cpp
    .def_static("static_method_name", &ClassName::static_method)
    ```
- **`.def_static_readonly`**：暴露静态只读属性。
    ```cpp
    .def_static_readonly("static_variable_name", &ClassName::static_variable)
    ```

## 4. `.def_overload_cast` 和 `.def_overload`
- **`.def_overload_cast`**：用于函数重载，确保调用的是正确的重载版本。
    ```cpp
    .def("method_name", py::overload_cast<int>(&ClassName::method))
    ```

## 5. `.def_init`
- **`.def(py::init<>())`**：绑定构造函数，允许在 Python 中通过构造函数创建类实例。
    ```cpp
    .def(py::init<int, std::string>())
    ```

## 6. `.def_operator`（操作符重载）
- **`.def_operator`**：绑定操作符重载，使 Python 中可以使用自定义的操作符（如 `+`, `==`, `[]`）。
    ```cpp
    .def(py::self + py::self)  // 绑定 `+` 操作符
    .def(py::self == py::self)  // 绑定 `==` 操作符
    ```

## 7. `.def_repr`
- **`.def_repr`**：为 Python 中的对象定义 `__repr__` 方法，便于打印对象的可读字符串表示。
    ```cpp
    .def("__repr__", [](const ClassName &a) {
        return "<ClassName value=" + std::to_string(a.value) + ">";
    })
    ```

## 8. `.def_pickle`
- **`.def_pickle`**：绑定 Python 中对象的序列化和反序列化，用于 `pickle` 序列化/反序列化。
    ```cpp
    .def(py::pickle(
        [](const ClassName &a) {  // __getstate__
            return py::make_tuple(a.value);
        },
        [](py::tuple t) {  // __setstate__
            return ClassName(t[0].cast<int>());
        }
    ))
    ```

## 9. `.def_buffer`
- **`.def_buffer`**：将类暴露为缓冲区接口，允许其与 NumPy 等库直接交互。
    ```cpp
    .def_buffer([](ClassName &a) -> py::buffer_info {
        return py::buffer_info(
            a.data(),                                // 指向缓冲区的指针
            sizeof(double),                          // 单个标量的大小
            py::format_descriptor<double>::format(), // 格式描述符
            1,                                       // 维度数
            { a.size() },                            // 缓冲区维度
            { sizeof(double) }                       // 步长
        );
    })
    ```

---

这些功能进一步增强了 C++ 和 Python 之间的交互，允许你将 C++ 类和函数更灵活地暴露给 Python，并且在 Python 中以更 Pythonic 的方式操作它们。这些接口在绑定 C++ 对象的属性、方法、操作符重载、序列化、以及与 Python 数据类型交互时非常有用。