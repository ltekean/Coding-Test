n = int(input())
book_count = {}
max_count = 0

for _ in range(n):
    book = input().strip()
    if book in book_count:
        book_count[book] += 1
    else:
        book_count[book] = 1
    max_count = max(max_count, book_count[book])

most_common_books = [book for book, count in book_count.items() if count == max_count]
most_common_books.sort()

print(most_common_books[0])
