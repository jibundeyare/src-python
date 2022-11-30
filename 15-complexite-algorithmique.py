# La notation de Landau : O()

# Les complexité algorithmiques par ordre d'efficacité :
#
# 1. O(1)
# 2. O(log(n))
# 3. O(n)
# 4. O(n ** 2)
# 5. O(n ** 3)
# 6. O(n ** n)
# 7. O(exp(n))
# 8. O(factorial(n))

# le nombre maximal de données à traiter
n = 1000

# O(1)
result = n * 123

# O(n)
for i in range(n):
    result = i * 123

# O(n + n) = O(2 * n)
for i in range(n)
    result = i * 123

for j in range(n)
    result = j * 123

# O(n * n) = O(n ** 2)
for i in range(n):
    for j in range(n)
        result = i * j * 123

# O(n * (n + n)) = O(n * n + n * n)) = O(n ** 2 + n ** 2) = O(2 * n ** 2)
for i in range(n):
    for j in range(n)
        result = i * j * 123

    for k in range(n)
        result = i * k * 123

# O(n * n * n) = O(n ** 3)
for i in range(n):
    for j in range(n)
        for k in range(n)
            result = i * j * k * 123

