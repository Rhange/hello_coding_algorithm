const graph = {};

graph["you"] = ["alice", "bob", "claire"];
graph["bob"] = ["anuj", "peggy"];
graph["alice"] = ["peggy"];
graph["claire"] = ["tom", "jonny"];
graph["anuj"] = [];
graph["peggy"] = [];
graph["tom"] = [];
graph["jonny"] = [];

console.log(graph);
console.log(graph.you);
console.log(graph["you"]);
