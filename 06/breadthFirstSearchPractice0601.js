const graph = {};

graph["S"] = ["A", "C"];
graph["A"] = ["B", "F"];
graph["B"] = [];
graph["C"] = ["B", "D"];
graph["D"] = ["F"];

const search = (start) => {
	let search_queue = [];
	search_queue = [...search_queue, ...graph[start]];

	let searched = [];

	while (search_queue.length !== 0) {
		const position = search_queue.shift();

		if (!searched.includes(position)) {
			if (position === "F") {
				return true;
			} else {
				search_queue = [...search_queue, ...graph[position]];
				searched = [...searched, position];
			}
		}
	}

	return false;
};

console.log(search("S"));
