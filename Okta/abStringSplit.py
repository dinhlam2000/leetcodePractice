# function solution(S) {
#     let max = -1;
#     let lengths = [];
#     let count = 1;
#     for (let i = 0; i<S.length; i+=count) {
#         count = 1;
#         for (let j = i+1; j<S.length; ++j) {
#             if (S[i] !== S[j]) {
#                 break;
#             } else count++;
#         }
#         if (count > max) {
#             max = count;
#         }
#         lengths.push(count);
#     }
#
#     let result = 0;
#     for (let l of lengths) {
#         result += (max - l);
#     }
#
#     return result;
# }

def solution(S):
    max = -1
    lengths = []
    count = 1
    i = 0
    while i < len(S):
        count = 1
        j = i + 1
        while j < len(S):
            j = j + 1

            if j >= len(S) or S[i] != S[j]:
                break
            else:
                count += 1
        if count > max:
            max = count
        lengths.append(count)
        i = i + count

    result = 0
    for value in lengths:
        result += (max - value)
    return result

import pdb; pdb.set_trace()
print(solution('babaa'))
