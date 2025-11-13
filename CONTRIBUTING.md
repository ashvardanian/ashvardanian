# Contributing to My Projects

Thank you for considering contributing to my projects!
To keep the quality of code and documentation high, there is a set of rules I follow and expect from regular contributors.

## Git History

I use `git` for version control.
The `main` branch should always be stable, the `main-dev` is the staging area.
A good commit message may look like this:

```
commit 53812b114729e006e226c4e8ef3b2b7919965364
Author: Ash Vardanian <1983160+ashvardanian@users.noreply.github.com>
Date:   Wed Nov 5 14:23:53 2025 +0000

    Improve: Faster SIMD kernel for sparse dot-product

    This commit introduces a new AVX-512 optimization for AMD Zen5
    CPUs that results in a 25% performance uplift on for sparse vector
    dot-product calculations using the `XXXX` instruction.

    Closes #42, #56

    Co-authored-by: Contributor Name <contributor@example.com>
    Reviewed-by: Reviewer Name <reviewer@example.com>
```

So the title line is short and descriptive.
It starts with a "Verb:" prefix, such as `Add:`, `Fix:`, `Improve:`, `Chore:`, `Break:`, or something else, compatible with [TinySemVer](https://github.com/ashvardanian/tinysemver) conventions.
It can contain no-reply emails with the GitHub user ID for proper attribution, but it shouldn't contain `@localhost` names.
Please use `Co-authored-by` to credit others.

## C++ Code

C++ is not one language but many dialects fused into one standard.
In short, my C++ subset for "core" code is:

- Avoid dynamic memory allocations - prefer stack allocation, `std::array`, `std::span`, or custom allocators.
- No exceptions - use error codes or `std::expected` instead. Handle out-of-memory and other critical failures gracefully.
- No [Run-Time Type Information](https://en.wikipedia.org/wiki/Run-time_type_information) (RTTI).

That said, tests, benchmarks, and examples follow more relaxed rules.
Even at the language level, there are clearly keywords that we use and others avoid, and vice versa.

|                  |                                                    We don't use |                 We use |
| :--------------- | --------------------------------------------------------------: | ---------------------: |
| Others use       | `throw`, `virtual`, `try`, `co_await`, `static`, `thread_local` |                    ... |
| Others don't use |                                                             ... | `goto`, `union`, `asm` |

There are other common patterns I prefer, more in line with modern C++ best practices:

| Traditional                     | Preferred                            |
| :------------------------------ | :----------------------------------- |
| `#ifdef X`                      | `#if defined(X)`                     |
| `#define FILE_NAME_H`           | `#pragma once`                       |
| `typedef x y;`                  | `using y = x;`                       |
| `auto v = expr(); if (v) {}`    | `if (auto v = expr(); v) {}`         |
| `if (x) { a; } else { b; }`     | `x ? a : b`                          |
| `~x() { if (y) { close(y); } }` | `~x() { if (!y) return; close(y); }` |

Avoid nesting in simple contexts.
That said, use scopes to limit the lifetime of variables and namespace pollution.

<table>
<tr>
<td>

```cpp
void validate_logic() {
    auto data_a = {1, 2, 3, 4, 5};
    auto sum_a = std::accumulate(data_a.begin(), data_a.end(), 0);        
    if (sum_a != 15) {
        std::printf("Sum mismatch for {}\n", sum_a);
    }

    auto data_b = {10, 20, 30};
    auto sum_b = std::accumulate(data_b.begin(), data_b.end(), 1, std::multiplies<>());
    if (sum_b != 6000) {
        std::printf("Product mismatch for {}\n", sum_b);
    }

    std::set<int> positive_mappings_b;
    for (auto const &value : data_b) {
        auto mapped_value = some_function(value);
        if (mapped_value >= 0) {
            positive_mappings_b.insert(mapped_value);
        }
    }
    ...
}
```

</td>
<td>

```cpp
void validate_logic() {
    {
        auto data = {1, 2, 3, 4, 5};
        auto sum = std::accumulate(data.begin(), data.end(), 0);        
        if (sum != 15) std::printf("Sum mismatch for {}\n", sum);
    }
    {
        auto data = {10, 20, 30};
        auto sum = std::accumulate(data.begin(), data.end(), 1, std::multiplies<>());
        if (sum != 6000) std::printf("Product mismatch for {}\n", sum);

        std::set<int> positive_mappings;
        for (auto const &value : data) {
            auto mapped_value = some_function(value);
            if (mapped_value < 0) continue;
            positive_mappings.insert(mapped_value);
        }
        ...
    }
}
```

</td>
</tr>
</table>


Prefer branchless techniques where possible.
Hand-written SIMD code or 4-8x way unrolled scalar code is often welcomed.
In libraries, attributes should be used to warn if functions are misused:

- `[[nodiscard]]` where the result of function execution can't be silently dropped.
- `[[maybe_unused]]` where the opposite effect is needed.

Aim for __C++ 20 standard compatibility__, avoiding compiler-specific extensions in library code.
Consider upgrading to C++ 23 once following proposals are widely supported:

- [p1169](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2022/p1169r4.html): `static operator ()` for efficient function objects.
- [p0847](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2021/p0847r7.html): "Deducing `this`" for explicit object parameter types.
- [p2128](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2021/p2128r6.pdf): Multi-dimensional subscripts for `std::mdspan`.
- [p0881](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/p0881r7.html): Stacktrace library.
- [p0323](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2022/p0323r12.html): `std::expected` for error handling.
- [p0429](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2022/p0429r9.pdf): `std::flat_map` for cache-friendly containers.

Following C++ 20 features usage is encouraged:

- [p0734](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2017/p0734r0.pdf): Concepts - forget `std::enable_if_t`.
- [p0515](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2017/p0515r3.pdf): spaceship operator `<=>` for comparisons.
- [p1099](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2019/p1099r5.html): `using enum` for cleaner `switch` tables.
- `std::ranges`, `std::span`, `std::atomic_ref`, `std::bit_cast`, `std::format`, `std::source_location`.

Following C++ 20 features should be avoided for broader compatibility:

- [p0912](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2019/p0912r5.html): Coroutines - avoid `co_yield` and `co_await`.
- [p1103](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2019/p1103r3.pdf): Modules - no `import std;` yet.

Following compiler versions are needed:

- GCC 12+ is needed for C++ 20 with AVX-512 and SVE extensions.
- Clang 17+ is needed for `consteval` functions and coroutines.
- MSVC 19.29+ for ranges library.
- AppleClang 16+ for floating-point atomics, text formatting, and source location.

### Formatting and Styling C++ Code

I use `clang-format` with the configuration defined in `.clang-format` file at the root of the repository.
Similarly, for CMake files, I use `cmake-format` with the configuration defined in `.cmake-format.py`.
Documentation is typically generated using Doxygen, mostly linking `.rst` files to `.md` Markdown files across the repository.

Tools aside, there are things that can't be enforced automatically but are still helpful in large codebases:

- Private names should end with an underscore, e.g., `my_variable_` or `my_type_`.
- Use `snake_case` for everything - variable, function names, templates, namespaces, etc.
- Prefer full words over abbreviations, e.g., `iterator` & `element` instead of `iter` & `elem`.
- Instantiate types (not templates) should end with `_t`, e.g., `value_t` or `string_view_t`.
- Avoid abbreviations and single-letter names, except for loop indices like `i`, `j`, or `k`.
- Avoid extra braces in single-line blocks, like `if (condition) task();`.
- Avoid generic class and variable names like `manager`, `value`, `item`, `obj`, `data`, `entry` - to simplify navigating GDB contexts.

Documentation is trickier.
All docstrings must use Doxygen-style comments.
Here are a couple of examples.
For minimalistic single-line descriptions:

```cpp
/** @brief Brief one-line description of the function or class. */
```

For more complex functions with many parameters, use the following template:

```cpp
/**
 *  @brief Some function similar to STL's @c std::map::try_emplace().
 *  @see External reference: https://en.cppreference.com/w/cpp/container/map/try_emplace.html
 *  @sa Internal reference: @c insert_if_missing() provides the same functionality.
 *  @param[in] key Object comparable and convertible to @c element_t.
 *  @return pair<iterator, bool> Pair consisting of an iterator to the inserted or existing element.
 *  @retval second True if a new element was inserted, false if an existing element was found.
 */
```

For multi-line descriptions, use 2 extra spaces for continuation indents:

```cpp
/**
 *  @brief Erases all elements in a range between two @c const_iterator values.
 *    Unlike STL, returns both the iterator following the last erased element and a status code.
 *    On error, some elements may have been erased (partial erase, matches STL's basic guarantee).
 *
 *  @param[in] first Beginning of range to erase.
 *  @param[in] last End of range to erase (not erased).
 *  @return erase_result_t Contains iterator equal to @p last and status of the operation.
 *    Returns first error encountered, or success if all elements erased.
 *
 *  @par Example
 *  @code{.cpp}
 *    auto [it, status] = my_container.erase_range(it_begin, it_end);
 *    if (status != status_t::success) {
 *        // Handle error
 *    }
 *  @endcode 
 */
 ```

Use `@see` for external references, `@sa` for internal cross-references, `@note` for attention points.
Use `@retval` for enumerated return values and `@return` for general return descriptions.
Mark class template parameters with `@tparam`.
Mark function parameters with direction indicators: `@param[in]`, `@param[out]`, or `@param[inout]` and cross-reference them with `@p` within the comment body.
Mark other class/type names and method names with `@c`.
Put examples or multi-token code snippets in `@code{.cpp}` ... `@endcode` blocks.
Use `@b` for bold text and `@a` for italics.
Keep whitespaces on both sides of tags - `[ @p example]` not `[@p example]`.
Use `@par` for titled sections within docstrings.
Start every file with a file-level docstring describing its relative path and purpose.
Use `@section` and `@subsection` for identifiable sections in such long documents:

```cpp
/**
 *  @brief This file provides utilities for data processing.
 *    It includes functions for loading, transforming, and saving data.
 *
 *  @file shared/unum/utilities.hpp
 *  @date November 25, 2015
 *  @author Ash Vardanian
 *
 *  @section libc LibC Usage
 *  Using parts of LibC functionality is discouraged. Prefer C++ STL alternatives
 *  for @c constexpr or third-party alternatives to avoid locale-sensitive behavior
 *  and hidden global state synchronization. 
 */
```

For short inline explanations, use `//` comments.

```cpp
enum class status_t {
    success_k,      // Operation completed successfully
    bad_alloc_k,    // Memory allocation failed
    invalid_arg_k,  // Invalid argument provided
    timeout_k       // Duration exceeded allowed limit
};
```

Use `#pragma region Name` and `#pragma endregion Name` to make sections of code collapsible and navigable in IDEs that support it.


### Dependency Management and Builds

CMake is the preferred build system for C++ projects.
Dependency management is done via `git submodule` or `FetchContent` in CMake.
Use of heavy frameworks is avoided - meaning no - Boost, Poco, Folly, or Qt.
Heavy and low-performance STL functionality is also avoided:

| STL Component        | Replacement                    |
| :------------------- | :----------------------------- |
| `std::function`      | `void(*function)(void *state)` |
| `std::iostream`      | FMT or `std::format`           |
| `std::unordered_map` | Abseil                         |
| `std::regex`         | PCRE2, Intel HyperScan         |

CMake should be kept as simple as possible.
Minimize [generator expressions](https://cmake.org/cmake/help/latest/manual/cmake-generator-expressions.7.html), complex conditionals, and custom functions/macros.
It's also a common pattern to split CMake into many files, including per-directory `CMakeLists.txt` and per-module `cmake/Find*.cmake` files.
Both are discouraged - prefer a single `CMakeLists.txt` at the root.
For projects with bindings to many higher-level languages prefer using their native build systems, such as `setuptools` for Python or `Cargo` for Rust, and avoid CMake altogether.
Such projects, should ideally be bridged from C++ to C 99 via stable C ABI.

### Testing and Benchmarking

Both `GoogleTest` and `GoogleBenchmark` are well tested and widely used frameworks for testing and benchmarking C++ code.
Use both where applicable, integrating with CMake via `FetchContent`.

> [!NOTE]
> For a collection of performance-oriented programming tips, check out [Less Slow C++](https://github.com/ashvardanian/less_slow.cpp).

## Python Code

> [!NOTE]
> For a minimal CMake-free project template for Python libraries PyBind-ing to CUDA/C++ kernels, check out [PyBindToGPUs](https://github.com/ashvardanian/PyBindToGPUs).
> For a collection of performance-oriented programming tips, check out [Less Slow Python](https://github.com/ashvardanian/less_slow.py).

Python code is formatted using `black` with default settings and 120-character line width for wide monitors, same as C++.
Type hints are used wherever possible, avoiding `Any` unless absolutely necessary.
Docstrings follow the Google style guide:

```python
def example_function(param1: int, param2: str) -> bool:
    """Brief one-line description of the function.
    
    Args:
        param1 (int): Description of param1.
        param2 (str): Description of param2.
    Returns:
        bool: Description of the return value.
    Examples:
        >>> example_function(5, "test")
        True
        >>> example_function(0, "")
        False
    """
    pass
```

Use `Args:` for parameters, `Returns:` for return values, and `Raises:` for exceptions.
Start every file with a module-level docstring describing its purpose:

```python
#!/usr/bin/env python3
"""This module provides utilities for data processing.

It includes functions for loading, transforming, and saving data.

Path: shared/unum/utilities.py
Date: November 25, 2015
Author: Ash Vardanian
"""
```

### Dependency Management

Avoid Anaconda and manual environment management.
Prefer `uv` and `pixi` for virtual environment management.
The former is better for CPU-only dependencies, the latter for GPU-accelerated ones and Mojo compatibility.
Both respect `pyproject.toml`.

### Testing and Benchmarking

For testing, use a combination of `doctest` and `pytest`.
The former takes care of `>>>` examples in docstrings, the latter for more complex test cases.
Keep the tests as simple and readable as possible, preferably, without "fixtures" or complex setup/teardown logic.
For benchmarking, consider `pytest-benchmark`, but be aware of its gigantic overhead.
