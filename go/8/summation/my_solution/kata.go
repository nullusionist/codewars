package kata

func Summation(n int) int {
	// the sleeper must awaken!
	var sum int
	for i := 1; i <= n; i++ {
		sum += i
	}
	return sum
}
