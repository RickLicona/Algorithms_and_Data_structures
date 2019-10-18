def insert(hash_table, key, value):
    # SAME HASH KEY, INSERT IN THE SAME INDEX POSITION
    # SAME KEY, REPLACE THE VALUE IN THE INDEX POSITION
    hash_key = hash(key) % len(hash_table)
    print("**********************")
    print("HASH KEY: ", hash_key)
    key_exists = False
    bucket = hash_table[hash_key]
    print("Bucket: ", bucket)
    for i, kv in enumerate(bucket):
        k, v = kv
        print("k--: ", k)
        print("v--: ", v)
        if key == k:
            key_exists = True
            print("\n\nC1")
            print("List: ", bucket)
            print("Key: ", key)
            print("Value: ", value)
            break
    if key_exists:
        bucket[i] = (key, value)
        print("\n\nC2")
        print("i: ", i)
        print("List: ", bucket)
        print("Key: ", key)
        print("Value: ", value)
    else:
        bucket.append((key, value))
        print("\n\nC3")
        print("List: ", bucket)
        print("Key: ", key)
        print("Value: ", value)
        print("\n\n")


def search(hash_table, key):
    hash_key = hash(key) % len(hash_table)
    bucket = hash_table[hash_key]
    for i, kv in enumerate(bucket):
        k, v = kv
        if key == k:
            print("Found: ", key)
            return v


def delete(hash_table, key):
    hash_key = hash(key) % len(hash_table)
    key_exists = False
    bucket = hash_table[hash_key]
    for i, kv in enumerate(bucket):
        k, v = kv
        if key == k:
            key_exists = True
            break
    if key_exists:
        del bucket[i]
        print("Key {} deleted".format(key))
    else:
        print("Key {} not found".format(key))

# Chaining approach (Collision Resolution)
# Table as a nested list (lists inside a list).
hash_table = [[] for _ in range(10)]
print(hash_table)
insert(hash_table, 10, 'Nepal')
insert(hash_table, 25, 'USA')
insert(hash_table, 30, 'India')
print("HASH TABLE: ", hash_table)
print("\n\n*************** SEARCH ***************")
print("Element: ", search(hash_table, 10))

print("\n\n*************** DELETE ***************")

delete(hash_table, 10)
print(hash_table)

