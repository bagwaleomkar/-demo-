
def knapsack():
    n = int(input("Enter number of items: "))

    val = []
    wt = []

    for i in range(n):
        val.append(int(input("Enter value: ")))

    for i in range(n):
        wt.append(int(input("Enter weight: ")))

    W = int(input("Enter bag capacity: "))

    dp = [[0] * (W + 1) for i in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, W + 1):

            if wt[i-1] <= w:
                dp[i][w] = max(
                    val[i-1] + dp[i-1][w-wt[i-1]],
                    dp[i-1][w]
                )
            else:
                dp[i][w] = dp[i-1][w]

    print("Maximum value:", dp[n][W])


knapsack()

# Time Complexity: O(n * W)
# Space Complexity: O(n * W)
