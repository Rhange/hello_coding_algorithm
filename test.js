function solution(s) {
	const sorted = s.split("").sort();
	const uniqueSorted = [...new Set(sorted)];
	const upper = [];
	const lower = [];
	for (const char of uniqueSorted) {
		if (char === char.toUpperCase()) {
			upper.push(char);
		} else {
			lower.push(char);
		}
	}

	for (let i = upper.length - 1; i >= 0; i--) {
		for (lowerChar of lower) {
			if (upper[i] === lowerChar.toUpperCase()) {
				return upper[i];
			}
		}
	}
}

str = "aaavabAAVBBddDccffeF";
console.log(solution(str));
