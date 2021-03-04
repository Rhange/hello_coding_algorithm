const count = (arr) => {
	if (arr.length === 0) {
		return 0;
	}
	console.log(arr.slice(1));
	return 1 + count(arr.slice(1));
};

count([1, 2, 3, 4, 5]);
