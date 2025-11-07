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

Dependency management is done via `git submodule` or `FetchContent` in CMake.
Use of heavy frameworks is avoided - meaning no - Boost, Poco, Folly, or Qt.
Heavy and low-performance STL functionality is also avoided:

| STL Component        | Replacement                    |
| :------------------- | :----------------------------- |
| `std::function`      | `void(*function)(void *state)` |
| `std::iostream`      | FMT                            |
| `std::unordered_map` | Abseil                         |
| `std::regex`         | PCRE2, Intel HyperScan         |

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
 *  @brief Erases all elements in the range [first, last) using const_iterators.
 *    Unlike STL, returns both the iterator following the last erased element and a status code.
 *    On error, some elements may have been erased (partial erase, matches STL's basic guarantee).
 *
 *  @param[in] first Beginning of range to erase.
 *  @param[in] last End of range to erase (not erased).
 *  @return erase_result_t Contains iterator equal to @p last and status of the operation.
 *    Returns first error encountered, or success if all elements erased.
 */
 ```

Use `@see` for external references, `@sa` for internal cross-references, `@note` for attention points.
Use `@retval` for enumerated return values.
Mark class template parameters with `@tparam`.
Mark function parameters with direction indicators: `@param[in]`, `@param[out]`, or `@param[inout]`.
Mention them with `@p`.
Mark class/type names and method names with `@c`.
Put examples or multi-token code snippets in `@code` ... `@endcode` blocks.
Use `@b` for bold text and `@a` for italics.
Keep whitespaces on both sides of tags - `[ @p example]` not `[@p example]`.

## Python Code

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
    """
    pass
```

Use `Args:` for parameters, `Returns:` for return values, and `Raises:` for exceptions.



