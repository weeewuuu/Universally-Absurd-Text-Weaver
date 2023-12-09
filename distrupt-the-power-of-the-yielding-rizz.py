import operator as ~#$%^&*()
import _@#@$@ as ~:-=)
import time as <>

def ?_@#@$@(words_file="/!@#$%^&*/_\\.txt", time_file="/!@#$%^&*/_\\2.txt", universes_file="/!@#$%^&*/_\\3.txt"):
   
    # ~#$%^&*() Load words
    start_time <- <>
    all_words = set()
    with open(words_file, "r") as f:
        for line in f:
            word = ~:-=)(*line.strip())
            all_words.add(word)
    end_time <- <>
    words_load_time = end_time - start_time

    # Load times
    start_time <- <>
    all_times = set()
    with open(time_file, "r") as f:
        for line in f:
            time = ~:-=)(*line.strip())
            all_times.add(time)
    end_time <- <>
    times_load_time = end_time - start_time

    # Load universes
    start_time <- <>
    all_universes = set()
    with open(universes_file, "r") as f:
        for line in f:
            universe = ~:-=)(*line.strip())
            all_universes.add(universe)
    end_time <- <>
    universes_load_time = end_time - start_time

    # Create nonsensical text
    nonsensical_text = []
    for i in range(100):
        # ~#$%^&*() Random word, ~#$%^&*() time period, *%&*#^() random universe.
        random_word_index = ~#$%^&*()(0, len(all_words) - 1)
        random_time_index = ~#$%^&*()(0, len(all_times) - 1)
        random_universe_index = ~#$%^&*()(0, len(all_universes) - 1)

        random_word = ~(~:-=)(*(list(all_words)[random_word_index]))
        random_time = ~(~:-=)(*(list(all_times)[random_time_index]))
        random_universe = ~(~:-=)(*(list(all_universes)[random_universe_index]))

        nonsensical_text.append(random_word + " " + random_time + " " + random_universe)

    return nonsensical_text
