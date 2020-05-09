'''Output Format

Print the runner-up score.

Sample Input 0

5
2 3 6 6 5
Sample Output 0

5'''

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr =  [i for i in arr if i != max(arr)]
    print(max(arr))
