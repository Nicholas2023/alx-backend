# Caching Strategies :smile:

This repository contains Python implementations of various caching strategies: Basic, FIFO, LIFO, LRU, MRU, and LFU.

## Description

Caching is a technique used in computer science to temporarily store data in order to improve data retrieval times. Different caching strategies determine how data is stored, accessed, and evicted based on various algorithms.

### Files

- `0-basic_cache.py`: Implements a basic caching system without a limit.
- `1-fifo_cache.py`: Implements a First-In, First-Out (FIFO) caching system.
- `2-lifo_cache.py`: Implements a Last-In, First-Out (LIFO) caching system.
- `3-lru_cache.py`: Implements a Least Recently Used (LRU) caching system.
- `4-mru_cache.py`: Implements a Most Recently Used (MRU) caching system.
- `100-lfu_cache.py`: Implements a Least Frequently Used (LFU) caching system.

Each file contains a Python class that inherits from a `BaseCaching` class and implements specific caching logic based on the respective algorithm.

## Usage

To test these caching strategies, execute the respective `main.py` files associated with each caching implementation.

For example:
```bash
./0-main.py
./1-main.py
# ... and so on for other caching strategies
```

These scripts demonstrate the functionality of each caching system, showing how items are stored, retrieved, and evicted according to the specific caching algorithm.

## Contribution

Feel free to contribute by suggesting optimizations, fixes, or additional caching strategies that could enhance the repository.

## Credits

These caching implementations are part of an educational project in an ALX Software Engineering program.
```

This `README.md` gives a brief overview of what each file contains, how to use them, encourages contributions, and acknowledges the project's origin. You might want to customize it further based on your project's specific needs and details.
