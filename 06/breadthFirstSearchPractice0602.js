const graph = {};

graph["CAB"] = ["CAT", "CAR"];
graph["CAT"] = ["MAT", "BAT", "CAR"];
graph["CAR"] = ["CAT", "BAR"];
graph["MAT"] = ["BAT"];
graph["BAR"] = ["BAT"];

const search = (start) => {
	let search_queue = [];
	search_queue = [...search_queue, ...graph[start]];
	let searched = [];

	while (search_queue.length !== 0) {
		const position = search_queue.shift();
		if (!searched.includes(position)) {
			if (position.localeCompare("BAT")) {
				return true;
			} else {
				search_queue = [...search_queue, graph[position]];
				searched = [...searched, position];
			}
		}
	}

	return false;
};

console.log(search("CAB"));
