# Pagination Tasks :wink:

This repository contains Python scripts related to pagination, dataset handling, and implementing pagination functionality using classes and methods.

## Files

### 0-simple_helper_function.py

Contains a function `index_range` that takes two integer arguments `page` and `page_size` and returns a tuple specifying the start and end indexes for a given page in a list.

### 1-simple_pagination.py

Implements a `Server` class capable of paginating a dataset of popular baby names stored in a CSV file. It includes a `get_page` method to retrieve specific pages of the dataset based on provided page numbers and sizes.

### 2-hypermedia_pagination.py

Extends the functionality of the `Server` class from the previous task by implementing a `get_hyper` method. This method returns a dictionary with details about the dataset page, including current page number, page size, data, next page number, previous page number, and total number of pages.

### 3-hypermedia_del_pagination.py

Introduces deletion-resilient hypermedia pagination by implementing a `get_hyper_index` method within the `Server` class. This method handles changes in the dataset between queries, ensuring continuity and correct indexing even if rows are deleted.

## Usage

Each Python script can be executed individually and contains test cases in their respective `main` files (`0-main.py`, `1-main.py`, etc.). Execute these `main` files to verify the functionality and behavior of the implemented methods.

To execute:

```bash
python3 0-main.py
python3 1-main.py
python3 2-main.py
python3 3-main.py
```

## Instructions

1. Clone the repository:

```bash
git clone https://github.com/your_username/alx-backend.git
```

2. Navigate to the appropriate directory:

```bash
cd alx-backend/0x00-pagination
```

3. Run individual Python scripts using the instructions mentioned above.

## Requirements

- Python 3.x
- CSV module

## Contributors

- [Nicky- Mane](https://github.com/Nicholas2023)

Feel free to contribute by forking the repository and submitting pull requests or reporting issues.
