# 4. Биоинформатика.
def all_subs(t_sequence):
    s_sequences = []
    size = len(t_sequence)
    end = 1 << size
    for i in range(end):
        s_sequence = []  # ∀s_sequence ⊂ t_sequence,∀s_sequence ∈ s_sequences.
        for j in range(size):
            if (i >> j) % 2:
                s_sequence.append(t_sequence[j])
        s_sequences.append(s_sequence)
    return s_sequences


def remove_repeated_elements(current_list):
    new_list = []
    for element in current_list:
        if element not in new_list:
            new_list.append(element)
    return new_list


def main():
    t_sequence = str(input())
    print(len(remove_repeated_elements(all_subs(t_sequence))))


if __name__ == "__main__":
    main()
