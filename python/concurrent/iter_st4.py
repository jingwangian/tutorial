#!/usr/bin/env python3


class TokenRecords:
    def __init__(self, token_codes) -> None:
        self.token_codes = token_codes
        self.row_count = 0
        self._records = range(1, 10)

    def __iter__(self):
        for record in self._records:
            for code in self.token_codes:
                token = "{}---{}".format(code, record)
                self.row_count += 1
                yield token

    # def __next__(self):
    #     record = next(self._records)
    #     for code in self.token_codes:
    #         token = "{}---{}".format(code, record)
    #         yield token

        # self.row_count += 1


trs = TokenRecords(['a', 'b', 'c'])

tr = iter(trs)

# for t in tr:
#     print(t)


print(next(tr))
print(next(tr))
print(next(tr))
print(next(tr))

print("row_count = {}".format(trs.row_count))

for i in tr:
    print(i)

print("row_count = {}".format(trs.row_count))
