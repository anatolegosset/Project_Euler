def main(max_nb_turns=15):
    factorials = [1]
    for i in range(2, max_nb_turns + 2):
        factorials.append(factorials[-1] * i)

    nb_states = [[-1] * (max_nb_turns + 1) for _ in range(max_nb_turns + 1)]

    def _rec_nb_states(nb_turns, nb_blue):
        if nb_states[nb_turns][nb_blue] != -1:
            return nb_states[nb_turns][nb_blue]
        elif nb_blue > nb_turns:
            nb_states[nb_turns][nb_blue] = 0
            return 0
        elif nb_blue == nb_turns:
            nb_states[nb_turns][nb_blue] = 1
            return 1
        elif nb_blue == 0:
            nb_states[nb_turns][nb_blue] = factorials[nb_turns]
            return factorials[nb_turns]
        else:
            total = _rec_nb_states(nb_turns - 1, nb_blue - 1) + nb_turns * _rec_nb_states(nb_turns - 1, nb_blue)
            nb_states[nb_turns][nb_blue] = total
            return total

    nb_states = _rec_nb_states(max_nb_turns, max_nb_turns // 2 + 1)
    return factorials[max_nb_turns] // nb_states

