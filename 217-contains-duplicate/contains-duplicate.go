func containsDuplicate(nums []int) bool {
    freq := make(map[int]int)

    for _ , num := range nums {
        freq[num]++
    }

    for key, _ := range freq {
        if freq[key] > 1 {
            return true
        }
    }

    return false
}