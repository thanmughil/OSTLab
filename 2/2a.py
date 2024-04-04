def generate_permutations(numbers):
    def permute(current_index):
        if current_index == len(numbers) - 1:
            result.append(numbers.copy())
            return

        for i in range(current_index, len(numbers)):
            numbers[current_index], numbers[i] = numbers[i], numbers[current_index]
            permute(current_index + 1)
            numbers[current_index], numbers[i] = numbers[i], numbers[current_index]

    result = []
    permute(0)
    return result

all_perm = []
sequence = ['a','b','c']

result_permutations = generate_permutations(sequence)
all_perm.extend([ "".join(map(str,i)) for i in result_permutations])

print(sorted(all_perm))