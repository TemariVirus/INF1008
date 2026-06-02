import sys

def import_numbers_from_file(filename):
    try:
        with open(filename, 'r') as f:
            contents = f.read().strip()
            return list(map(float, contents.split()))
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.", file=sys.stderr)
        sys.exit(1)
    except ValueError:
        print("Error: File contains non-numeric values.", file=sys.stderr)
        sys.exit(1)

def merge_sort(arr, left, right):
    if left >= right:
        return

    mid = (left + right) // 2
    merge_sort(arr, left, mid)
    merge_sort(arr, mid + 1, right)
    merge(arr, left, mid, right)

def merge(arr, left, mid, right):
    L = arr[left:mid+1].copy()
    R = arr[mid+1:right+1].copy()

    i = j = 0
    k = left

    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <filename>", file=sys.stderr)
        sys.exit(1)

    filename = sys.argv[1]
    numbers = import_numbers_from_file(filename)
    merge_sort(numbers, 0, len(numbers) - 1)

    for num in numbers:
        print(num, end=' ')
    print()

if __name__ == "__main__":
    main()
