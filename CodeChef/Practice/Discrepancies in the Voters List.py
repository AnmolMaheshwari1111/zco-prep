def main():
    import sys
    data = sys.stdin.read().strip().split()
    n1, n2, n3 = map(int, data[:3])
    freq = {}
    idx = 3
    
    for _ in range(n1):
        num = int(data[idx])
        idx += 1
        freq[num] = freq.get(num, 0) + 1
    for _ in range(n2):
        num = int(data[idx])
        idx += 1
        freq[num] = freq.get(num, 0) + 1
    for _ in range(n3):
        num = int(data[idx])
        idx += 1
        freq[num] = freq.get(num, 0) + 1

    result = [num for num, count in freq.items() if count >= 2]
    result.sort()
    output = [str(len(result))]
    output.extend(str(num) for num in result)
    print("\n".join(output))

if __name__ == "__main__":
    main()