func twoSum(nums []int, target int) []int {
	var diff map[int]int = make(map[int]int)
	for i, num := range nums {
		if val, ok := diff[target-num]; ok {
			return []int{val, i}
		}
		diff[num] = i
	}
	return nil
}