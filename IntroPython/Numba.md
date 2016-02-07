Numba
================
- Numba is an Open Source NumPy-aware optimizing compiler for Python sponsored by Continuum Analytics, Inc. It uses the LLVM compiler infrastructure to compile Python syntax to machine code.

- It is aware of NumPy arrays as typed memory regions and so can speed-up code using NumPy arrays. Other, less well-typed code will be translated to Python C-API calls effectively removing the "interpreter" but not removing the dynamic indirection.

- Numba is also not a tracing jit. It compiles code before it gets run either using run-time type information or type information provided in a decorator.

 -Numba is a mechanism for producing machine code from Python syntax and typed data structures such as those that exist in NumPy.
