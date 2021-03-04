const max = (arr) => {
	//! base case
	if (arr.length === 2) {
		return arr[0] > arr[1] ? arr[0] : arr[1];
	}
	//! recursive case
	const sub_max = max(arr.slice(1));
	return arr[0] > sub_max ? arr[0] : sub_max;
};

console.log(max([2, 5, 100, 4, 101, 56, 27, 48]));
