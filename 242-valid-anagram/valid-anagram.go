func isAnagram(s string, t string) bool {

    if len(s) != len(t) {
        return false
    }

    freq := make(map[rune]int)


    for _, chx := range s {
        freq[chx]++
    }

    for _, ch := range t {
        freq[ch]--

        if freq[ch] < 0 {
            return false
        }   
    }


    return true
}