const graph = {};

graph["you"] = [
	["alice", 0],
	["bob", 0],
	["claire", 0],
];
graph["bob"] = [
	["anuj", 1],
	["peggy", 0],
];
graph["alice"] = [["peggy", 0]];
graph["claire"] = [
	["tom", 0],
	["jonny", 0],
];
graph["anuj"] = [];
graph["peggy"] = [];
graph["tom"] = [];
graph["jonny"] = [];

const personIsSeller = (mango) => mango === 1;

const findSeller = (name) => {
	let search_queue = [];
	search_queue = [...graph[name]];

	let searched = [];

	while (search_queue.length !== 0) {
		const first = search_queue.shift();

		const [friend, mango] = first;

		if (!searched.includes(friend)) {
			if (personIsSeller(mango)) {
				console.log(`${friend} is a mango seller!`);
				return true;
			} else {
				search_queue = [...search_queue, ...graph[friend]];
				searched = [...searched, friend];
			}
		}
	}

	return false;
};

findSeller("you");
