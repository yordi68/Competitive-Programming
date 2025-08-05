func isAnagram(s string, t string) bool {
    if len(s) != len(t) {
        return false
    }

    hashmap := make(map[rune]int)

    for _, ch := range s {
        hashmap[ch]++
    }

    for _, ch := range t {
        hashmap[ch]--

        if hashmap[ch] < 0 {
            return false
        }
    }

    return true

}