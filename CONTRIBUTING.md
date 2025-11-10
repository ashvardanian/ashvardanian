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

| Traditional                  | Preferred                    |
| :--------------------------- | :--------------------------- |
| `#ifdef X`                   | `#if defined(X)`             |
| `#define FILE_NAME_H`        | `#pragma once`               |
| `typedef x y;`               | `using y = x;`               |
| `auto v = expr(); if (v) {}` | `if (auto v = expr(); v) {}` |
| `if (x) { a; } else { b; }`  | `x ? a : b`                  |

The last example can be pushed even further using branchless techniques.
Hand-written SIMD code or 4-8x way unrolled scalar code is often welcomed.
In libraries, attributes should be used to warn if functions are misused:

- `[[nodiscard]]` where the result of function execution can't be silently dropped.
- `[[maybe_unused]]` where the opposite effect is needed.

### Formatting and Styling C++ Code

I use `clang-format` with the configuration defined in `.clang-format` file at the root of the repository.
Similarly, for CMake files, I use `cmake-format` with the configuration defined in `.cmake-format.py`.
Documentation is typically generated using Doxygen, mostly linking `.rst` files to `.md` Markdown files across the repository.

Tools aside, there are things that can't be enforced automatically but are still helpful in large codebases:

- Private names should end with an underscore, e.g., `my_variable_` or `my_type_`.
- Use `snake_case` for everything - variable, function names, templates, namespaces, etc.
- Instantiate types (not templates) should end with `_t`, e.g., `value_t` or `string_view_t`.
- Avoid abbreviations and single-letter names, except for loop indices like `i`, `j`, or `k`.

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
Use `@retval` for enumerated return values.
Mark class template parameters with `@tparam`.
Mark function parameters with direction indicators: `@param[in]`, `@param[out]`, or `@param[inout]`.
Mention them with `@p`.
Mark class/type names and method names with `@c`.
Put examples or multi-token code snippets in `@code{.cpp}` ... `@endcode` blocks.
Use `@b` for bold text and `@a` for italics.
Keep whitespaces on both sides of tags - `[ @p example]` not `[@p example]`.
Start every file with a file-level docstring describing its relative path and purpose:

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

### Dependency Management and Builds

CMake is the preferred build system for C++ projects.
Dependency management is done via `git submodule` or `FetchContent` in CMake.
Use of heavy frameworks is avoided - meaning no - Boost, Poco, Folly, or Qt.
Heavy and low-performance STL functionality is also avoided:

| STL Component        | Replacement                    |
| :------------------- | :----------------------------- |
| `std::function`      | `void(*function)(void *state)` |
| `std::iostream`      | FMT                            |
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
