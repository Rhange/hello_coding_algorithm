const binary_search = (arr, answer) => {
	arr.sort((a, b) => a - b);

	const length = arr.length;
	const centerIndex = Math.floor(length / 2);
	pivot = arr[centerIndex];

	// base case
	if (pivot === answer) {
		return pivot;
	}

	let next_arr;
	if (pivot > answer) {
		next_arr = arr.filter((each, index) => index < centerIndex);
	}
	if (pivot < answer) {
		next_arr = arr.filter((each, index) => index > centerIndex);
	}

	return binary_search(next_arr, answer);
};

const array = [10, 5, 2, 3, 7, 15, 31];

const answer = array[Math.floor(Math.random() * array.length)];

console.log(binary_search(array, answer));
