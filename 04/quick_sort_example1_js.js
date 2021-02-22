const quicksort = (arr) => {
	if (arr.length < 2) {
		return arr;
	} else {
		const pivot = arr[0];
		const less = arr.filter((each, index) => index !== 0 && each <= pivot);
		const greater = arr.filter((each, index) => index !== 0 && each > pivot);
		return [...quicksort(less), pivot, ...quicksort(greater)];
	}
};

console.log(quicksort([10, 2, 5, 7, 1, 8, 9]));
